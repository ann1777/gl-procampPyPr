import errno
import logging
import os
import shutil
import allure
import request

from src.application.api.helpers.artifacts import 

class WebApiClient:
    api_key = None
    def __init__(self, auth_provider, base)
    self.tsv=TSV(self)
    self.ca=CA(self)
    self.s3=S3(self)
    self.delayed_report=DelayedReport(self)
    self.storage=StorageAPI(self)
    self.pricing=Pricing(self)
    self.refdb_search=RefDBSearch(self)
    self.sra=SampleRunsArtifacts(self)
    self.ffint=FFInt(self)
    self.wait=Waiters(self)
    self.upload=Upload(self)
    self.validator=validation(self)
    self.http_session=cosmosHttpSession(self)
    self.auth_provider=auth_provider(self)
    self.endpoint=CIDEndpoint(self)
   
def destroy(self):
    self.logout()

@property
def user_email(self):
    """
    Get user email from session object
    :return: User email
    """
    return self.http_session.user.email
..../

def login(self, user: UserModel, expires= ):
    """
    Init session object for api client
    :return: session
    """
    self auth_provider.login(user, self.http )
    returm self.http_session.user.email
    
def logout(self, userModel, expires=  ):
    """
    Definit session for api client
    :return: bool
    """
    self.auth_provider.logout(self.http_session)
    return True
    
def create_user(self, user):
    """
    Create a new user
    """
    
res=self.http_session.post(self, endpoints.signup,
    json={
        "email":user.email.lower(),
        'password":user.password,
        "name":user.name,
        "job_title":user.job_title,
        "organization":user.organization
        }
   )
if res.status_code == 400:
    logging.error(msg=res.text)
    
@allure.step("Generate API key for current user")
def generate_api_key(self):
    """
    Generate api_key
    :return: api_key
    """
res=self.http_session.put(self.endpoint)
res.raise for status()
data=res.json
self.http_session.user.api_key=
return self.http.session.user.api_key

@allure.step("Reset_password for user")
def reset_password(self, email:str):
    """
    Reset password
    :param email: user_email
    :return: response
    """
res=self.http_session.post
(self.endpoints.reset_password, 
 json={"email":email},
 res.raise_for_status()
 return res

@allure.step("Set new_pasword for user"}
def set_new_password_by_personal_link(self, new_password:str)
    """
    Set new password using reset password
    TODO: Should use pop 3 or imap read email
    now getting information From Redis
    :param email:User_email for wich
    :param new_password:New_password to be set
    :return:response
    """
    response=CacheProvider.get_redis().get
    if response is None:
             raise ValeError("Result received from...")
    uuid=str(response).split(" ' ")
    res=self.http-session.post(
        self.endpoints.reset_password and setup 
        json={"password":new_password},
    )
    res.raise_for_status()
    return res
             
@allure.step("Change password to new_password")
def chamge_password(self, new_password:str)
   """
   Change password
   :param new_password:new_password
   :return:response
   """
res=self,http_session.post(
    self.endpoints.change_password,
    json={"password":new_password}
             
                        
            
                           
                           
    
    


