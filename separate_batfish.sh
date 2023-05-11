nxp=35

t=0
mkdir OutcomesBatfish/Reachability
mkdir OutcomesBatfish/Waypoint
mkdir OutcomesBatfish/Loop

cp reachability.sh OutcomesBatfish/Reachability/
cp waypoint.sh OutcomesBatfish/Waypoint/
cp loop.sh OutcomesBatfish/Loop/

while [ $t -lt $nxp ]
do
    cp -r Outcomes/Reachability/Exp$t/Batfish/. OutcomesBatfish/Reachability/Exp$t/
    #cp -r Outcomes/Waypoint/Exp$t/Batfish/. OutcomesBatfish/Waypoint/Exp$t/
    #cp -r Outcomes/Loop/Exp$t/Batfish/. OutcomesBatfish/Loop/Exp$t/

    t=$((t+1))
done
