#!/bin/bash

nxp=2

cd Outcomes

cd Loop

t=0
while [ $t -lt $nxp ]
do
    cd Exp$t
    cd Vermon
    cp path ../../Executable/
    cp network.json ../../Executable/experiments/general/
    cp workload.json ../../Executable/experiments/general/
    sudo chmod 777 run.sh
    ./run.sh
    cd ..
    cd ..
    t=$((t+1))
done

cd ..