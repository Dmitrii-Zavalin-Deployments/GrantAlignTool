#!/bin/bash

# Function to print a separator for better readability
print_separator() {
    echo "----------------------------------------"
}

echo "Run this script from the local computer"
print_separator

# Ask the user to enter the path to the local GrantAlignTool folder
read -p "Enter the path to your local GrantAlignTool folder: " grantaligntool_path
print_separator

# Navigate to the GrantAlignTool folder
cd "$grantaligntool_path" || { echo "Invalid path. Exiting."; exit 1; }
print_separator

# Navigate to the Projects folder
cd Projects || { echo "Projects folder not found. Exiting."; exit 1; }
print_separator

# Copy the names of all PDF files in the Projects folder
pdf_files=($(ls *.pdf 2>/dev/null))
if [ ${#pdf_files[@]} -eq 0 ]; then
    echo "No PDF files found in the Projects folder. Exiting."
    exit 1
fi
echo "Found PDF files: ${pdf_files[@]}"
print_separator

# Navigate to the Results folder
cd ../Results || { echo "Results folder not found. Exiting."; exit 1; }
print_separator

# Create folders with the names of the PDF files (without extensions) if they do not exist
for pdf_file in "${pdf_files[@]}"; do
    folder_name="${pdf_file%.pdf}"
    if [ ! -d "$folder_name" ]; then
        mkdir "$folder_name"
        echo "Created folder: $folder_name"
    else
        echo "Folder already exists: $folder_name"
    fi
    print_separator
done

# Return to the GrantAlignTool folder
cd "$grantaligntool_path" || { echo "Invalid path. Exiting."; exit 1; }
print_separator

# Move txt files with 'result' in the name to the appropriate folder in Results
for txt_file in *result*.txt; do
    for pdf_file in "${pdf_files[@]}"; do
        project_name="${pdf_file%.pdf}"
        if [[ "$txt_file" == *"$project_name"* ]]; then
            mv "$txt_file" "Results/$project_name/"
            echo "Moved $txt_file to Results/$project_name/"
            print_separator
        fi
    done
done

echo "All tasks completed successfully!"
print_separator