# Grant Alignment Tool

## Overview
This tool aligns project descriptions with grant requirements using GPT-4All. It processes PDF files containing project descriptions and grant requirements, and generates alignment results.

## Usage
1. **Prepare PDF files**:
    - **Project Descriptions**: Place PDF files with project descriptions in the Dropbox folder `/GrantAlignTool/Projects`.
    - **Grant Requirements**: Place PDF files with grant requirements in the Dropbox folder `/GrantAlignTool`.

2. **Update Dropbox Access Token**:
    - Generate a new Dropbox access token for the needed application from Dropbox Developers: https://www.dropbox.com/developers/apps.
    - Update the Dropbox access token in GitHub Actions Secrets.

3. **Run the script**:
    - Trigger the job on GitHub Actions after all the PDF files are uploaded.

4. **Important**:
    - Process one grant at a time. After running the script, delete or move the grant PDF files to avoid confusion for the next run.

## Output
- **Results**: Generated results files are uploaded to the Dropbox folder `/GrantAlignTool`.
- **Logs**: Log files are uploaded to the Dropbox folder `/GrantAlignTool`.

## Notes
- Ensure the `Projects` folder in Dropbox contains only the project description PDFs.
- The script processes each project file and generates a unique result file for each.

## Example
1. **Project Descriptions**:
    - `/GrantAlignTool/Projects/project1.pdf`
    - `/GrantAlignTool/Projects/project2.pdf`

2. **Grant Requirements**:
    - `/GrantAlignTool/grant1.pdf`

3. **Run the script**:
    - Trigger the job on GitHub Actions.

4. **Output**:
    - Results and log files will be uploaded to Dropbox.

## Contact
For any issues or questions, please contact [your_email@example.com].
