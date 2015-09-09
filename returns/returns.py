"""A decorator to return namedtuples."""
from collections import namedtuple
from functools import wraps


def underscore_separated_words_to_camel_case(underscore_separated):
    """
    Convert lowercase underscore-separated name to a CamelCase name.

    :param str underscore_separated:
    :rtype: str
    :return: CamelCase name
    """
    words = (word for word in underscore_separated.split('_') if word != '')
    # `capitalize` would lowercase the rest of letters:
    return ''.join(word[0].upper() + word[1:] for word in words)


def custom_namedtuple(*fields, **kwargs):
    """
    Return a decorator that wraps a function to return a custom namedtuple.

    :param str *fields: list of fields that the returned namedtuple will define (variable arguments
        list)
    :param str name: (optional) the name of namedtuple to be created
    """
    def decorator(fn):
        """Wrap the function to return a custom namedtuple."""
        name = kwargs.get('name')
        if name is None:
            name = underscore_separated_words_to_camel_case(fn.__name__)
        returned_namedtuple = namedtuple(name, fields)

        @wraps(fn)
        def wrapped(*args, **kwargs):
            return_value = fn(*args, **kwargs)
            return returned_namedtuple(*return_value)

        return wrapped

    return decorator
