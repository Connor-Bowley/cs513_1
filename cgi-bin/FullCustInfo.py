import sys
sys.stderr = sys.stdout

import cgi
import cx_Oracle as Oracle
import json
import os
import subprocess

dump = True
form = cgi.FieldStorage()

#do form["key"] or form.getvalue("key","default value"). second is better
#can also do form.getlist

connection, cursor = None,None

if len(sys.argv) > 1:
	cust_id = sys.argv[1]
else:
	cust_id = str(form.getvalue("cid",-1))
if cust_id == -1:
	sys.exit()
output = dict([('Id',cust_id),('Account',[])])
try:
	connection = Oracle.connect("cbowley","secrets","oracle1.aero.und.edu:1521/cs513.aero.und.edu")

	cursor = connection.cursor()
	
	query = "SELECT c.name, a.asin, g.title, a.quantity, a.cost FROM customers c, games g, TABLE(c.account) a WHERE c.id = " + cust_id + " AND a.asin = g.asin"
	cursor.execute(query)
	#results = cursor.fetchall() or cursor.fetchone() or others
	first = True
	for row in cursor:
		if first:
			first = False 
			output['Name'] = row[0]
		output['Account'].append(dict([('Asin',row[1]),('Title',row[2]),('Quantity',row[3]),('Cost',row[4])]));
	if first: #this means the person potentially had no games
		#os.system("python CustInfo.py "+cust_id)
		print subprocess.check_output("python CustInfo.py "+cust_id, shell=True)[1:-2]
		dump = False
	#fetchall returns array of tuples

except Oracle.DatabaseError, e:
	print e;
finally:
	if cursor is not None:
		cursor.close()
	if connection is not None:
		connection.close()
	#print json.dumps(array or dictionary or whatever)
	if dump:
		print json.dumps(output)
