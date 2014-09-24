"""
Heavily inspired by func/strings.py
"""
from __future__ import absolute_import
import re
import operator
import functools

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
    """Return all matching groups."""
    return list(re_iter(regex, _string, flags))

def re_test(regex, _string, flags=0):
    """Predicate. Return True if _string matches regex."""
    try:
        re_iter(regex, _string, flags).next()
        return True
    except StopIteration:
        return False

#==============================================================================
#        Convenience & Partial Functions
#==============================================================================
def make(re_func, regex, flags=0):
    """Function factory. Constructs partial-functions for 
    regex-related functions.
    
    make(re_iter, 'aa')('aabbbaaa') == re_iter('aa', 'aabbbaaa')
    """
    return functools.partial(re_func, regex, flags=flags)


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
    
