import dropbox
import os

def download_pdfs_from_dropbox(dropbox_folder, local_folder, access_token):
    dbx = dropbox.Dropbox(access_token)
    print("1")
    try:
        os.makedirs(local_folder, exist_ok=True)
        print("2")
        result = dbx.files_list_folder(dropbox_folder)
        print(f"Listing files in Dropbox folder: {dropbox_folder}")
        for entry in result.entries:
            print(f"Found entry: {entry.name}")
            if isinstance(entry, dropbox.files.FileMetadata) and entry.name.endswith('.pdf'):
                local_path = os.path.join(local_folder, entry.name)
                with open(local_path, "wb") as f:
                    metadata, res = dbx.files_download(path=entry.path_lower)
                    f.write(res.content)
                print(f"Downloaded {entry.name} to {local_path}")
        print("Download completed.")
    except dropbox.exceptions.ApiError as err:
        print(f"Error downloading files: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")