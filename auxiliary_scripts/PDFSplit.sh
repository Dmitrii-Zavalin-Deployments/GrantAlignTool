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
    # Prompt user for the path to the PDF file
    read -p "Please enter the path to the PDF file: " input_pdf
else
    # Use the parameter as the input PDF file path
    input_pdf="$1"
fi

# Check if the file exists
if [[ ! -f "$input_pdf" ]]; then
    echo "File not found!"
    exit 1
fi

# Get the directory of the input PDF
output_dir=$(dirname "$input_pdf")

# Get the number of pages in the PDF
num_pages=$(pdftk "$input_pdf" dump_data | grep NumberOfPages | awk '{print $2}')

# Determine the number of digits needed for zero-padding
num_digits=${#num_pages}

# Loop through each page and create a separate PDF with leading zeros in the filename
for i in $(seq 1 $num_pages); do
    printf -v page_num "%0${num_digits}d" $i
    output_pdf="$output_dir/page_$page_num.pdf"
    pdftk "$input_pdf" cat $i output "$output_pdf"
    echo "Created $output_pdf"
done

echo "All pages have been split into individual PDFs."