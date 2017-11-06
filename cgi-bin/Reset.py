import sys
sys.stderr = sys.stdout
import cgi
import json
from subprocess import Popen, PIPE

out = {"success":False}
try:
	sqlplus = Popen(['sqlplus','-S','cbowley/secrets@//oracle1.aero.und.edu:1521/cs513.aero.und.edu'],stdin=PIPE, stdout=PIPE, stderr=PIPE)
	sqlplus.stdin.write('@sqlscripts/CreateTables.sql');
	response = sqlplus.communicate()
	if "error" not in ''.join(response).lower():
		out['success'] = True
	
	#print ''.join(response)

except Exception, e:
	out["message"] = str(e);
finally:
	print json.dumps(out);
