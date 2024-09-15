import os
import datetime
from extract_text_from_pdf import extract_text_from_pdf
from download_from_dropbox import download_pdfs_from_dropbox, upload_file_to_dropbox
from gpt4all_functions import run_gpt4all

def main():
    pdf_folder = 'pdfs'
    dropbox_folder = '/GrantAlignTool'
    access_token = os.getenv('DROPBOX_ACCESS_TOKEN')  # Read from environment variable
    question = "What causes the Northern Lights?"
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
        # Run GPT-4 model
        answer = run_gpt4all(data, question, log_file)
        log_file.write(f"Answer: {answer}\n")

    # Upload the log file to Dropbox
    upload_file_to_dropbox(log_file_path, dropbox_folder, access_token)

    # Create results file
    results_file_path = os.path.join(pdf_folder, "results.txt")
    with open(results_file_path, "w") as results_file:
        results_file.write(f"Answer: {answer}\n")

    # Upload the results file to Dropbox
    upload_file_to_dropbox(results_file_path, dropbox_folder, access_token)

if __name__ == "__main__":
    main()