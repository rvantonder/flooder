#!/bin/bash

NODES=$# # all cmd-line args

NODES=$(($NODES)) # the rest are botnet nodes

for i in `seq $NODES`
do
  ssh -t rai@$1 "ps aux | awk '/flooder/ {print \$2}' | xargs kill -9"
  shift
done
