"""
Set up credentials: https://cloud.google.com/vision/docs/before-you-begin
You need to have an account, create a project, download a private key as JSON and
create a processor

For batch processing your documents should be uploaded to cloud storage https://console.cloud.google.com/storage

"""

import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"document-ocr-123456-ab123456789cd.json" # when you create a service account key,
# as in before-you-begin guide, a JSON key file is downloaded to your computer

project_id = '111704984007'  # get your project id from https://console.cloud.google.com/iam-admin/settings . Project number will work too.
processor_id = '80d8a23b65b5a14d'  # Create processor in Cloud Console https://console.cloud.google.com/ai/document-ai
location = 'us'  # Format is 'us' or 'eu', can be looked up on the processor page
# https://console.cloud.google.com/ai/document-ai/processors
bucket_name = 'documents-for-ocr'  # bucket name in cloud storage, where you put your files for ocr
result_bucket_folder = 'result_example_name'  # folder in your bucket for output JSON files with extracted text
result_local_folder = 'result_example_name'  # folder on your local computer where you want to save your .txt files with results of google ocr. Will be created if not exists.


