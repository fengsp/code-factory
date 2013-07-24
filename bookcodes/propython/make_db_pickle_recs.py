import pickle
from initdata import *
for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
	recfile = open(key + '.pkl', 'wb')
	pickle.dump(record, recfile)
	recfile.close()

