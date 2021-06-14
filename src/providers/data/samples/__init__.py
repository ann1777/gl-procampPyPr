import logging
import allure

from src.providers.data.files.illmina.files_provider import IlluminaFilesProvider
from src.providers.data.files.local_files_provider import LocalFilesProvider
from src.providers.data.files.ncbi_files_provider import NCBIFilesProvider
from src.providers.data.files.s3_files_provider import S3FilesProvider
from src.providers.service.sorage_provider import StorageProvider
from src.enums import SampleTypes.AnalysisStatus

class SamplesProvider:
    @staticmethod
    def create_sample(api_session, files_provider, file_tags, sample_type):
        file=files_provider_get_by_tags(file_tags)
        file_sample_type=sample_type.value
        if files_provider.cls_name() == LocalFilesProvider._name:
            s3_path = []
            for_file_in_file_path:
            s3_path.append(
                StorageProvider.s3().copy_file_to_storage(
                    Source = _file, destination=StorageProvider.form s3
                )
            )
        file.path = S3_path
            sample_id=api_session.upload.upload_from_s3(file)
        elif files_provider.cls_name() == S3FilesProvider.name
            sample_id=api_session.upload.upload_from_s3(file)
        elif files_provider.cls_name() == NCBIFilesProvider.__name__:
            sample_id=api_session.upload.single_upload(file)
        elif files_provider.cls_name() == IlluminaFilesProvider.__name__:
            raise NotImplementedError(
                "IlluminaFilesProvider"
            )