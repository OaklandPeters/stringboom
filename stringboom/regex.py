"""
Heavily inspired by func/strings.py
"""
from __future__ import absolute_import
import re
import operator
import functools
#from .shared import identity

__all__ = ['re_iter', 're_find', 're_all', 're_test', 'make']


#==============================================================================
#        Core Function(s)
#==============================================================================
#Note similarity to my construction of iterget(), get(), and get_all()
def re_iter(regex, _string, flags=0):
    """Returns iterator over groups resulting from testing regex."""
    regex, getter = _prepare(regex, flags)
    return (getter(elm) for elm in regex.finditer(_string))

    

#==============================================================================
#        Derived Functions
#==============================================================================
def re_find(regex, _string, flags=0):
    """Find regex inside _string."""
    return _first(re_iter(regex, _string, flags))

def re_all(regex, _string, flags=0):
    return list(re_iter(regex, _string, flags))

def re_test(regex, _string, flags=0):
    try:
        re_iter(regex, _string, flags).next()
        return True
    except StopIteration:
        return False

#==============================================================================
#        Convenience & Partial Functions
#==============================================================================
def make(re_func, regex, flags=0):
    """Partial-functions for regex-related functions.
    re_iter_finder('aa') == make(re_iter, 'aa')
    make(re_iter, 'aa')('aabbbaaa') == re_iter('aa', 'aabbbaaa')
    """
    return functools.partial(re_func, regex, flags=flags)
# def re_iter_finder(regex, flags=0):
#     #return functools.partial(re_iter, regex, flags=flags)
#     return make(re_iter, regex, flags)
# def re_finder(regex, flags=0):
#     """Factory; create functions to find regex inside a given string."""
#     #return functools.partial(re_find, regex, flags=flags)
#     return make(re_find, regex, flags)
# def re_all_finder(regex, flags=0):
#     #return functools.partial(re_all, regex, flags=flags)
#     return make(re_all, regex, flags)
# def re_tester(regex, flags=0):
#     #return functools.partial(re_test, regex, flags=flags)
#     return make(re_test, regex, flags)


#==============================================================================
#        Local Utility Functions
#==============================================================================
_re_type = type(re.compile(r''))

def _make_getter(regex):
    """Function factory. Returns a function which retreives regex groups
    for the input string, if present."""
    if regex.groups == 0:
        return operator.methodcaller('group')
    elif regex.groups == 1 and regex.groupindex == {}:
        return operator.methodcaller('group', 1)
    elif regex.groupindex == {}:
        return operator.methodcaller('groups')
    elif regex.groups == len(regex.groupindex):
        return operator.methodcaller('groupdict')
    else:
        return _identity

def _prepare(regex, flags=0):
    """For either input regex or standard-string, construct regex and
    a group-getter function."""
    if not isinstance(regex, _re_type):
        regex = re.compile(regex, flags)
    return regex, _make_getter(regex)


def _first(iterator):
    try:
        return iterator.next()
    except StopIteration:
        return None
    
def _identity(*args, **kwargs):
    """Identity function accounting for complicated possibilities"""
    if len(args) == 0 and len(kwargs) == 0:
        return None
    elif len(args) == 1 and len(kwargs) == 0:
        return args[0]
    elif len(args) > 1 and len(kwargs) == 0:
        return args
    elif len(args) == 0 and len(kwargs) != 0:
        return kwargs
    elif len(args) == 1 and len(kwargs) != 0:
        return (args[0], kwargs)
    elif len(args) > 1 and len(kwargs) != 0:
        return (args, kwargs)
    
