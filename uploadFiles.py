
import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.waik(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
        with open(local_path,'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite')) 
            
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

   


def main():
    access_token='sl.BNDoV6tsJT3EsPVvEFHMK7NdHLfgf1VpTWTOMcASOaBOSP7UPNiJ8HMx-zWg1KmjsHbGZNYvqt0M4kvsV3Xm8SmR4RxPGZXn4vJXi2a02GH2Qd0HtPGuYE6rxeCCIG2Ccg7s3Sc'
    transferData=TransferData(access_token)

    file_from=input("Enter the file path to transfer : ")
    file_to=input("Enter full path to upload to dropbox : ")

    #API
    transferData.upload_file(file_from,file_to)
    print("file has been moved")

