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

def get_files(
        gcs_output_uri_prefix,
        filename,
        ):
    # Results are written to GCS. Find output files:
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob_list = list(bucket.list_blobs(
        prefix=f'{gcs_output_uri_prefix}/{filename[:-4]}'))  # находит всё, что есть в папке gcs_output_uri_prefix/, ищет во вложенных папках тоже.
    count = 0
    print("blob_list: ", blob_list)

    for i, blob in enumerate(blob_list):
        # If JSON file, download the contents of this blob as a bytes object.
        if ".json" in blob.name:
            # берем только джейсонки, названия которых совпадают с оригинальным файлом.
            # названия файлов в формате "original_file_name-0.json"
            only_name = get_only_name(blob.name)
            if filename[:-4] == only_name:
                count += 1
                print(f"Fetched part {count}")
                blob_as_bytes = blob.download_as_bytes()
                document = documentai.types.Document.from_json(blob_as_bytes)

                # For a full list of Document object attributes, please reference this page:
                # https://cloud.google.com/document-ai/docs/reference/rpc/google.cloud.documentai.v1beta3#document

                # Read the text recognition output from the processor
                for page in document.pages:
                    for form_field in page.form_fields:
                        field_name = get_text(form_field.field_name, document)
                        field_value = get_text(form_field.field_value, document)
                        print("Extracted key value pair:")
                        print(f"\t{field_name}, {field_value}")
                    for paragraph in page.paragraphs:
                        paragraph_text = get_text(paragraph.layout, document)

                        with open(fr'{result_local_folder}\{filename}.txt', 'a', encoding='utf-8') as f:
                            f.write(paragraph_text)

    # Extract shards from the text field


def get_text(doc_element: dict, document: dict):
    """
    Document AI identifies form fields by their offsets
    in document text. This function converts offsets
    to text snippets.
    """
    response = ""
    # If a text segment spans several lines, it will
    # be stored in different text segments.
    for segment in doc_element.text_anchor.text_segments:
        start_index = (
            int(segment.start_index)
            if segment in doc_element.text_anchor.text_segments
            else 0
        )
        end_index = int(segment.end_index)
        response += document.text[start_index:end_index]
    return response


def get_only_name(blob_name):
    postfix_pos = blob_name.rfind("-")
    name_start = blob_name.rfind("/")
    return blob_name[name_start + 1:postfix_pos]


root_dir = "../work_docs"
filenames = [f for f in listdir(root_dir) if isfile(join(root_dir, f))]

# create folder for results if not exists
os.makedirs(result_local_folder, exist_ok=True)

for file_name in filenames:
    print("Currently processing: ", file_name)
    # create new file or clean up old one, if we have already processed a document with the same name
    with open(fr'{result_local_folder}\{file_name}.txt', 'w', encoding='utf-8') as f:
        pass
    gcs_input_uri = fr"gs://{bucket_name}/{file_name}"  # path to file we want to process in google storage
    get_files( gcs_output_uri_prefix, file_name)