import os

from google_AI.credentials import config
from google.cloud import language_v1

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


def sample_classify_text(gcs_content_uri):
    """
    Classifying Content in text file stored in Cloud Storage

    :param gcs_content_uri: Google Cloud Storage URI where the file content is located.
            e.g. gs://[Your Bucket]/[Path to File]
            The text file must include at least 20 words.
    """

    client = language_v1.LanguageServiceClient()

    # gcs_content_uri = 'gs://cloud-samples-data/language/classify-entertainment.txt'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    document = {"gcs_content_uri": gcs_content_uri, "type_": type_}

    response = client.classify_text(request={'document': document})
    # Loop through classified categories returned from the API
    for category in response.categories:
        # Get the name of the category representing the document.
        # See the predefined taxonomy of categories:
        # https://cloud.google.com/natural-language/docs/categories
        print(u"Category name: {}".format(category.name))
        # Get the confidence. Number representing how certain the classifier
        # is that this category represents the provided text.
        print(u"Confidence: {}".format(category.confidence))


filename = "AG_2406_E-ZA_525.0001__EN__2.0.txt"
gcs_content_uri = fr"gs://{bucket_name}/{filename}"
sample_classify_text(gcs_content_uri)
