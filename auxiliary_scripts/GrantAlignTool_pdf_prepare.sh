#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if pdftk is installed, if not, install it
if ! command_exists pdftk; then
    echo "pdftk is not installed. Installing pdftk..."
    sudo apt-get update
    sudo apt-get install -y pdftk
fi

# Check if python3 is installed, if not, install it
if ! command_exists python3; then
    echo "python3 is not installed. Installing python3..."
    sudo apt-get update
    sudo apt-get install -y python3
fi

# Check if pip3 is installed, if not, install it
if ! command_exists pip3; then
    echo "pip3 is not installed. Installing pip3..."
    sudo apt-get update
    sudo apt-get install -y python3-pip
fi

# Check if pdfplumber is installed, if not, install it
if ! python3 -c "import pdfplumber" &> /dev/null; then
    echo "pdfplumber is not installed. Installing pdfplumber..."
    pip3 install pdfplumber
fi

# Prompt user for the path to the GrantAlignTool folder
read -p "Please enter the path to the GrantAlignTool folder: " grant_align_tool_path

# Prompt user for the exchange path
read -p "Please enter the path to the exchange folder (where PDFs will be merged and split for GrantAlignTool): " exchange_path

# Ensure the exchange path ends with a slash
exchange_path="${exchange_path%/}/"

# Define paths based on the provided GrantAlignTool folder path
source_path="${grant_align_tool_path}/*.pdf"
final_destination="${grant_align_tool_path}/"

# Copy all PDF files from Windows to WSL
cp $source_path $exchange_path

# Run the PDFMerge.sh script on the exchange path
./PDFMerge.sh "$exchange_path"

# Ask for the name of the PDF file without extension
read -p "Enter the name of the PDF file (without extension): " pdf_name

# Define the specific destination path for the selected PDF
destination_path="${exchange_path}${pdf_name}.pdf"

# Check if the specific PDF file exists
if [[ ! -f "$destination_path" ]]; then
    echo "File not found!"
    exit 1
fi

# Extract text from the merged PDF
extracted_text=$(python3 <<EOF
import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
    except Exception as e:
        print(f"An error occurred: {e}")
    return text

pdf_path = "$destination_path"
text = extract_text_from_pdf(pdf_path)
print(text)
EOF
)

# Save the extracted text to a text file
text_file_path="${exchange_path}${pdf_name}.txt"
echo "$extracted_text" > "$text_file_path"

# Move the text file to the Results folder inside GrantAlignTool folder
results_folder="${grant_align_tool_path}/Results/"
mkdir -p "$results_folder"
mv "$text_file_path" "$results_folder"

# Run the PDFSplit.sh script on the copied file
./PDFSplit.sh "$destination_path"

# Delete the copied PDF file
rm "$destination_path"

# Move all PDF files from WSL to Windows
mv "$exchange_path"*.pdf "$final_destination"

echo "Operation completed successfully."