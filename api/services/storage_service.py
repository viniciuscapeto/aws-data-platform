import boto3
import uuid
from config.settings import S3_BUCKET, AWS_REGION


s3_client = boto3.client(
    "s3",
    region_name=AWS_REGION
)


def upload_file_to_s3(file):
    file_extension = file.filename.split(".")[-1]
    object_name = f"uploads/{uuid.uuid4()}.{file_extension}"

    s3_client.upload_fileobj(
        file.file,
        S3_BUCKET,
        object_name
    )

    return {
        "file_name": file.filename,
        "s3_key": object_name,
        "bucket": S3_BUCKET
    }