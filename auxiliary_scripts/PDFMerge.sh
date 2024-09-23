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

# Check if the script was called with a parameter
if [ -z "$1" ]; then
    # Prompt user for the directory containing the PDF files
    read -p "Please enter the directory containing the PDF files: " pdf_dir
else
    # Use the parameter as the directory containing the PDF files
    pdf_dir="$1"
fi

# Check if the directory exists
if [[ ! -d "$pdf_dir" ]]; then
    echo "Directory not found!"
    exit 1
fi

# Find all PDF files in the directory
pdf_files=("$pdf_dir"/*.pdf)

# Check if there are any PDF files in the directory
if [ ${#pdf_files[@]} -eq 0 ]; then
    echo "No PDF files found in the directory!"
    exit 1
fi

# Define the output merged PDF file
merged_pdf="$pdf_dir/merged.pdf"

# Merge all PDF files into one
pdftk "${pdf_files[@]}" cat output "$merged_pdf"

# Check if the merge was successful
if [ $? -eq 0 ]; then
    echo "Merged PDF created successfully: $merged_pdf"
    # Delete the original PDF files
    rm "${pdf_files[@]}"
    echo "Original PDF files deleted."
else
    echo "Failed to merge PDF files."
    exit 1
fi

echo "Operation completed successfully."