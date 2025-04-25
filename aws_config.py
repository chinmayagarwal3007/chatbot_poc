import boto3

def get_bedrock_runtime_client():
    return boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1"
    )
