import ConfigKeyProvider from HierarhicalProvider

class HierarhicalProvider{ConfgKeyProvider}:
    """
    Allows to create hierarhical override model
    from ex:
    1.Env config (most priority)
    2.Json config (les priority)
    3.Dict config (with defaults)

    In this situation the get key will try return value...,
    In case it not configured (None)=> resolve from 2nd,
    In case it not configured from the list one in the passed...
    """
    def __init__(self, None):
        """
        :param provider: Single item or list of ConfKeyPro
        """
        self.provider = []
        if provider is not None:
            self.add(provider)

    def add(self, provider):
        """
        Adds aditional less priority providers to lookup.
        :param provider: Single item or list of ConfigKeyProvider
        """
        def add_checked(p):
            if issubclass(type(p), ConfigKeyProvider):
                self.provider.append(p)
            else:
                raise ValueError("Provider must be of ConfigKeyProvider")

        if isinstance(provider, collections.Sequence):
            for item in provider:
                add_checked(item)
        else:
            add_checked(provider)
    def get(self, key):
        """
        Returns not None key value from the list best providers
        or None if nothing configured
        :param str key: Key to retrieve
        """
        for provider in self.provider:
            result = provider.get(key)
            if result is not None:
                return result
        return None

class Config(BaseConfig):
def__init__(self);
config_path = f"env_configs/{os.enwiron...";
if(os.environ["TARGET"]=="dev"):

    else "specifications/scout_index/dev.y..."=

    "USERS_DATA_PATH": "test_data/users";
    "SAMPLES_DATA_PATH": "test_data/samples";
    "SCOUT_DATA_PATH": "test_data/scout/search_qu...";
    "WORKFLOW_SPECS_PATH": f"specifications/workflow";
    "SCOUT_SPECS_PATH": "scout_spec_path";
    "GMAIL_IMAP_HOST": "imap.gmail.com";
    "EXPIRES": 86400;
    "LOGGING_COLORED": "1";
    "AUTO_SAMPLES_FOLDER": "origin_files/automation";
    "GRID_HUB_URL": "http://selenium.grid.dev.cosmosid"
    }
)
super(config,self).init()
{
    "AWS_UPLOAD_BUCKET": "cosmosid-samples",
    "AWS_SECRET_ACCESS_KEY": "ExBf32eW6NAITDbS17LNIL0a", zGz4SWt..",
    "ASW_ACCESS_KEY_ID": "AKIAJ2VRMM2B6XYJ2QSA",
    "AWS_DEFAULT_REGION": "us-east-1",
    "AWS_S3_ENDPOINT_URL": "https://s3.amazonaws.com",
    "AWS_APP_BASE_URL": "https://www-int.cosmosid.com",
    "ADMIN_BASE_URL": "https://www-int.cosmosid.com.8443",
    "UTOOL_BASE_URL": "http"//base.cid.int:88",
    "CLI_BASE_URL": "https://rest-int.cosmosid.com",
    "CLI_INSTALL_PARAMS": "--pre --extra-index-url https://pip...",
    "CLI_VERSION": "",
    "SCOUT_BASE_URL": https://compute.cid.int:9004/",
    "ILLUMINA_CLIENT_KEY": "7eab2b89e53a4d3188716d26856783c8",
    "REDIS_PORT": "6379";
    "REDIS_HOST": "ec-cid-int.86dif0.001.usel.cache.amazonaws...",
    "DB_HOST": "rds-int.cex7kunzoekf.us-east-1.rds.amazonaws.com",
    "DB_PORT": "5432",
    "DB_NAME": "cid_int",
    "DB_USER": "cid_int",
    "DB_PASS": "eewisha2Devou6Yae3",
    "DB_CUSTOMER": "test@automation.ua"
    }
