"""
Used as one client
for test use
by fsp 20130502_16_43
"""
import urllib2
from optparse import OptionParser


requestUrl = 'http://localhost'
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-l", "--url", dest="link", help="The url you want to access remember to use quotes")
    (options, args) = parser.parse_args()
    if options.link is not None:
        requestUrl = options.link


    #req = urllib2.Request(requestUrl)
    #req.add_header('X-nHorizon-Component-Versions', 'z:1;fsptest;') 
    #r = urllib2.urlopen(req)
    #print r.read()
    opener = urllib2.build_opener()
    opener.addheaders = [('X-nHorizon-Component-Versions', 'z:1; fsptest;')]
    r = opener.open(requestUrl)
    print r.read()

