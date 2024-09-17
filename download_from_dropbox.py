import dropbox
import os

def download_pdfs_from_dropbox(dropbox_folder, local_folder, access_token, log_file, file_list_path=None):
    dbx = dropbox.Dropbox(access_token)
    log_file.write("1\n")
    try:
        os.makedirs(local_folder, exist_ok=True)
        log_file.write("2\n")
        result = dbx.files_list_folder(dropbox_folder)
        log_file.write(f"Listing files in Dropbox folder: {dropbox_folder}\n")

        # Read the list of files to download if file_list_path is provided
        files_to_download = []
        if file_list_path and os.path.exists(file_list_path):
            with open(file_list_path, 'r') as file_list:
                files_to_download = [line.strip() + '.pdf' for line in file_list.readlines()]
            log_file.write(f"Files to download: {files_to_download}\n")

        for entry in result.entries:
            log_file.write(f"Found entry: {entry.name}\n")
            if isinstance(entry, dropbox.files.FileMetadata) and entry.name.endswith('.pdf'):
                if not files_to_download or entry.name in files_to_download:
                    local_path = os.path.join(local_folder, entry.name)
                    with open(local_path, "wb") as f:
                        metadata, res = dbx.files_download(path=entry.path_lower)
                        f.write(res.content)
                    log_file.write(f"Downloaded {entry.name} to {local_path}\n")
        log_file.write("Download completed.\n")
    except dropbox.exceptions.ApiError as err:
        log_file.write(f"Error downloading files: {err}\n")
    except Exception as e:
        log_file.write(f"Unexpected error: {e}\n")

def upload_file_to_dropbox(local_file_path, dropbox_folder, access_token):
    dbx = dropbox.Dropbox(access_token)
    with open(local_file_path, "rb") as f:
        dbx.files_upload(f.read(), os.path.join(dropbox_folder, os.path.basename(local_file_path)), mode=dropbox.files.WriteMode.overwrite)
    print(f"Uploaded file to Dropbox: {os.path.join(dropbox_folder, os.path.basename(local_file_path))}")