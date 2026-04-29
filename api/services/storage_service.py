import boto3
from config.settings import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, S3_BUCKET

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

def upload_file(file):
    s3.upload_fileobj(file.file, S3_BUCKET, file.filename)
    
    url = f"https://{S3_BUCKET}.s3.amazonaws.com/{file.filename}"
    return url