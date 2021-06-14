import logging
import allure
import endpoints

class WebApiClient:
    api_key = None
def __init__(self, auth_provider, base_provider):
    self.tsv = TSV(self)
    self.ca = CA(self)
    self.s3 = S3(self)
    self.delayed_report = DelayedReport(self)
    self.storage = StorageAPI(self)
    self.pricing = Pricing(self)
    self.refdb_search = RefDBSearch(self)
    self.sra = SampleRunsArtifacts(self)
    self.ffint = FFInt(self)
    self.wait = Waiters(self)
    self.upload = Upload(self)
    self.validator = validation(self)
    self.http_session = cosmosHttpSession(self)
    self.auth_provider = auth_provider(self)
    self.endpoint = CIDEndpoint(self)

def destroy(self):
    self.logout()

@property
def user_email(self):
    """
    Get user email from session object
    :return: User email
    """
    return self.http_session.user_email(gettext)

def login(self, user: UserModel, expires=self.http_session):
    """
    Init session object for api client
    :return: session
    """
    self.auth_provider.login(self.http_session)
    return self.http_session.user_email(gettext)

def logout(self, userModel, expires=self.http_session):
    """
    Definit session for api client
    :return: bool
    """
    self.auth_provider.logout(self.http_session)
    return True

def create_new_user(self, user):
    """
    Create a new user
    """
    self.user = user(self)
    return user

res = self.http_session.post(self, endpoints.signup):
  json={
     "email": user.email.lower(),
     "password":user.password,
     "name": user.name(),
     "job_title": user.job_title(),
     "organization": user.organization
      }

if res.status_code == 400:
    logging.error(msg=res.text)

@allure.step("Generate API key for current user")
def step_generate_api_key(self):
    """
    Generate api_key
    :return: api_key
    """
res = self.http_session.put(self.endpoints.user.api_key):
res.raise_for_status()
data = res.json()
self.http_session.user.api_key = data[],
return self.http_session.user.api_key

@allure.step("Reset_password for user")
def step_reset_password(self, email:str):
    """
    Reset password
    :param email:user_email
    :return:responce
    """
res=self.http_session.post(self.endpoints.reset_password,
json={"email":email},)
res.raise_for_status()
return res

@allure.step("Set new_pasword {new_rassword}for user{email}by_personal_link")
def set_new_password_by_personal_link(self, email:str, new_password:str):
    """
    Set new password using reset password
    TODO: Should use pop 3 or imap read email
    now getting information From Redis
    :param email:User_email for wich set new password
    :param new_password:New_password to be set
    :return:response
    """
response = CacheProvider.get_redis().get(f"flash.cache_pass_reset_(endpoints)")
if response is None:
raise ValeError("Result received from is None")
res=self.http_session.post(self.endpoints.reset_password,
json={"password":new_password}
)
res.raise_for_status()
return res

@allure.step("Change password to {new_password}")
def chamge_password(self, new_password:str):
    """
    Change password
    :param new_password:new_password
    :return:response
    """
res = self, http_session.post(self.endpoints.change_password,
json={"password":new_password}
)
res.raise_for_status()
return res