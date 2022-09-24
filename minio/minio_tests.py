from re import I
import pytest
import uuid
from pathlib import Path
from minio_client import MinioClientNative


@pytest.fixture()
def bucket_name() -> str:
    return "models"


@pytest.fixture()
def minio_client_native(bucket_name: str) -> MinioClientNative:
    return MinioClientNative(bucket_name=bucket_name)


@pytest.fixture()
def file_to_save(tmp_path: Path) -> Path:
    _file_to_save = tmp_path / f"{uuid.uuid4()}.mock"
    open(_file_to_save, "a").close()
    return _file_to_save


class TestMinioClientNative:
    def test_upload_file(self, minio_client_native: MinioClientNative, file_to_save: Path, tmp_path: Path):
        minio_client_native.upload_file(file_to_save)
        # assert ... check file exists on minio

        path_to_save = tmp_path / "saved_file.mock"
        minio_client_native.download_file(object_name=file_to_save.name, file_path=path_to_save)
        # check file exists locally
        assert path_to_save.exists()
