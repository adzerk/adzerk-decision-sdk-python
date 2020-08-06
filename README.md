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

# Demo network ID and API key; find your own via the Adzerk UI!
client = adzerk_decision_sdk.Client(23, api_key="YOUR_API_KEY")
client.user_db.forget("abc")
```

### Logging

The Adzerk Decision SDK uses the built-in Python logging mechanism to capture log data. By default, warning and error messages will be sent to `stderr` even if no logger is configured.

To configure different log levels for the SDK, you first have to configure logging for your application. A simple configuration that enables informational level logging application wide would be:

```python
import logging

logging.basicConfig(level=logging.INFO)
```

Now that logging is configured for the application, you can set the log level for the SDK:

```python
client = Client(23)
client.decisions.logger.setLevel(logging.INFO)
```

You will now see informational messages being output from the SDK.

The SDK `Client` also allows you to optionally specify `logger_format` (follows the standard `logging` module format) and `logger_file`. If `logger_file` is provided, logging will continue to show using the application's logging configuration as well as the file specified. The file will only contain Adzerk Decision SDK related logs and can be helpful if communicating issues back to the Adzerk team.

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
