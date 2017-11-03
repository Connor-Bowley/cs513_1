import sys
import traceback
sys.stderr = sys.stdout
import cgi
import cx_Oracle as Oracle
import json
form = cgi.FieldStorage()
#do form["key"] or form.getvalue("key","default value"). second is better
#can also do form.getlist

connection, cursor = None,None
out = {"success":False}
try:
	connection = Oracle.connect("cbowley","secrets","oracle1.aero.und.edu:1521/cs513.aero.und.edu")

	cursor = connection.cursor()
	cid = form.getvalue("id","-1")
	games = form.getlist("asin")
	quantities = form.getlist("quantity")
	if cid == "-1" or len(games) == 0 or len(quantities) == 0 or len(quantities) != len(games):
		out["error"] = str(cid) + " " + str(games) + " " + str(quantities) 
		raise Exception()
	query = "BEGIN "
	for game, quantity in zip(games, quantities):
		query += "purchase_game("+cid+",'"+game+"',"+quantity+");"
	query += "END;"
		

	cursor.execute(query)
	connection.commit()
	out["success"] = True
except (Oracle.DatabaseError, Exception) as e:
	print "Exception was: ", traceback.format_exc();
finally:
	if cursor is not None:
		cursor.close()
	if connection is not None:
		connection.close()
	#print json.dumps(array or dictionary or whatever)
	print json.dumps(out)
