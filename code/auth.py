from eve.auth import BasicAuth

class MyBasicAuth(BasicAuth):
    """ Custom authentication logic is provided by a subclass of
    eve.auth.BasicAuth
    """
    def check_auth(self, username, password, allowed_roles, resource, method):
        """ Override the base check_outh method to provide your own
        auth logic
        """
        return username == 'admin' and password == 'secret'