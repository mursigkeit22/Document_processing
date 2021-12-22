from google.cloud import documentai_v1 as documentai


def launch_ocr_process(project_id: str,
                       location: str,
                       processor_id: str,
                       gcs_input_uri: str,
                       gcs_output_uri: str,
                       gcs_output_uri_prefix: str,
                       timeout: int = 600, ):
    """
        https://cloud.google.com/document-ai/docs/send-request
        Sends a process request to a processor to extract text data from a specified document
        (previously uploaded to Google Cloud Storage).
        When this operation finishes it stores output as a JSON file in a specified Cloud Storage bucket.

        :param project_id:  google project id, can be looked up here https://console.cloud.google.com/iam-admin/settings
        :param location: format is 'us' or 'eu', can be looked up on the processor page
                https://console.cloud.google.com/ai/document-ai/processors
        :param processor_id: create processor in Cloud Console https://console.cloud.google.com/ai/document-ai
        :param gcs_input_uri: path to file in Cloud Storage we want to process in format "gs://bucket_name/filename.pdf"
        :param gcs_output_uri: name of your bucket in cloud storage in format "gs://name-of-bucket"
        :param gcs_output_uri_prefix: folder in your bucket you choose to store the output JSON files,
                e.g. "result" or "result/test". Path will be created if not exists.
        :param filename: name of the file you want to process without extension, e.g. "passport" instead of "passport.pdf"
        :param timeout: max time we are ready to wait for the operation to finish

        """

    # Prepare process request

    opts = {}
    if location == "eu":  # You must set the api_endpoint if you use a location other than 'us', e.g.:
        opts = {"api_endpoint": "eu-documentai.googleapis.com"}
    client = documentai.DocumentProcessorServiceClient(client_options=opts)
    destination_uri = f"{gcs_output_uri}/{gcs_output_uri_prefix}/"
    gcs_documents = documentai.GcsDocuments(
        documents=[{"gcs_uri": gcs_input_uri, "mime_type": "application/pdf"}]  # 'mime_type' can be 'application/pdf',
        # 'image/tiff', and 'image/gif', or 'application/json'
    )
    input_config = documentai.BatchDocumentsInputConfig(gcs_documents=gcs_documents)
    output_config = documentai.DocumentOutputConfig(
        gcs_output_config={"gcs_uri": destination_uri}  # Where to write results
    )
    name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"
    request = documentai.types.document_processor_service.BatchProcessRequest(
        name=name, input_documents=input_config, document_output_config=output_config,
    )

    # Send process request
    print("Begin extracting process...")
    operation = client.batch_process_documents(request)
    operation.result(timeout=timeout)  # Wait for the operation to finish
