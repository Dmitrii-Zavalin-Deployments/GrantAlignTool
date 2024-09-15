import dropbox
import os
import datetime

def download_pdfs_from_dropbox(dropbox_folder, local_folder, access_token, log_file):
    dbx = dropbox.Dropbox(access_token)

    try:
        os.makedirs(local_folder, exist_ok=True)
        result = dbx.files_list_folder(dropbox_folder)
        log_file.write(f"Listing files in Dropbox folder: {dropbox_folder}\n")
        for entry in result.entries:
            log_file.write(f"Found entry: {entry.name}\n")
            if isinstance(entry, dropbox.files.FileMetadata) and entry.name.endswith('.pdf'):
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

def upload_log_to_dropbox(local_log_path, dropbox_folder, access_token):
    dbx = dropbox.Dropbox(access_token)
    with open(local_log_path, "rb") as f:
        dbx.files_upload(f.read(), os.path.join(dropbox_folder, os.path.basename(local_log_path)), mode=dropbox.files.WriteMode.overwrite)
    print(f"Uploaded log file to Dropbox: {os.path.join(dropbox_folder, os.path.basename(local_log_path))}")