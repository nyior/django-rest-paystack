import pytest
import json

from django.utils.encoding import force_str


@pytest.mark.usefixtures("client")
class RequestMixin(object):

    def send_request(self, **kwargs):
        request_method = kwargs.get('request_method').lower()
        request_url  =   kwargs.get('request_url')

        if 'content_type' not in kwargs and request_method != 'get':
            kwargs['content_type'] = 'application/json'
        if 'payload' in kwargs and request_method != 'get' and kwargs['content_type'] == 'application/json':
            payload = kwargs.get('payload', '')
            kwargs['payload'] = json.dumps(payload)
        
        if  request_method == "post":
            response = self._client.post(
                request_url,
                data=kwargs['payload']
            )
        if request_method == "get":
            response = client.get(
                request_url
            )
        
        is_json = 'application/json' in response.get('content-type', '')

        if is_json and response.content:
            response = json.loads(force_str(response))

        return response