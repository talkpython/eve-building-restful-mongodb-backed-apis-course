from app import MyBasicAuth

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