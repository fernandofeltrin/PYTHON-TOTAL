import sqlite3

conexao = sqlite3.connect('base.db')

///

import sqlite3

conexao = sqlite3.connect(database = 'base.db',
                          timeout = 5,
                          detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
                          isolation_level = 'DEFERRED')
