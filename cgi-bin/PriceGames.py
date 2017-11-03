import sys
sys.stderr = sys.stdout
import cgi
import cx_Oracle as Oracle
import json

form = cgi.FieldStorage()
prices = form.getlist("price");
asins = form.getlist("asin");
	

#do form["key"] or form.getvalue("key","default value"). second is better
#can also do form.getlist

#connection, cursor = None,None
cursor = None
ret = {"success":False,"message":"Failed to attempt update"}
try:
	if len(prices) != 0 and len(asins) != 0 and len(asins) == len(prices):
		param = [{"price":price, "asin":asin} for price, asin in zip(prices,asins)];
		with Oracle.connect("cbowley","secrets","oracle1.aero.und.edu:1521/cs513.aero.und.edu") as connection:
			cursor = connection.cursor()
			query = "UPDATE games SET price = :price WHERE asin = :asin"
			cursor.prepare(query)
			cursor.executemany(None,param)
			ret["success"] = True
			ret["message"] = "Successfully updated prices"
	elif len(prices) == 0 or len(asins) == 0:
		ret["message"] = "No new prices to update"
except Oracle.DatabaseError, e:
	#print e;
	ret["message"] = "Failed to update prices: "+str(e)
finally:
	if cursor is not None:
		cursor.close()
	#print json.dumps(array or dictionary or whatever)
	print json.dumps(ret)
