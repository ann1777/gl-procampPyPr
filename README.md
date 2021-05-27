## Manual

How to run tests:

1. Execute test directly "src/tests/functional/smoke/LoginTest.python"

2. Execute Test Suite "src/main/resources/testngSmokeTest.xml"

### Tasks:

1. Create framework structure for https://app.cosmosid.com Api documentation: https://docs.cosmosid.com/docs/api-documentation

1.1. It shall contain folders for:

1.1.1. configuration 

1.1.2. application specific libraries/helpers

1.1.3. app api clients

1.1.4. page objects

1.1.5. tests

2. Create Config class

2.1. It shall be possible to set config variables via Environment variables

2.2. It shall be possible to set config variables via YAML file

2.3. It shall be possible to set config variables inside Config class

3. Create class for sending HTTP requests

3.1. It shall be able to send requests:
- GET
- PUT
- POST
- DELETE

