from google.cloud import storage


def upload_file(bucket_name: str, destination_blob_name: str, filename: str,):
    """
    Uploads a file to the bucket.
    https://cloud.google.com/storage/docs/samples/storage-upload-file

    :param bucket_name: name of a bucket in google Cloud Storage.
    :param destination_blob_name: name of a file or path to a file,
        e.g. "new.txt" or "testfolder/new.txt" as it will be in Cloud Storage.
        Path to a file will be created if not exists.
    :param filename: The path to file on your local machine you want to upload to Cloud Storage.

    """

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(filename)

    print(
        "File {} uploaded to {} as {}.".format(
            filename, bucket_name, destination_blob_name
        )
    )
