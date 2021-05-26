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
    @property
    def file name(self):
    if len(self.path) == 0:
        return self.__file_name
    if len(self.path)>1:
        pass
    return self.path[0].split("/")[-1]

    def __repr__(self):
        return(
            f"{self.file_name}:{self.path}:{...}"
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