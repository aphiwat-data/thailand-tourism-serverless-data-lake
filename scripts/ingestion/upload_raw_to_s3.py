import os
from datetime import datetime
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "ap-southeast-1")
S3_BUCKET = os.getenv("S3_BUCKET_NAME")
S3_PREFIX = os.getenv("S3_PREFIX", "raw/tourism_domestic")

def upload_file(local_path: str, s3_key: str) -> None:
    s3 = boto3.client("s3", region_name=AWS_REGION)
    try:
        s3.upload_file(local_path, S3_BUCKET, s3_key)
        print(f"✅ Uploaded: s3://{S3_BUCKET}/{s3_key}")
    except ClientError as e:
        raise RuntimeError(f"Upload failed: {e}")

if __name__ == "__main__":
    if not S3_BUCKET:
        raise SystemExit("❌ Missing S3_BUCKET_NAME in .env")

    # change this to your actual dataset file name
    local_file = "data/raw/thailand_domestic_tourism_2019_2023_ver2.csv"
    if not os.path.exists(local_file):
        raise SystemExit(f"❌ File not found: {local_file}")

    dt = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    s3_key = f"{S3_PREFIX}/ingestion_dt={dt}/source.csv"

    upload_file(local_file, s3_key)
