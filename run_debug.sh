nxp=1

cd Outcomes

cd Reachability

t=0
while [ $t -lt $nxp ]
do
    cp Exp$t/Vermon/path Executable/
    cp Exp$t/Vermon/network.json Executable/experiments/general/network.json
    cp Exp$t/Vermon/workload.json Executable/experiments/general/workload.json
    cd Executable
    sudo chmod 777 run.sh
    ./run.sh
    mkdir ../Exp$t/results/
    mkdir ../Exp$t/logs/
    cp results/* ../Exp$t/results/
    cp sender.json ../Exp$t/results/sender.json
    cp logs/* ../Exp$t/logs/
    #sudo make clean
    truncate -s 0 sender.txt
    rm results/*
    rm -rf resources/workloads/general/
    echo "0" > results/counter.txt
    cd ..
    t=$((t+1))
done

cd ..