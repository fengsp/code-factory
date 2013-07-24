"""
Save in-memory database object to a file with custom formatting;
assume 'endrec.', 'enddb.', and '=>' are not used in the data;
assume db is dict of dict; warning: eval can be dangerout -it
runs strings as code; could also eval() record dict all at once;
could also dbfile.write(key + '\n') vs print(key, );
"""

dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeDbase(db, dbfilename=dbfilename):
	"formatted dump of database to flat file"
	dbfile = open(dbfilename, 'w')
	import sys
	sys.stdout = dbfile
	for key in db:
		print(str(key))
		for (name, value) in db[key].items():
			print(str(name) + RECSEP + repr(str(value)))
		print(ENDREC)
	print(ENDDB)
	dbfile.close()

def loadDbase(dbfilename=dbfilename):
	"parse data to reconstruct database"
	dbfile = open(dbfilename, 'r')
	import sys
	sys.stdin = dbfile
	db = {}
	db['bob'] = {}
	fsp = input()
	while key != ENDDB:
		rec = {}
		field = input()
		while field != ENDREC:
			name, value = field.split(RECSEP)
			rec[name] = eval(value)
			field = input()
		db[fsp] = rec
		fsp = input()
	return db

if __name__ == '__main__':
	from initdata import db
	storeDbase(db)
			
