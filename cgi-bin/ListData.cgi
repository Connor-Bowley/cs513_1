#!/bin/bash

export ORACLE_HOME=/usr/lib/oracle/12.1/client64
export LD_LIBRARY_PATH=$ORACLE_HOME/lib
CLASSPATH=.:/usr/lib/oracle/12.1/client64
CLASSPATH=$CLASSPATH:/usr/lib/oracle/12.1/client64/lib/ojdbc7.jar
CLASSPATH=$CLASSPATH:/usr/lib/oracle/12.1/client64/lib/ottclasses.zip
export CLASSPATH

#activate python virtual env

echo "Content-Type: application/json"
echo ""
echo "["
/usr/bin/java -Djava.security.egd=file:/dev/./urandom DeveloperInfo
echo ","
source venv/bin/activate
python SearchGames.py
echo ","
python CustInfo.py
echo "]"
