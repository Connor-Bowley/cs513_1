import sys
sys.stderr = sys.stdout
import cgi
import cx_Oracle as Oracle
import json

form = cgi.FieldStorage()

#do form["key"] or form.getvalue("key","default value"). second is better
#can also do form.getlist
if(len(sys.argv) > 1):
	names = sys.argv[1].strip().split()
else:
	names = form.getvalue("search","").strip().split()
names = [name.strip() for name in names]
out = []
connection, cursor = None,None
try:
	connection = Oracle.connect("cbowley","secrets","oracle1.aero.und.edu:1521/cs513.aero.und.edu")

	cursor = connection.cursor()

	if(len(names) == 0):
		query = "SELECT g.asin, g.title, g.price FROM games g ORDER BY g.title"
	else:
		query = "SELECT g.asin, g.title, g.price, count(*) AS total FROM games g, TABLE(g.developers) gd, developers d WHERE gd.id = d.id AND (REGEXP_LIKE(d.name,'"+names[0]+"','i')"

		for name in names[1:]:
			query += " OR REGEXP_LIKE(d.name,'"+name+"','i')"
		query += ") GROUP BY g.asin, g.title, g.price ORDER BY total DESC"
	
	cursor.execute(query)
	#fetchall returns array of tuples
	for row in cursor:
		out.append(dict([("Asin",str(row[0])),("Title",str(row[1])),("Price",str(row[2]))]))
except Oracle.DatabaseError, e:
	print e;
finally:
	if cursor is not None:
		cursor.close()
	if connection is not None:
		connection.close()
	print json.dumps(out)
