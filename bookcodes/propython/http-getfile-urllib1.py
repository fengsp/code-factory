import sys
from urllib.request import urlopen
showlines = 6
try:
	servername, filename = sys.argv[1:]
except:
	servername, filename = 'www.baidu.com', ''

remoteaddr = 'http://%s%s' % (servername, filename)
print(remoteaddr)
remotefile = urlopen(remoteaddr)
remotedata = remotefile.readlines()
remotefile.close()
for line in remotedata[:showlines]: print(line)
