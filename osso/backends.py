from social_core.backends.oauth import BaseOAuth2
from urllib.parse import urlencode

class Osso(BaseOAuth2):
    """Osso OAuth authentication backend"""
    name = 'osso'
    REDIRECT_STATE = False
    STATE_PARAMETER = True
    AUTHORIZATION_URL = 'https://demo.ossoapp.com/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://demo.ossoapp.com/oauth/token'
    ACCESS_TOKEN_METHOD = 'POST'
    SCOPE_SEPARATOR = ','
    EXTRA_DATA = [
        ('id', 'id'),
    ]

    def auth_params(self, state=None):
        client_id, _client_secret = self.get_key_and_secret()
        params = {
            'client_id': client_id,
            'redirect_uri': self.get_redirect_uri(state)
        }
        if self.data.get('email'):
            params['email'] = self.data.get('email')
        if self.data.get('domain') and not self.data.get('email'):
            params['domain'] = self.data.get('domain')
        if self.STATE_PARAMETER and state:
            params['state'] = state
        if self.RESPONSE_TYPE:
            params['response_type'] = self.RESPONSE_TYPE
        return params


    def get_user_details(self, response):
        """Return user details from Osso"""
        return {'username': response.get('login') or '',
                'email': response.get('email') or ''}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = 'https://demo.ossoapp.com/oauth/me?' + urlencode({
            'access_token': access_token
        })
        return self.get_json(url)