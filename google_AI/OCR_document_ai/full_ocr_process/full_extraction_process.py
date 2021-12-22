"""
see example config file for all credentials info
"""
import os

from google_AI.OCR_document_ai.full_ocr_process.upload_file import upload_file
from google_AI.OCR_document_ai.full_ocr_process.launch_ocr_process import launch_ocr_process
from google_AI.OCR_document_ai.full_ocr_process.download_extracted_text import download_extracted_text
from google_AI.OCR_document_ai.full_ocr_process.delete_files import delete_files_from_cloud_storage
from google_AI.credentials import config
from os import listdir
from os.path import isfile, join

project_id = config.project_id
location = config.location
processor_id = config.processor_id
bucket_name = config.bucket_name
result_bucket_folder = config.result_bucket_folder
result_local_folder = config.result_local_folder


def full_extracting_process(dir_with_docs, project_id,
                            location,
                            processor_id,
                            bucket_name,
                            result_bucket_folder,
                            result_local_folder
                            ):
    """
        Uploads files to Google Cloud Storage, launches extraction process,
     writes extracted text to files on your local machine,
     deletes uploaded files and files with text extraction output from Google Cloud Storage

    :param dir_with_docs: folder on your local machine with files you want to extract text from
    :param project_id:  google project id, can be looked up here https://console.cloud.google.com/iam-admin/settings .
    :param location: format is 'us' or 'eu', can be looked up on the processor page
        https://console.cloud.google.com/ai/document-ai/processors .
    :param processor_id: create processor in Cloud Console https://console.cloud.google.com/ai/document-ai .
    :param bucket_name: name of a bucket in google Cloud Storage.
    :param result_bucket_folder: folder in your bucket for output JSON files with extracted text.
        Will be created if not exists.
    :param result_local_folder: folder on your local computer where you want to save your .txt files with results of google ocr.
        Will be created if not exists.
    """
    filenames = [f for f in listdir(dir_with_docs) if isfile(join(dir_with_docs, f))]

    os.makedirs(result_local_folder, exist_ok=True)  # create folder for output files if not exists
    for filename in filenames:
        filename_without_extension = filename[:-4]
        print("Currently processing: ", filename)
        try:

            with open(fr'{result_local_folder}\{filename_without_extension}.txt', 'w', encoding='utf-8') as f:
                pass  # create new file or clean up old one, if a document with the same name was already processed

            upload_file(bucket_name, filename, f"{dir_with_docs}/{filename}")
            gcs_output_uri = fr"gs://{bucket_name}"  # name of your bucket in cloud storage in format "gs://name-of-bucket"
            input_bucket_uri = fr"gs://{bucket_name}/{filename}"  # path to uploaded file
            output_bucket_prefix = f'{result_bucket_folder}/{filename_without_extension}'  # create separate folder for each output
            launch_ocr_process(project_id,
                               location,
                               processor_id,
                               input_bucket_uri,
                               gcs_output_uri,
                               output_bucket_prefix,
                               timeout=600, )
            download_extracted_text(filename_without_extension, bucket_name, output_bucket_prefix, result_local_folder)
            print("Cleaning Cloud Storage:")
            delete_files_from_cloud_storage(bucket_name, filename)  # delete uploaded file
            delete_files_from_cloud_storage(bucket_name, output_bucket_prefix)  # delete output files
            print()
        except Exception as e:
            print(f"Error processing file {filename}: {e}")


dir_with_docs = "../../work_docs"  # path to folder with files you want to process. Nested folders are ignored.
full_extracting_process(dir_with_docs, project_id,
                        location,
                        processor_id,
                        bucket_name,
                        result_bucket_folder,
                        result_local_folder
                        )
