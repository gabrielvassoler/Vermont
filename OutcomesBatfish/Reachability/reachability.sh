nxp=35

t=0
while [ $t -lt $nxp ]
do
    cd Exp$t/Config-Generator
    python3 BatFishConfigGenerator.py
    cd ..
    python3 reachability.py
    t=$((t+1))
    cd ..
done
