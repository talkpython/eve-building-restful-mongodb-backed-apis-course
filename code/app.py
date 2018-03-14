from redis import Redis

from eve import Eve

from auth import MyBasicAuth
from validation import MyValidator
from callbacks import inject_signature, add_age

app = Eve()

@app.route('/hello')
def hello():
    """ A Eve instance is still a 100% Flask application """
    return 'Hello, world!'

# attach a callback function to GET requests.
app.on_fetched_item += inject_signature
# attach a callback function to POST requests.
app.on_insert += add_age