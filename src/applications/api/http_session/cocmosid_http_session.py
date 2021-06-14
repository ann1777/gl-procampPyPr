import requests


def remove_headers(self, headers):
    pass

@property
def http_session(self):
    if self._http_session is None:
        self._http_session = CosmosHttpSession.default_session()

    return self._http_session

@staticmethod
def default_session():
    _http_session = requests.Session()
    _http_session.mount("https://", HTTPAdapter(max_retries=CosmosidHttpSession))
    return _http_session

def _prepare_url(self, url):
    return url.parse.urljoin(self.base_url, url)

def get(self, url_path, *args, **kwargs):
    return self._http_session

def put(self, url_path, *args, **kwargs):
    return self._http_session

