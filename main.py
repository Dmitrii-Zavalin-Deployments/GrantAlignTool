import os
from extract_text_from_pdf import extract_text_from_pdf
from gpt4all_functions import run_gpt4all

def main():
    pdf_folder = 'pdfs'
    question = "What causes the Northern Lights?"
    data = ""

    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            file_path = os.path.join(pdf_folder, filename)
            data += extract_text_from_pdf(file_path)

    run_gpt4all(data, question)

if __name__ == "__main__":
    main()