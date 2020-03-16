# adzerk-decision-sdk
Adzerk Decision API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import adzerk_decision_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import adzerk_decision_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.rest import ApiException
from pprint import pprint


# Defining host is optional and default to https://e-23.adzerk.net
configuration.host = "https://e-23.adzerk.net"
# Create an instance of the API class
api_instance = adzerk_decision_sdk.DecisionApi(adzerk_decision_sdk.ApiClient(configuration))
body = {"placements": [{ "divName": "header", "networkId": 23, "siteId": 667480, "adTypes": [5] }] } # object |  (optional)

try:
    api_response = api_instance.get_decisions(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DecisionApi->get_decisions: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://e-23.adzerk.net*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DecisionApi* | [**get_decisions**](docs/DecisionApi.md#get_decisions) | **POST** /api/v2 | 
*UserdbApi* | [**add_custom_properties**](docs/UserdbApi.md#add_custom_properties) | **POST** /udb/{networkId}/custom | 
*UserdbApi* | [**add_interests**](docs/UserdbApi.md#add_interests) | **GET** /udb/{networkId}/interest/i.gif | 
*UserdbApi* | [**add_retargeting_segment**](docs/UserdbApi.md#add_retargeting_segment) | **GET** /udb/{networkId}/rt/{advertiserId}/{retargetingSegmentId}/i.gif | 
*UserdbApi* | [**forget**](docs/UserdbApi.md#forget) | **DELETE** /udb/{networkId} | 
*UserdbApi* | [**gdpr_consent**](docs/UserdbApi.md#gdpr_consent) | **POST** /udb/{networkId}/consent | 
*UserdbApi* | [**ip_override**](docs/UserdbApi.md#ip_override) | **GET** /udb/{networkId}/ip/i.gif | 
*UserdbApi* | [**match_user**](docs/UserdbApi.md#match_user) | **GET** /udb/{networkId}/sync/i.gif | 
*UserdbApi* | [**opt_out**](docs/UserdbApi.md#opt_out) | **GET** /udb/{networkId}/optout/i.gif | 
*UserdbApi* | [**read**](docs/UserdbApi.md#read) | **GET** /udb/{networkId}/read | 
*UserdbApi* | [**set_user_cookie**](docs/UserdbApi.md#set_user_cookie) | **GET** /udb/{networkId}/set/i.gif | 


## Documentation For Models

 - [Consent](docs/Consent.md)
 - [Content](docs/Content.md)
 - [Decision](docs/Decision.md)
 - [DecisionData](docs/DecisionData.md)
 - [Event](docs/Event.md)
 - [GdprConsent](docs/GdprConsent.md)
 - [Placement](docs/Placement.md)
 - [PricingData](docs/PricingData.md)
 - [Request](docs/Request.md)
 - [RequestConsent](docs/RequestConsent.md)
 - [Response](docs/Response.md)
 - [User](docs/User.md)


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-Adzerk-ApiKey
- **Location**: HTTP header


## Author



