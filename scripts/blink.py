# -*- coding: utf-8 -*-
from blinker import signal


def subscriber(sender):
    print("Got a signal sent by %r" % sender)


test = signal('test')
test.connect(subscriber)
send_data = signal('send-data')
@send_data.connect
def receive_data(sender, **kwargs):
    print("Caught signal from %r, data %r" % (sender, kwargs))
    return 'received!'


class Processor(object):
    def __init__(self, name):
        self.name = name

    def go(self):
        test = signal('test')
        test.send(self)
        print("Processing...")
        complete = signal('complete')
        complete.send(self)
        send_data = signal('send-data')
        result = send_data.send(self, aiyou='aiyou')
        print("Getting result" + str(result))

    def __repr__(self):
        return '<Processor %s>' % self.name


processor_fsp = Processor('fsp')
processor_fsp.go()
