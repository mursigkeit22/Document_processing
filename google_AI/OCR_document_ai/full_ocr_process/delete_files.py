from google.cloud import storage


def delete_files_from_cloud_storage(bucket_name: str, prefix: str):
    """Deletes a file from the bucket.
    Its containing folder if empty is also deleted.

    :param prefix: file or folder to delete
    :param bucket_name: name of a bucket in google Cloud Storage.
    """

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blobs = list(bucket.list_blobs(prefix=prefix))
    bucket.delete_blobs(blobs)
    for blob in blobs:
        print("File {} deleted.".format(blob.name))
