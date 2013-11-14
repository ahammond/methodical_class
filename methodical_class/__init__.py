__author__ = 'ahammond'

from types import FunctionType


__all__ = ['MethodicalClass']


class MethodicalType(type):
    """
    Wrap all methods so that they have a method parameter that is a self-reference.
    """

    def __new__(mcs, name, bases, dictionary):
        for k, v in dictionary.items():
            # in this context, methods are still just functions, since they haven't yet been bound to an object
            if isinstance(v, FunctionType):
                dictionary[k] = mcs.methodizing_wrapper(dictionary[k])
        return type.__new__(mcs, name, bases, dictionary)

    @classmethod
    def methodizing_wrapper(mcs, method_reference):
        """
        Wrapper around methods that adds a method parameter
        """

        def wrapper(self, *args, **kwargs):
            # TODO: I might also be able to dynamically mangle the calling parameters to prepend method.
            # The idea here would be to have method implicitly declared as a formal parameter.
            # I'm not convinced this is a good idea.
            return method_reference(self, *args, method=method_reference, **kwargs)
        return wrapper


class MethodicalClass(object):
    __metaclass__ = MethodicalType
