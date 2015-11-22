import MySQLdb

def connection():
	conn = MySQLdb.connect(host = "localhost",
						   user = "root",
						   passwd = "emission",
						   db = "rma" )
	c = conn.cursor()

	return c, conn
