The cgi stuff is in cgi-bin.
The create commands for SQL are in cgi-bin/sqlscripts/CreateTables.sql.

To use the cgi stuff it needs to be soft linked.

cd into root of this repo
ln -s cgi-bin ../../cgi-bin/513/1

This project uses a python virtual environment.

pip install virtualenv
cd to cgi-bin
virtualenv venv
pip install -r path/to/requirements.txt
