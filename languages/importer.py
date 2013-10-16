# -*- coding: utf-8 -*-
class Importer(object):
    """This importer redirects imports from one module to other locations"""

    def __init__(self, prefix='fsp'):
        self.prefix = prefix

    def install(self):
        sys.meta_path[:] = [x for x in sys.meta_path if self != x] + [self]

    def __eq__(self, other):
        return self.__class__.__module__ == other.__class__.__module__ and \
               self.__class__.__name__ == other.__class__.__name__

    def __ne__(self, other):
        return not self.__eq__(self, other)

    def find_module(self, fullname, path=None):
        if fullname.startswith(self.prefix):
            return self
        else:
            return None

    def load_module(self, fullname):
        if fullname in sys.modules:
            return sys.modules[fullname]
        # put your logic here
        realname = fullname + '.fsp'
        try:
            __import__(realname)
        module = sys.modules[fullname] = sys.modules[realname]
        return module
