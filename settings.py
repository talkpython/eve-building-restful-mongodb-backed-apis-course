from app import MyBasicAuth

# mongo connection string 
# see https://docs.mongodb.com/manual/reference/connection-string/
MONGO_URI = 'mongodb://localhost:27017/eve-course'

# methods allowed at the resource (collection) endpoint
# POST = add new document(s)
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# methods allowed at the item (document) endpoint
# PATCH = edit a document
# PUT = replace a document
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# CORS support
# Allow access from all domains (javascript/web clients)
# see https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
X_DOMAINS = '*'

# A Python date format used to parse and render datetime values.
#DATE_FORMAT = '%d %b %Y'

# Key for the filters query parameter. Defaults to 'where'.
#QUERY_WHERE = 'find'

# Key for the sort query parameter. Defaults to 'sort'.
#QUERY_SORT = 'orderby'

# List of fields on which filtering is allowed. Defaults to ['*'].
# An empty list means no queries are allowed.
#ALLOWED_FILTERS = []

# True if sorting is supported for GET requests, otherwise False. 
# Can be overridden by resource settings. Defaults to True.
#SORTING = True

# A list of Mongo query operators that are not allowed to be used in 
# resource filters (?where=). Defaults to ['$where', '$regex'].
#MONGO_QUERY_BLACKLIST = ['$where']

# True if pagination is enabled for GET requests, otherwise False. 
# Can be overridden by resource settings. Defaults to True.
#PAGINATION = False

# Key for the pages query parameter. Defaults to 'page'.
#QUERY_PAGE = 'section'

# Key for the max results query parameter. Defaults to 'max_results'.
#MAX_QUERY_RESULT = 'max'

# Default value for QUERY_MAX_RESULTS. Defaults to 25.
#PAGINATION_DEFAULT = 25

# Maximum value allowed for QUERY_MAX_RESULTS query parameter. 
# Values exceeding the limit will be silently replaced with this value. 
# You want to aim for a reasonable compromise between performance and 
# transfer size. Defaults to 50.
#PAGINATION_LIMIT = 50

# True to enable concurrency control, False otherwise. Defaults to True.
#IF_MATCH = True

# True to always enforce concurrency control when it is enabled, False 
# otherwise. Defaults to True. 
#ENFORCE_IF_MATCH = False

# Allows to customize the etag field. Defaults to '_etag'.
#ETAG = 'etag'

# Name for the field used to record a document creation date. 
# This field is automatically handled by Eve. Defaults to '_created'.
#DATE_CREATED = 'created'

# Name of the field used to record a document’s last update date. 
# This field is automatically handled by Eve. Defaults to '_updated'.
#LAST_UPDATED = 'updated'

# When False, this option disables HATEOAS. Defaults to True.
#HATEOAS = False

# Allows to customize the links field. Defaults to '_links'.
#LINKS = 'links'

# Allows to switch JSON rendering on and off. Defaults to True.
#JSON = False

# Allows to switch XML rendering on and off. Defaults to True.
#XML = False

# True to enable JSON key sorting, False otherwise. Defaults to False.
#JSON_SORT_KEYS = True

# Supported JSON content types. Useful when you need support for 
# vendor-specific json types. Please note: responses will still carry the 
# standard application/json type. Defaults to ['application/json'].
#JSON_REQUEST_CONTENT_TYPES = ['application/json']

# Rate limiting
# A tuple expressing the rate limit on GET requests. The first element of 
# the tuple is the number of requests allowed, while the second is the time 
# window in seconds. For example, (300, 60 * 15) would set a limit of 300 
# requests every 15 minutes. Defaults to None.
#RATE_LIMIT_GET = (1, 60)
# Same as above, for POST (replace verb name for other HTTP methods)
#RATE_LIMIT_POST = (1, 60)

##
# API surface (domain) definition
##
people = {
    # A class with the authorization logic for the endpoint. If not provided 
    # the eventual general purpose auth class will be used.
    'authentication': MyBasicAuth,
    # When False, this option disables HATEOAS for the resource. 
    # Defaults to True.
    'hateoas': False,
    # A dict defining the actual data structure being handled by the resource. 
    # Enables data validation. 
    'schema': {
        'firstname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 30,
        },
        'lastname': {
            'type': 'string',
            'maxlength': 50,
            'required': True,
            'unique': True,
        },
        'born': {
            'type': 'datetime',
        },
        # This field is added by app.add_age(). We still need to add it
        # to the schema definition, or it won't be returned to clients.
        'age': {
            'type': 'int',
            # Make sure clients don't try to write to it.
            'readonly': True,
        },
        # 'role' is a list, and can only contain values from 'allowed'.
        'role': {
            'type': 'list',
            'allowed': ['author', 'contributor', 'copy'],
            'default': ['author']
        },
        # 'location' is a subdocument (a dict).
        'location': {
            'type': 'dict',
            'schema': {
                'address': {'type': 'string'},
                'city': {'type': 'string', 'required': True}
            },
        },
        # this only works when app.MyValidator is used, as it brings support
        # for validating a field of type 'email'.
        'email': {'type': 'email'}
    }
}

works = {
    'schema': {
        'title': {
            'type': 'string',
            'required': True,
        },
        'description': {
            'type': 'string',
        },
        'owner': {
            'type': 'objectid',
            'required': True,
            # referential integrity constraint: value must exist in the
            # 'people' collection. Since we aren't declaring a 'field' key,
            # will default to `people._id` (or, more precisely, to whatever
            # ID_FIELD value is).
            'data_relation': {
                'resource': 'people',
                # make the owner embeddable with ?embedded={"owner":1}
                'embeddable': True
            },
        },
    }
}


# A dict holding the API domain definition. 
# See http://python-eve.org/config.html#domain-configuration.
DOMAIN = {
    'people': people,
    'works': works
}