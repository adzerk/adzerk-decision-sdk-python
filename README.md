# Adzerk Python Decision SDK

Python Software Development Kit for Adzerk Decision & UserDB APIs

## Installation

Requires [Python 3.7.6](https://en.wikipedia.org/wiki/History_of_Python#Table_of_versions) or higher.

[PyPI Package](https://pypi.org/project/adzerk-decision-sdk/)

```shell
pip install adzerk-decision-sdk
```

Or add to your `requirements.txt` file:

```
adzerk-decision-sdk===1.0.0b3
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

### Recording Impression & Clicks

Use with the fetch ad example above.

```python
# Impression pixel; fire when user sees the ad
client.pixels.fire(decision.impression_url)

# Click pixel; fire when user clicks on the ad
# status: HTTP status code
# location: click target URL
status, location = client.pixels.fire(decision.click_url)
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

# Demo network ID; find your own via the Adzerk UI!
client = adzerk_decision_sdk.Client(23)

props = {
  "favoriteColor": "blue",
  "favoriteNumber": 42,
  "favoriteFoods": ["strawberries", "chocolate"],
}

client.user_db.set_custom_properties("abc", props)
```

### UserDB: Forgetting User Record

```python
import adzerk_decision_sdk
import os

# Demo network ID and API key; find your own via the Adzerk UI!
api_key = os.environ.get("ADZERK_API_KEY")
client = adzerk_decision_sdk.Client(23, api_key=api_key)
client.user_db.forget("abc")
```

### Decision Explainer

The Decision Explainer returns information on a Decision API request explaining why each candidate ad was or was not chosen. 

```python
import adzerk_decision_sdk
import os

# Demo network, site, and ad type IDs; find your own via the Adzerk UI!
api_key = os.environ.get("ADZERK_API_KEY")
client = adzerk_decision_sdk.Client(23, site_id=667480)

request = {
  "placements": [{"adTypes": [5]}],
  "user": {"key": "abc"},
  "keywords": ["keyword1", "keyword2"],
}

options = {
  "include_explanation": True,
  "api_key": api_key
}

response = client.decisions.get(request, **options)
print(response)
```

The response returns a decision object with placement, buckets, rtb logs, and result information.
``` json
{
  "div0": {
    "placement": {},
    "buckets": [],
    "rtb_log": [],
    "results": []
  }
}
```
The "placement" object represents a decision in which an ad may be served. A Explainer Request can have multiple placements in the request.
The "buckets" array contains channel and priority information.
The "rtb_logs" array contains information about Real Time Bidding.
The "results" array contains the list of candidate ads that did and did not serve, along with a brief explanation.

### Logging

The Adzerk Decision SDK uses the built-in Python logging mechanism to capture log data. By default, warning and error messages will be sent to `stderr` even if no logger is configured.

To configure different log levels for the SDK, you first have to configure logging for your application. A simple configuration that enables informational level logging application wide would be:

```python
import logging

# This represents your logging framework being initialized, usually by Flask or
# Django, etc.  This will create a base handler that will output to sys.stderr,
# but you can override the config in several ways:
# https://docs.python.org/3/library/logging.html
logging.basicConfig()

# Set both the client & rest loggers to INFO to avoid over-the-wire debug logs.
logging.getLogger("adzerk_decision_sdk.client").setLevel(logging.INFO)
logging.getLogger("adzerk_decision_sdk.rest").setLevel(logging.INFO)

# Demo network ID; find your own via the Adzerk UI!
client = Client(23)
```

As a convenience, you can *optionally* specify a `logger_file` parameter to the Client and it will create an _additional_ Python log handler that will send Adzerk Decision SDK logs to the named file.  A few tips:

1. Depending on your app logging config this might create *duplicate logs* between this file and your normal logging destination.  
2. It's probably a good idea to use the `logging.DEBUG` level in this case to get all the over-the-wire debug info.
3. You can also pass in a `logger_format` parameter to control how the logs will be displayed.  This requires the `logger_file` parameter too.  More info on how to format messages: https://docs.python.org/3/library/logging.html#logrecord-attributes

```python
# OPTIONAL use of an ADDITIONAL logger file for SDK messages only;
# logger_format is optional but ignored unless logger_file is present;
# Demo network ID; find your own via the Adzerk UI!
client = Client(23, logger_file="adzerk-python.log", logger_format="%(asctime)s %(name)s %(levelname)s %(message)s")
```

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
pip install flake8
pip install --requirement requirements.txt
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
python setup.py sdist bdist_wheel
```
