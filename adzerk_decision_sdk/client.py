import copy
import re
import six
from importlib import import_module
from pydoc import locate
from urllib.parse import urlparse, parse_qsl, urlencode, ParseResult
from adzerk_decision_sdk.rest import RESTClientObject
from adzerk_decision_sdk.api_client import ApiClient
from adzerk_decision_sdk.configuration import Configuration
from adzerk_decision_sdk.api.decision_api import DecisionApi
from adzerk_decision_sdk.api.userdb_api import UserdbApi
from adzerk_decision_sdk.models import Decision

class Client(object):
    class _DecisionClient(object):
        reverse_attribute_cache = {}

        def __init__(self, network_id, site_id, api_client: ApiClient):
            self.api_client = api_client
            self.network_id = network_id
            self.site_id = site_id
            self.api = DecisionApi(api_client)

        def get(self, request, **kwargs):
            if 'decision_request' not in kwargs:
                kwargs['decision_request'] = request if type(request) is dict else Client._DecisionClient._to_dict(request)

            for idx, placement in enumerate(kwargs['decision_request']['placements']):
                if 'network_id' not in placement:
                    placement['network_id'] = self.network_id
                if 'site_id' not in placement:
                    placement['site_id'] = self.site_id
                if 'div_name' not in placement:
                    placement['div_name'] = f'div{idx}'

            if ('include_explanation' in kwargs and kwargs['include_explanation']) or 'user_agent' in kwargs:
                api_client = copy.deepclone(self.api_client)
                if 'include_explanation' in kwargs and kwargs['include_explanation']:
                    api_client.set_default_header('X-Adzerk-Explain', api_client.configuration.api_key)
                if 'user_agent' in kwargs:
                    api_client.set_default_header('user-agent', kwargs['user_agent'])
                api = DecisionApi(api_client)
            else:
                api = self.api

            return self._parse_response(api.get_decisions(**kwargs))

        @classmethod
        def _to_dict(cls, obj):
            """Patched version of the generated to_dict to properly set keys"""
            result = {}

            if not hasattr(obj.__class__, 'attribute_map') or not hasattr(obj.__class__, 'openapi_types'):
                return

            for attr, _ in six.iteritems(obj.__class__.openapi_types):
                value = getattr(obj, attr)
                if isinstance(value, list):
                    result[obj.__class__.attribute_map[attr]] = [
                        cls._to_dict(x) if hasattr(x, 'to_dict') else x for x in value
                    ]
                elif hasattr(value, 'to_dict'):
                    result[obj.__class__.attribute_map[attr]] = Client._DecisionClient._to_dict(value)
                elif isinstance(value, dict):
                    result[obj.__class__.attribute_map[attr]] = dict(map(
                        lambda item: (item[0], Client._DecisionClient._to_dict(item[1]))
                        if hasattr(item[1], 'to_dict') else item,
                        value.items()
                    ))
                else:
                    result[obj.__class__.attribute_map[attr]] = value

            return result

        def _parse_response(self, response):
            for key, value in six.iteritems(response.decisions):
                response.decisions[key] = value if isinstance(value, list) else [value]
                for index, placement in enumerate(response.decisions[key]):
                     response.decisions[key][index] = self.api_client._ApiClient__deserialize(placement, Decision)

            return response

        @classmethod
        def _reverse_attribute_map(cls, attribute_map):
            r = {}
            for key, value in six.iteritems(attribute_map):
                r[value] = key

            return r

    class _UserDbClient(object):
        def __init__(self, network_id, api_client: ApiClient):
            self.api = UserdbApi(api_client)
            self.network_id = network_id

        def set_custom_properties(self, user_key, properties, **kwargs):
            network_id = kwargs['network_id'] if 'network_id' in kwargs else self.network_id
            return self.api.add_custom_properties(network_id,
                                                  user_key,
                                                  body=properties)

        def add_interest(self, user_key, interest, **kwargs):
            network_id = kwargs['network_id'] if 'network_id' in kwargs else self.network_id
            return self.api.add_interests(network_id,
                                          user_key,
                                          interest)

        def add_retargeting_segment(self,
                                    user_key,
                                    advertiser_id,
                                    retargeting_segment_id,
                                    **kwargs):
            network_id = kwargs['network_id'] if 'network_id' in kwargs else self.network_id
            return self.api.add_retargeting_segment(network_id,
                                                    advertiser_id,
                                                    retargeting_segment_id,
                                                    user_key)

        def forget(self, user_key, **kwargs):
            network_id = kwargs['network_id'] if 'network_id' in kwargs else self.network_id
            return self.api.forget(network_id, user_key)

        def gdpr_consent(self, consent_request, **kwargs):
            network_id = kwargs['network_id'] if 'network_id' in kwargs else self.network_id
            return self.api.gdpr_consent(network_id, consent_request=consent_request)

        def ip_override(self, user_key, ip, **kwargs):
            network_id = kwargs['network_id'] if 'network_id' in kwargs else self.network_id
            return self.api.ip_override(network_id, user_key, ip)

        def match_user(self, user_key, partner_id, user_id, **kwargs):
            network_id = kwargs['network_id'] if 'network_id' in kwargs else self.network_id
            return self.api.match_user(network_id,
                                       user_key,
                                       partner_id,
                                       user_id)

        def opt_out(self, user_key, **kwargs):
            network_id = kwargs['network_id'] if 'network_id' in kwargs else self.network_id
            return self.api.opt_out(network_id, user_key)

        def read(self, user_key, **kwargs):
            network_id = kwargs['network_id'] if 'network_id' in kwargs else self.network_id
            return self.api.read(network_id, user_key)

    class _PixelClient(object):
        def __init__(self, configuration):
            self.rest_client = RESTClientObject(configuration)

        def fire(self, url, revenue_override=None, additional_revenue=None, **kwargs):
            parsed_url = urlparse(url)
            query_string_params = parse_qsl(parsed_url.query)
            if revenue_override is not None:
                query_string_params.append(('override', revenue_override))
            if additional_revenue is not None:
                query_string_params.append(('additional', additional_revenue))
            new_query = urlencode(query_string_params)
            full_url = ParseResult(
                parsed_url.scheme, parsed_url.netloc, parsed_url.path,
                parsed_url.params, new_query, parsed_url.fragment
            ).geturl()

            result = self.rest_client.GET(url)

            return result.status == 200

    def __init__(self, network_id, protocol='https',
                 host=None, path=None, api_key=None,
                 user_agent=None, logger_format=None,
                 logger_file=None, is_debug=False, site_id=None):
        host = f'{protocol}://e-{network_id}.adzerk.net' if host is None else host

        configuration = Configuration(host,
                                      api_key={'X-Adzerk-ApiKey': api_key})

        if logger_format is not None:
            configuration.logger_format = logger_format

        if logger_file is not None:
            configuration.logger_file = logger_file

        api_client = ApiClient(configuration)
        api_client.set_default_header('X-Adzerk-Sdk-Version', 'adzerk-decision-sdk-python:v1')

        self.decision_client = self._DecisionClient(network_id, site_id, api_client)
        self.user_db_client = self._UserDbClient(network_id, api_client)
        self.pixel_client = self._PixelClient(configuration)

    @property
    def decisions(self):
        return self.decision_client

    @property
    def user_db(self):
        return self.user_db_client

    @property
    def pixels(self):
        return self.pixel_client
