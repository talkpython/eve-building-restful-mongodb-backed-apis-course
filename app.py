import re

from datetime import date
from redis import Redis

from eve import Eve
from eve.io.mongo import Validator
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

class MyValidator(Validator):
    """ You can extend or override the built-in validation rules easily
    by inheriting from the eve.io.mongo.Validator class
    """
    def _validate_isodd(self, isodd, field, value):
        """ Define a brand new 'isodd' rule """
        if isodd and not bool(value & 1):
            self._error(field, 'Value must be an odd number')

    def _validate_type_email(self, field, value):
        """ Extend types by adding a new 'email' type """
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            self._error(field, 'Value is not a valid email address')

def inject_signature(resource, response):
    """ This callback is executed every time a document (item)
    is fetched from the db and it is about to be returned to the client.
    """
    response['_signature'] = "Talk Python Training"

def add_age(resource, items):
    """ This callback is invoked every time a POST request hits the service,
    *before* the documents are sent to the db.
    """
    for item in items:
        if 'born' in item:
            today = date.today()
            item['age'] = today.year - item['born'].year


app = Eve(validator=MyValidator, redis=Redis())

@app.route('/hello')
def hello():
    """ A Eve instance is still a 100% Flask application """
    return 'Hello, world!'

# attach a callback function to GET requests.
app.on_fetched_item += inject_signature

# attach a callback function to POST requests.
app.on_insert += add_age
