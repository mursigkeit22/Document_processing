from google.cloud import storage
from google.cloud import documentai_v1 as documentai


def download_extracted_text(filename: str, bucket_name, output_bucket_prefix, result_local_folder):
    """
    downloads extracted text, writes text to file to specified folder.


    :param filename: name of the file you processing without extension, e.g. "passport" instead of "passport.pdf".
    :param bucket_name: name of a bucket in google cloud storage.
    :param output_bucket_prefix: folder in your bucket you chose to store the output JSON files,
                e.g. "result" or "result/test".
    :param result_local_folder: path to folder you want to save file with extracted text to.
    """

    # list all the objects in output_bucket_prefix folder including nested folders
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob_list = list(bucket.list_blobs(
        prefix=output_bucket_prefix))

    count_parts = 0  # extracted text can be divided into several documents, so we will count.

    # iterate over found objects. if object is JSON and has name 'filename',
    # download the contents of this blob as a bytes object
    for i, blob in enumerate(blob_list):
        if ".json" in blob.name:
            only_name = get_only_name(blob.name)
            if only_name == filename:
                count_parts += 1
                blob_as_bytes = blob.download_as_bytes()
                print(f"Fetching part {count_parts} of extracted text...")
                document = documentai.types.Document.from_json(blob_as_bytes)

                # Read the text recognition output from downloaded json file
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


def get_only_name(blob_name: str):
    """
    Cuts off path and postfix from blob name:
    google api returns file name with the path from folder we specified as prefix.
    Also when file created, sequence number is added to the filename as a postfix. Blob_name example:
    "result/Untitled1/3568214382860494758/0/Untitled1-0.json"

    :param blob_name: filename in Cloud Storage in format "prefix/still_prefix/3568214382860494758/0/filename-0.json"
    :return: name of the blob (file) without path and postfix number
    """
    postfix_pos = blob_name.rfind("-")
    name_start = blob_name.rfind("/")
    return blob_name[name_start + 1:postfix_pos]
