import sys
sys.stderr = sys.stdout

import cgi
import cx_Oracle as Oracle
import json

form = cgi.FieldStorage()

#do form["key"] or form.getvalue("key","default value"). second is better
#can also do form.getlist

if(len(sys.argv) > 1):
	cid = sys.argv[1]
else:
	cid = form.getvalue("id","-1")

connection, cursor = None,None

output = []
try:
	connection = Oracle.connect("cbowley","secrets","oracle1.aero.und.edu:1521/cs513.aero.und.edu")

	cursor = connection.cursor()
	
	query = "SELECT c.id, c.name FROM customers c"
	if int(cid) > 0:
		query += " WHERE c.id = "+cid
	cursor.execute(query)
	for row in cursor:
		output.append({"Id":row[0],"Name":row[1]});

except Oracle.DatabaseError, e:
	print e;
finally:
	if cursor is not None:
		cursor.close()
	if connection is not None:
		connection.close()
	print json.dumps(output)
