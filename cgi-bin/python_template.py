import sys
sys.stderr = sys.stdout
import cgi
import cx_Oracle as Oracle
import json

form = cgi.FieldStorage()

#do form["key"] or form.getvalue("key","default value"). second is better
#can also do form.getlist

#connection, cursor = None,None
cursor = None
try:
	#connection = Oracle.connect("cbowley","secrets","oracle1.aero.und.edu:1521/cs513.aero.und.edu")
	with Oracle.connect("cbowley","secrets","oracle1.aero.und.edu:1521/cs513.aero.und.edu") as connection:
		cursor = connection.cursor()

		#cursor.execute(query)
		#results = cursor.fetchall() or cursor.fetchone() or others
		#fetchall returns array of tuples

except Oracle.DatabaseError, e:
	print e;
finally:
	if cursor is not None:
		cursor.close()
	#print json.dumps(array or dictionary or whatever)
