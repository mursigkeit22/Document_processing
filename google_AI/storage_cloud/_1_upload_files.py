"""
https://cloud.google.com/storage/docs/samples/storage-upload-file
"""

from google_AI.credentials import config
from google.cloud import storage

bucket_name = config.bucket_name

# The path to your file to upload
source_file_name = "../work_docs/not_pdfs/new.txt"
# name as it will be in the bucket
destination_blob_name = "testfolder/new.txt"


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""



    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}/{}.".format(
            source_file_name, bucket_name, destination_blob_name
        )
    )
upload_blob(bucket_name, source_file_name, destination_blob_name)