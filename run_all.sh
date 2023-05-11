nxp=35

rm -rf Outcomes

python3 main.py topology.json

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
    sudo make clean
    truncate -s 0 sender.txt
    rm results/*
    rm -rf resources/workloads/general/
    echo "0" > results/counter.txt
    cd ..
    t=$((t+1))
done

cd ..

cd ..

t=0
mkdir OutcomesBatfish
mkdir OutcomesBatfish/Reachability

cp reachability.sh OutcomesBatfish/Reachability/

cp startup.py OutcomesBatfish/

while [ $t -lt $nxp ]
do
    cp -r Outcomes/Reachability/Exp$t/Batfish/. OutcomesBatfish/Reachability/Exp$t/

    t=$((t+1))
done

mkdir Outcomes-0

cp -r Outcomes/* Outcomes-0/

rm -rf Outcomes

python3 main-10.py topology.json

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
    sudo make clean
    truncate -s 0 sender.txt
    rm results/*
    rm -rf resources/workloads/general/
    echo "0" > results/counter.txt
    cd ..
    t=$((t+1))
done

cd ..

cd ..

t=0
mkdir OutcomesBatfish-10
mkdir OutcomesBatfish-10/Reachability

cp reachability.sh OutcomesBatfish-10/Reachability/

cp startup.py OutcomesBatfish-10/

while [ $t -lt $nxp ]
do
    cp -r Outcomes/Reachability/Exp$t/Batfish/. OutcomesBatfish-10/Reachability/Exp$t/

    t=$((t+1))
done

mkdir Outcomes-10

cp -r Outcomes/* Outcomes-10/

rm -rf Outcomes

python3 main-100.py topology.json

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
    sudo make clean
    truncate -s 0 sender.txt
    rm results/*
    rm -rf resources/workloads/general/
    echo "0" > results/counter.txt
    cd ..
    t=$((t+1))
done

cd ..

cd ..

t=0
mkdir OutcomesBatfish-100
mkdir OutcomesBatfish-100/Reachability

cp reachability.sh OutcomesBatfish-100/Reachability/

cp startup.py OutcomesBatfish-100/

while [ $t -lt $nxp ]
do
    cp -r Outcomes/Reachability/Exp$t/Batfish/. OutcomesBatfish-100/Reachability/Exp$t/

    t=$((t+1))
done

mkdir Outcomes-100

cp -r Outcomes/* Outcomes-100/

rm -rf Outcomes

python3 main-1000.py topology.json

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
    sudo make clean
    truncate -s 0 sender.txt
    rm results/*
    rm -rf resources/workloads/general/
    echo "0" > results/counter.txt
    cd ..
    t=$((t+1))
done

cd ..

cd ..

t=0
mkdir OutcomesBatfish-1000
mkdir OutcomesBatfish-1000/Reachability

cp reachability.sh OutcomesBatfish-1000/Reachability/

cp startup.py OutcomesBatfish-1000/

while [ $t -lt $nxp ]
do
    cp -r Outcomes/Reachability/Exp$t/Batfish/. OutcomesBatfish-1000/Reachability/Exp$t/

    t=$((t+1))
done

mkdir Outcomes-1000

cp -r Outcomes/* Outcomes-1000/

rm -rf Outcomes