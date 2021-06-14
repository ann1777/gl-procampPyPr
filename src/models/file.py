from src.config import CONFIG
class FileModel:
    def__init__(
        self,
        file_name = None,
        path = None,
        results_path = None,
        folder_id = None,
        sample_type = None,
        file_priority = CONFIG.DEFAULT_FILE..,
        pricing = None,
        standard_id = None,
        tags = None,
        upload_type = None
    )
    """
    Data model for file
    :param file_name:simple file_name
    :param path:list,path to sample from models
    :param results path:str,path to golden
    :param folder_id:folder_id, if not None
    :param sample_type:file_type fron src
    :param file_priority:file_priority
    :param pricing:analysis cost
    :param standard_id:Standard microbiome[]
    :param tags:tags used to find files
    :param upload_type:can be 'web-upload', 'storage-upload' for external storage
    """
    self.path=[]
    if path is None
        else path
    self.result_path=result_path
    self.folder_id=folder_id
    self.sample_type=sample_type
    self.file_priority=file_priority
    self.pricing=pricing
    self.standard_id=standard_id
    self.tags=tags
    self.upload_type=upload_type
    self._file_name=file_name

    @property
    def file name(self):
    if len(self.path) == 0:
        return self.__file_name
    if len(self.path)>1:
        #TODO: add smart split of the name
        pass
    return self.path[0].split("/")

    def __repr__(self):
        return(
            f"{self.file_name}:{self.path}"
            f"{self.priority}:{self.pricing}"
        )
    @file_name.setter
    def file_name(self.value):
    self.file_name = value

    res = self.http_session_post()
    self.endpoints.signup,
    json = {
        "email": user.email.lower(),
        "password": user.password,
        "name": user.name,
        "job title": user.job_title,
        "organization": user.organization
    }
    if res.status_code == 400:
        logging.error(msg=res.text)