#!/usr/bin/env python

import urllib
import threading
import Queue
from optparse import OptionParser
import gevent
from gevent import monkey
monkey.patch_all()
import urllib2

dev_host = 'localhost'
dev_port = '80'
prefix = ''
channel_id_max = 80
NUM_WORKERS = 15
q = Queue.Queue(0)

class EzineReloadWorker(threading.Thread):
    """
    by fsp 20130227_11_54
    """
    def __init__(self, queue):
        self._queue = queue
        threading.Thread.__init__(self)
    
    def run(self):
        while True:
            try:
                channel_id = self._queue.get()
                if channel_id is not None:
                    self._reload(channel_id)
            finally:
                self._queue.task_done()
    
    def _reload(self, channel_id):
        reload_url = 'http://' + str(dev_host) + ':' + str(dev_port) + prefix + '/index.php' + '?r=channel/reload&id=' + str(channel_id)
        #print(reload_url)
        urllib.urlopen(reload_url)

if __name__ == '__main__':
    from optparse import OptionParser
    
    parser = OptionParser()
    parser.add_option("-n", "--host", dest="hostname", help="The hostname of development server")
    parser.add_option("-p", "--port", dest="portnum", help="The portnum of development server")
    parser.add_option("-a", "--prefix", dest="prefix", help="Some prefix of your hostname")
    (options, args) = parser.parse_args()

    if options.hostname is not None:
        dev_host = options.hostname
    if options.portnum is not None:
        dev_port = options.portnum
    if options.prefix is not None:
        prefix = options.prefix

    #Strip the '/' at the start and end of prefix
    prefix = prefix.strip('/')
    if prefix != '':
        prefix = '/' + prefix
    #Strip the '/' and 'http:' at the start of hostname
    if dev_host.startswith('http:'):
        dev_host = dev_host[5:]
    dev_host = dev_host.strip('/')


    def reload(channel_id):
        reload_url = 'http://' + str(dev_host) + ':' + str(dev_port) + prefix + '/index.php' +'?r=channel/reload&id=' + str(channel_id)
        urllib2.urlopen(reload_url)
    
    jobs = [gevent.spawn(reload, channel_id) for channel_id in range(channel_id_max)]
    gevent.joinall(jobs)
