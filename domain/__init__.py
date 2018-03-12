from .people import people
from .works import works

# A dict holding the API domain definition. 
# See http://python-eve.org/config.html#domain-configuration.
DOMAIN = {
    'people': people,
    'works': works,
}