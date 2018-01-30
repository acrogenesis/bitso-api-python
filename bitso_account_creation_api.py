
from bitso_general_api import *



## Required Fields START ##
def required_fields():
    endpoint = "/v3/account_required_fields/"
    try:
        auth_header = getAuthorizationHeaderGET(endpoint)

        headers = {"Authorization":auth_header}
        response = getGETRequestHeaders(endpoint, headers)
    except requests.exceptions.RequestException as e:
        print "Error: " + e
        return {}
    return response.content
## Required Fields  END ##

## Create Account START ##
def create_account(email, given_name, family_name, dob, country_code, security_pin):
    endpoint = "/v3/accounts/"
    try:

        payload_data = { "payload": [
                            {
                                "field_name": "email_address",
                                "field_description": "test@test.test"
                            },
                            {
                                "field_name": "given_names",
                                "field_description": "Test"
                            },
                            {
                                "field_name": "family_names",
                                "field_description": "Testez"
                            },
                            {
                                "field_name": "dob",
                                "field_description": "1971-01-01"
                            },
                            {
                                "field_name": "country_code",
                                "field_description": "mx"
                            },
                            {
                                "field_name": "security_pin",
                                "field_description": "1234"
                            }
                        ]}
        json_payload = json.dumps(payload_data)
        auth_header = getAuthorizationHeaderPOST(endpoint, json_payload)

        headers = {"Authorization":auth_header,'content-type': "application/json"}
        response = getPOSTRequestPayload(endpoint, headers, json_payload)
    except requests.exceptions.RequestException as e:
        print "Error: " + e
        return {}
    return response.content
    ## Create Account  END ##