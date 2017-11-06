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
out = {"success":False,"message":"Unable to purchase games"}
try:
	connection = Oracle.connect("cbowley","secrets","oracle1.aero.und.edu:1521/cs513.aero.und.edu")

	cursor = connection.cursor()
	cid = form.getvalue("id","-1")
	games = form.getlist("asin")
	quantities = form.getlist("quantity")
	if cid != "" and int(cid) <= 0:
		out["message"] = "Admin not permitted to purchase games"
	elif len(games) != len(quantities):
		out["message"] = "Inconsistent lengths for games and quantities. Contact sys admin."
	elif len(games) == 0:
		out["message"] = "No games were selected"
	else:
		query = "BEGIN "
		hits = 0
		for game, quantity in zip(games, quantities):
			if int(quantity) != 0:
				hits += 1
				query += "purchase_game("+cid+",'"+game+"',"+quantity+");"
		query += "END;"
			
		if hits > 0:
			cursor.execute(query)
			connection.commit()
			out["success"] = True
			out["message"] = "Successfully purchased games"
		else:
			out["message"] = "All game quantities were 0"
except (Oracle.DatabaseError, Exception) as e:
	out["message"] = "Exception was: ", traceback.format_exc();
finally:
	if cursor is not None:
		cursor.close()
	if connection is not None:
		connection.close()
	#print json.dumps(array or dictionary or whatever)
	print json.dumps(out)
