class Config(BaseConfig):
def__init__(self):
config_path = f"env_configs/{os.enwiron..."
if os.environ["TARGET"] == "qa"
    else "specifications/scout_index/qa.y..."
)
app_env = ConfigFromEnvProvider()
app_json_conf = ConfigFromSimpleJsonProvid...
app_defaults = ConfigFromDictProvider(
"USERS_DATA_PATH": "data/user..."
"SAMPLES_DATA_PATH": "data/sampl..."
"SCOUT_DATA_PATH": f"specifications/workf..."
"SCOUT_SPECS_PATH": "scout_spec_path",
"AWS_UPLOADS_BUCKET": "cosm..."
"AWS_SECRET_ACCESS_KEY":
"AWS_ACCESS_KEY_ID": "..."
"AWS_DEFAULT_REGION": "US -..."
"AWS_S3_ENDPOINT_URL": "https://..."
"ADMIN_BASE_UPL": "https://..."
"UTOOL_BASE_URL":
"CLI_BASE_URL":
"CLI_INSTALL_PARAMS":
"CLI_VERSION":
"SCOUT_BASE_URL":
"ILLUMINA_CLIENTT_..."
"REDIS_PORT": "6379" +
"REDIS_HOST": ".."