import logging

import azure.functions as func
from azure.identity import ManagedIdentityCredential
from azure.storage.blob import BlobServiceClient

# def main(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')

#     if name:
#         return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#              status_code=200
#         )


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

     # Initialize a Blob Client instance
    credential = ManagedIdentityCredential()
    blob_service_client = BlobServiceClient(
        account_url="https://sato04storage.blob.core.windows.net",
        credential=credential
    )

    container_client = blob_service_client.get_container_client("sato04container")
    blob_client = container_client.get_blob_client("blobSample.json")


    # Get the metadata
    properties = blob_client.get_blob_properties()
    last_updated = properties.metadata.get('daytime')
    logging.info(last_updated) 
    return func.HttpResponse("Some HTML", status_code=200)