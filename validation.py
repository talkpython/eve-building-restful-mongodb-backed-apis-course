import re

from eve.io.mongo import Validator

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