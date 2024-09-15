# download_from_dropbox.py
import dropbox
import os

def download_pdfs_from_dropbox(dropbox_folder, local_folder, access_token):
    dbx = dropbox.Dropbox(access_token)
    
    try:
        os.makedirs(local_folder, exist_ok=True)
        for entry in dbx.files_list_folder(dropbox_folder).entries:
            if isinstance(entry, dropbox.files.FileMetadata) and entry.name.endswith('.pdf'):
                local_path = os.path.join(local_folder, entry.name)
                with open(local_path, "wb") as f:
                    metadata, res = dbx.files_download(path=entry.path_lower)
                    f.write(res.content)
        print("Download completed.")
    except Exception as e:
        print(f"Error downloading files: {e}")