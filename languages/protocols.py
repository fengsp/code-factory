# -*- coding: utf-8 -*-
"""
Common Protocols
"""
class Protocol(object):
    """Protocol class
    Just to implements most of the Protocols
    """
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return self.value == 'fsp'
    __nonzero__ == __bool__

    def __add__(self, other):
        return Protocol(self.value + other.value)

    def __lshift__(self, positions):
        return self.value.__lshift__(positions)

    def __rshift__(self, pos):
        pass

    def __and__(self, value):
        pass

    def __or__(self, value):
        pass

    def __xor__(self):
        pass

    def __radd__(self, other):
        return Protocol(self.value + other)

    def __eq__(self, value):
        pass

    def __ne__(self, value):
        pass

    def __reversed__(self):
        pass

    def __getitem(self, key):
        pass

    def __setitem(self, key):
        pass

    def __delitem__(self, key):
        pass
