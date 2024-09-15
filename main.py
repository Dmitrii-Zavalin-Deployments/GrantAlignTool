import os
from extract_text_from_pdf import extract_text_from_pdf
# from gpt4all_functions import run_gpt4all
from download_from_dropbox import download_pdfs_from_dropbox

def main():
    pdf_folder = 'pdfs'
    dropbox_folder = '/GrantAlignTool'
    access_token = os.getenv('DROPBOX_ACCESS_TOKEN')  # Read from environment variable
    question = "What causes the Northern Lights?"
    data = ""

    # Debugging: Print folder paths
    print(f"Dropbox folder: {dropbox_folder}")
    print(f"Local PDF folder: {pdf_folder}")

    # Download PDFs from Dropbox
    download_pdfs_from_dropbox(dropbox_folder, pdf_folder, access_token)

    # Extract text from PDFs
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            file_path = os.path.join(pdf_folder, filename)
            data += extract_text_from_pdf(file_path)

    print("Data from Dropbox:")
    print(data)
    # Run GPT-4 model
    # run_gpt4all(data, question)

if __name__ == "__main__":
    main()