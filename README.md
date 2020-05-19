# Adzerk Decision Python SDK

Python SDK for Adzerk Decision & UserDB APIs

## Installation

Requires [Python 3.7.6](https://en.wikipedia.org/wiki/History_of_Python#Table_of_versions) or higher.

```shell
pip install adzerk-decision-sdk
```

Or add to your `requirements.txt` file:

```
adzerk-decision-sdk===1.0.0
```

## Examples

### API Credentials & Required IDs

- Network ID: Log into [Adzerk UI](https://app.adzerk.com/) & use the "circle-i" help menu in upper right corner to find Network ID. Required for all SDK operations.
- Site ID: Go to [Manage Sites page](https://app.adzerk.com/#!/sites/) to find site IDs. Required when fetching an ad decision.
- Ad Type ID: Go to [Ad Sizes page](https://app.adzerk.com/#!/ad-sizes/) to find Ad Type IDs. Required when fetching an ad decision.
- API Key: Go to [API Keys page](https://app.adzerk.com/#!/api-keys/) find active API keys. Required when writing to UserDB.
- User Key: UserDB IDs are [specified or generated for each user](https://dev.adzerk.com/reference/userdb#passing-the-userkey).

### Fetching an Ad Decision

```python
import adzerk_decision_sdk

# Demo network, site, and ad type IDs; find your own via the Adzerk UI!
client = adzerk_decision_sdk.Client(23, site_id=667480)

request = {
  "placements": [{"adTypes": [5]}],
  "user": {"key": "abc"},
  "keywords": ["keyword1", "keyword2"],
}

response = client.decisions.get(request)
print(response)
```

### UserDB: Reading User Record

```python
import adzerk_decision_sdk

# Demo network ID; find your own via the Adzerk UI!
client = adzerk_decision_sdk.Client(23)
record = client.user_db.read("abc")
print(record)
```

### UserDB: Setting Custom Properties

```python
import adzerk_decision_sdk
import os

# Requires setting API key in "$ADZERK_API_KEY" environ variable
API_KEY = os.environ["ADZERK_API_KEY"]

# Demo network ID; find your own via the Adzerk UI!
client = adzerk_decision_sdk.Client(23, api_key=667480)

props = {
  "favoriteColor": "blue",
  "favoriteNumber": 42,
  "favoriteFoods": ["strawberries", "chocolate"],
}

client.user_db.set_custom_properties("abc", props)
```

<!-- ### Logging Example

TBD: ....... -->

## Documentation

- [Adzerk API Documentation](https://dev.adzerk.com/reference)
- [Adzerk User & Developer Documentation](https://dev.adzerk.com/docs)

## Contributing

### Reporting Issues

- For bug fixes and improvements to this SDK please use Github to [open an issue](https://github.com/adzerk/adzerk-decision-sdk-python/issues) or send us a [pull request](https://github.com/adzerk/adzerk-decision-sdk-python/pulls).
- For questions or issues regarding Adzerk functionality, please [contact Adzerk support](https://adzerk.com/help/).

### Building

To install dependencies and run the builds associated with this SDK, please use:

```
pip install --requirement requirements.txt
[QUESTION: how to run the build?]
```
