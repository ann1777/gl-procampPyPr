import os
import allure
import request

from Sra config import CONFIG

class BaseSpaseApiclient:
def __init__(self, base_url):
    self.client_key()
    self.base_url()
    self.auth = None
    
def login(self, user):
    payload = {
        "username":user.email,
        "password":user.password,
        "domain":"basespase",
        "rURL":"http://basespase.illumina.com
        "clientVars":" ",
        "originPlatformUrl":"underfined",
        "client":"basespace",
        "deviceType":" ",
        "instrumentType":" ",
        "icsVersion":" ",
        "postLoginAction":" ",
        "workgroupid":" ",
        "responseType":"underfined",
        "scope":"underfined",
        "state":"underfined",
    }
    res=request.post("https://login.illumina.com/
    
def get code(self, scope="browse_global"):
   scope=request.utils.quote(scope)
   res=requests.get("https://basespace.illumina.com/cout)
                    f"redirect_url={self.base_url}/illumina.com}
                    f"response_type={ },
                    f"client_id={   },
                    f"scope={ },
                    "state=login&logout=true",
                    allow redirecrs=False,
                    cookies={  },
                    timeout=(1,120)
                   )
assert res;status_code == 302
code=res.headers_store["location"]
return code
