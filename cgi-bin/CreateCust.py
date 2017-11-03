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
out = {"success":False}
try:
	#connection = Oracle.connect("cbowley","secrets","oracle1.aero.und.edu:1521/cs513.aero.und.edu")
	with Oracle.connect("cbowley","secrets","oracle1.aero.und.edu:1521/cs513.aero.und.edu") as connection:
		cursor = connection.cursor()
		param = {"name":form.getvalue("name","")}
		if(param["name"] != ""):
			check_query = "SELECT id FROM customers WHERE name = :name"
			cursor.execute(check_query,param);
			result = cursor.fetchone()
			cid = int(result[0]) if result else -1;
			if(cid != -1): #already exists
				out["Id"] = cid
				out["success"] = True
			else: # need to add
				insert_query = "INSERT INTO customers(name,account) VALUES (:name,purchased_game_table())"
				cursor.execute(insert_query,param);
				cursor.execute(check_query,param);
				result = cursor.fetchone()
				cid = int(result[0]) if result else -1
				if(cid != -1): #good
					out["Id"] = cid
					out["success"] = True
		#cursor.execute(query)
		#results = cursor.fetchall() or cursor.fetchone() or others
		#fetchall returns array of tuples

except Oracle.DatabaseError, e:
	print e;
finally:
	if cursor is not None:
		cursor.close()
	#print json.dumps(array or dictionary or whatever)
	print json.dumps(out)
