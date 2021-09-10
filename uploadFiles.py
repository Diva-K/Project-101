import dropbox
import os
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for file_name in files:
                local_path=os.path.join(root,file_name)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to, relative_path) 
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path, mode=dropbox.files.WriteMode.overwrite)
                
      

def main():
    access_token='zisFCoQ4u2IAAAAAAAAAAZB7xmso-pEPqFCin6-hLuk5m8fwW03k4cslKUDGOJb7'
    transferData=TransferData(access_token)

    file_from=input("enter the name of the file")
    file_to='/test_dropbox/'

    transferData.upload_file(file_from, file_to)

    print("file has been moved")

main()