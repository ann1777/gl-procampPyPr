from cosmos.config.validators import RequiredValid

class Config(BaseConfig):
    def __init__(self):
        config_path = f"env_configs/{os.environ['TARGET']}.json"
        scout_spec_path = (
            f"specifications/scout_index/{os.environ['TARGET']}.yaml"
            if os.environ["TARGET"] == "prod"
            else "specifications/scout_index/dev.yaml"
        )
        app_env = ConfigFromEnvProvider()
        app_json_conf = ConfigFromSimpleJsonProvider(config_path)
        app_defaults = ConfigFromDictProvider(
            {
                "USERS_DATA_PATH": "test_data/users",
                "SAMPLES_DATA_PATH": "test_data/samples",
                "SCHOUT_DATA_PATH": "test_data/scout/search_queries.tsv",
                "WORKFLOW-SPECS_PATH": f"specifications/workflows/{os.environ['TARGET']}",
                "SCOUT_SPECS_PATH": scout_spec_path,
                "GMAIL_IMAP_HOST": "imap.gmail.com",
                "EXPIRES": 86400,
                "LOGGING_LEVEL": "INFO",
                "LOGGING_FORMAT": "%(asctime)s - %(filename)s:%(funcName)s:%(lineno)d",
                "LOGGING_COLORED": "1",
                "DEFAULT_FILE_PRIORITY": "7",
                "AUTO_SAMPLES_FOLDER": "origin_files/automation/",
                "GRID_HUB_URL": "http://selenium.grid.dev.cosmosid.com:4444/wd/hub",
            }
        )
        super(Config. self).__init__()
        self.config_provider = HierarchicalProvider([app_env, app_json_conf, app_defaults])

        self.register_bulk(
            {
                "AUTO_SAMPLES_FOLDER": dict(converter=ToStringCoverter, validators=RequiredValid),
                "DEFAULT_FILE_PRIORITY": dict(converter=ToStringCoverter, validators=RequiredValid),
                "LOGGING_LEVEL": dict(converter=ToStringCoverter, validators=RequiredValid),
                "LOGGING_FORMAT": dict(converter=ToStringCoverter, validators=RequiredValid),
                "LOGGING_COLORED": dict(converter=ToStringCoverter, validators=RequiredValid),
                "USERS_DATA_PATH": dict(converter=ToStringCoverter, validators=RequiredValid),
                "SCOUT_DATA_PATH": dict(converter=ToStringCoverter, validators=RequiredValid),
                "WORKFLOW_SPECS_PATH": dict(converter=ToStringCoverter, validators=RequiredValid),
                "DB_PASS": dict(converter=ToStringCoverter, validators=RequiredValid),
                "DB_CUSTOMER": dict(converter=ToStringCoverter, validators=RequiredValid),
                "ILLUMINA_CLIENT_KEY": dict(converter=ToStringCoverter, validators=RequiredValid)
            }
        )
CONFIG = Config()

