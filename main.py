import os
import datetime
from extract_text_from_pdf import extract_text_from_pdf
from download_from_dropbox import download_pdfs_from_dropbox, upload_file_to_dropbox
from gpt4all_functions import run_gpt4all
from question_builder import build_question

def main():
    pdf_folder = 'pdfs'
    dropbox_folder = '/GrantAlignTool'
    projects_folder = '/GrantAlignTool/Projects'
    access_token = os.getenv('DROPBOX_ACCESS_TOKEN')  # Read from environment variable
    data = ""

    # Create a unique log file name
    log_file_name = f"log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    log_file_path = os.path.join(pdf_folder, log_file_name)

    # Ensure the local folder exists
    os.makedirs(pdf_folder, exist_ok=True)

    # Open the log file
    with open(log_file_path, "w") as log_file:
        # Debugging: Print folder paths
        log_file.write(f"Dropbox folder: {dropbox_folder}\n")
        log_file.write(f"Local PDF folder: {pdf_folder}\n")

        # Download PDFs from Dropbox
        download_pdfs_from_dropbox(dropbox_folder, pdf_folder, access_token, log_file)

        # Extract text from PDFs
        for filename in os.listdir(pdf_folder):
            if filename.endswith('.pdf'):
                file_path = os.path.join(pdf_folder, filename)
                data += extract_text_from_pdf(file_path)

        log_file.write("Data from Dropbox:\n")
        log_file.write(data + "\n")

        # Process each project file
        for project_filename in os.listdir(projects_folder):
            if project_filename.endswith('.txt'):
                project_file_path = os.path.join(projects_folder, project_filename)
                with open(project_file_path, 'r') as project_file:
                    project_text = project_file.read()

                # Build the question
                question = build_question(project_text, data)
                log_file.write(f"Built question for {project_filename}: {question}\n")

                # Run GPT-4 model
                answer = run_gpt4all(data, question, log_file)
                log_file.write(f"Answer for {project_filename}: {answer}\n")

                # Remove the extension from project_filename
                project_name = os.path.splitext(project_filename)[0]

                # Create results file with a unique name
                results_file_name = f"result_{project_name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                results_file_path = os.path.join(pdf_folder, results_file_name)
                with open(results_file_path, "w") as results_file:
                    results_file.write(f"Log file: {log_file_name}\n\n")
                    results_file.write("Result:\n")
                    results_file.write(f"{answer}\n")

                # Upload the results file to Dropbox
                upload_file_to_dropbox(results_file_path, dropbox_folder, access_token)

    # Upload the log file to Dropbox
    upload_file_to_dropbox(log_file_path, dropbox_folder, access_token)

if __name__ == "__main__":
    main()