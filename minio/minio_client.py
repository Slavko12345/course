from pathlib import Path
from minio import Minio

ACCESS_KEY = "minio"
SECRET_KEY = "minio123"
ENDPOINT = "0.0.0.0:9000"

class MinioClientNative:
    def __init__(self, bucket_name: str) -> None:
        client = Minio(ENDPOINT, access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)

        self.client = client
        self.bucket_name = bucket_name

    def upload_file(self, file_path: Path):
        self.client.fput_object(self.bucket_name, file_path.name, file_path)

    def download_file(self, object_name: str, file_path: Path):
        self.client.fget_object(bucket_name=self.bucket_name, object_name=object_name, file_path=str(file_path))