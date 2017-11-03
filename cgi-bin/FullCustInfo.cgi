#!/bin/bash

export ORACLE_HOME=/usr/lib/oracle/12.1/client64
export LD_LIBRARY_PATH=$ORACLE_HOME/lib

#activate python virtual env
source venv/bin/activate

#echo "Content-Type: application/json"
echo "Content-Type: text/plain"
echo ""

python FullCustInfo.py 
