import os, sys, ftplib
from getpass import getpass
from mimetypes import guess_type

nonpassive = False
remotesite = 'home.rmi.net'
remotedir = '.'
remoteuser = 'lutz'
remotepass = getpass('Password for %s on %s: ' % (remoteuser, remotesite))
localdir = (len(sys.argv) > 1 and sys.argv[1]) or '.'
cleanall = input('Clean local directory first?')[:1] in ['y', 'Y']

print('connectiong...')
connection = ftplib.FTP(remotesite)
connection.login(remoteuser, remotepass)
connection.cwd(remotedir)
if nonpassive:
	connection.set_pasv(False)

if cleanall:
	for localname in os.listdir(localdir):
		try:
			print('deleting local', localname)
			os.remove(os.path.join(localdir, localname))
		except:
			print('cannot delete local', localname)

count = 0
remotefiles = connection.nlst()

for remotename in remotefiles:
	if remotename in ('.', '..'): continue

