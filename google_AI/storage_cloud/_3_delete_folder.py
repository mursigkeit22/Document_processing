import os

from google_AI.credentials import config
from os import listdir
from os.path import isfile, join
from google.cloud import documentai_v1 as documentai
from google.cloud import storage

project_id = config.project_id
location = config.location
processor_id = config.processor_id
bucket_name = config.bucket_name
result_bucket_folder = config.result_bucket_folder
result_local_folder = config.result_local_folder

gcs_output_uri = fr"gs://{bucket_name}"  # name of your bucket in cloud storage in format "gs://name-of-bucket"
gcs_output_uri_prefix = config.result_bucket_folder


# def delete_folder(cls, bucket_name, folder_name):
#     bucket = cls.storage_client.get_bucket(bucket_name)
#     """Delete object under folder"""
#     blobs = list(bucket.list_blobs(prefix=folder_name))
#     bucket.delete_blobs(blobs)
#     print(f"Folder {folder_name} deleted.")

def delete_blob(bucket_name, folder_name):
    """Deletes a blob from the bucket."""

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blobs = list(bucket.list_blobs(prefix=folder_name))
    bucket.delete_blobs(blobs)
    for blob in blobs:
        print("Blob {} deleted.".format(blob.name))


root_dir = "../work_docs"
filenames = [f for f in listdir(root_dir) if isfile(join(root_dir, f))]

for filename in filenames:
    delete_blob(bucket_name, f"{result_bucket_folder}/{filename[:-4]}")
    # delete_blob(bucket_name, filename)
