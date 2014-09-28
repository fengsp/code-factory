# -*- coding: utf-8 -*-
"""
    Coroutine
    ~~~~~~~~~

    Coroutines via Enhanced Generators.

    http://www.python.org/dev/peps/pep-0342/
"""
import collections
import types


class Trampoline(object):
    """Manage communications between coroutines"""

    running = False

    def __init__(self):
        self.queue = collections.deque()
        
    def add(self, coroutine):
        """Request that a coroutine be executed"""
        self.schedule(coroutine)

    def run(self):
        result = None
        self.running = True
        try:
            while self.running and self.queue:
                func = self.queue.popleft()
                result = func()
            return result
        finally:
            self.running = False

    def stop(self):
        self.running = False

    def schedule(self, coroutine, stack=(), val=None, *exc):
        def resume():
            value = val
            try:
                if exc:
                    value = coroutine.throw(value, *exc)
                else:
                    value = coroutine.send(value)
            except:
                if stack:
                    # send the error back to the 'caller'
                    self.schedule(
                        stack[0], stack[1], *sys.exc_info()
                    )
                else:
                    # Nothing to handle it
                    raise
            
            if isinstance(value, types.GeneratorType):
                # Yielded to a specific coroutine
                self.schedule(value, (coroutine, stack))
            elif stack:
                self.schedule(stack[0], stack[1], value)
            else:
                return value

        self.queue.append(resume)


if __name__ == "__main__":
    def gen1():
        yield 'result'

    def gen2():
        data = yield gen1()
        yield data

    t = Trampoline()
    couroutine = gen2()
    t.add(couroutine)
    print t.run()
