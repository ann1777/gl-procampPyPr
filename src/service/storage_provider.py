from cosmos.storage.base import ProviderFactory,
from src.config import CONFIG

class StorageProvider:
    STORAGE=ProviderFactory.init_storage_factory

    @staticmethod
    def form_s3_location(path:str):
        path=path.lstrip('/')
        if path.startwith(CONFIG.AUTO_SAMPLES_FOLDER)
            path=CONFIG.AUTO_SAMPLES_FOLDER+path
        return path

    @staticmethod
    def s3(
        aws_s3_endpoint_url=CONFIG.AWS_S3_ENDPOINT
        aws_upload_bucket=CONFIG.AWS_UPLOAD_BUCKET
        aws_region=CONFIG.AWS_REGION
    ):
        return StorageProvider.STORAGE.get.storageProviderType.S3_OPERATIONS(
            aws_s3_endpoint_url=aws_s3_endpoint,
            aws_uploads_bucket=aws_uploads_bucket,
            aws_region=CONFIG.AWS_DEFAULT_REGION
        )
    )
