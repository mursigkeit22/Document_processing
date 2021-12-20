"""
see example config file for all credentials info
"""

from google_AI.credentials import _0_config
from google.cloud import documentai_v1 as documentai


project_id = _0_config.project_id
location = _0_config.location
processor_id = _0_config.processor_id


def process_document_sample(
        project_id: str, location: str, processor_id: str, file_path: str
):
    # You must set the api_endpoint if you use a location other than 'us', e.g.:
    opts = {}
    if location == "eu":
        opts = {"api_endpoint": "eu-documentai.googleapis.com"}

    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    # The full resource name of the processor, e.g.:
    # projects/project-id/locations/location/processor/processor-id
    name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"

    with open(file_path, "rb") as image:
        image_content = image.read()

    # Read the file into memory
    document = {"content": image_content, "mime_type": "application/pdf"}

    # Configure the process request
    request = {"name": name, "raw_document": document}

    # Recognizes text entities in the PDF document
    result = client.process_document(request=request)

    document = result.document

    print("Document processing complete.")

    # For a full list of Document object attributes, please reference this page:
    # https://googleapis.dev/python/documentai/latest/_modules/google/cloud/documentai_v1beta3/types/document.html
    # #Document

    document_pages = document.pages

    # Read the text recognition output from the processor
    print("The document contains the following paragraphs:")
    for page in document_pages:
        paragraphs = page.paragraphs
        for paragraph in paragraphs:
            paragraph_text = get_text(paragraph.layout, document)
            with open("results_single.txt", "a", encoding="utf-8") as f:
                f.write(paragraph_text)
                print(paragraph_text)


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


file_path = r'..\work_docs\Untitled1.pdf'

# create or clean up file for recognized text
with open("results_single.txt", "w", encoding="utf-8") as f:
    pass

process_document_sample(project_id, location, processor_id, file_path)
