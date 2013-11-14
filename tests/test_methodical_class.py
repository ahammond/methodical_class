__author__ = 'ahammond'

from methodical_class import MethodicalClass
from unittest2 import TestCase


class T(MethodicalClass):
    def get_params(*args, **kwargs):
        return args, kwargs


class TestMethodicalClass(TestCase):

    def test_fcn_has_method(self):
        t = T()
        args, kwargs = t.get_params()
        self.assertEqual(1, len(args))
        self.assertEqual(t, args[0])
        self.assertEqual(1, len(kwargs))
        self.assertItemsEqual(('method',), kwargs.keys())
        self.assertEqual('function', kwargs['method'].__class__.__name__)
        self.assertEqual('get_params', kwargs['method'].__name__)
