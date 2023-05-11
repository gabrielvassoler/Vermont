# Import packages and load questions
filename = '../../startup.py'
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)
bf = Session(host="localhost")

import time
import json

CHANGE1_NAME = "change"
CHANGE1_PATH = "Config-Generator/Outcomes/"

PATH = ''

with open('path', 'r') as f:
    PATH = json.load(f)

startPoint = PATH['src']
endPoint = PATH['dst']

wp = '3'

bf.init_snapshot(CHANGE1_PATH, name=CHANGE1_NAME, overwrite=True)

start = time.time()
answer = bf.q.reachability(
    pathConstraints=PathConstraints(
        startLocation="h_"+str(startPoint)+"_1"),
    headers=HeaderConstraints(dstIps="h_"+str(endPoint)+"_1"),
    actions="SUCCESS,FAILURE"
).answer(snapshot=CHANGE1_NAME)

app = 0

for x in PATH['cflows']:
    startPoint = x[0]
    endPoint = x[0]


    if(app % 2 == 0):
        answer = bf.q.reachability(
        pathConstraints=PathConstraints(
            startLocation="h_"+str(startPoint)+"_1"),
        headers=HeaderConstraints(dstIps="h_"+str(endPoint)+"_1"),
        actions="SUCCESS,FAILURE"
        ).answer(snapshot=CHANGE1_NAME)
    else:
        answer = bf.q.reachability(
            pathConstraints=PathConstraints(
                startLocation="h_"+str(startPoint)+"_1",
                transitLocations ="sw"+str(wp)),
            headers=HeaderConstraints(dstIps="h_"+str(endPoint)+"_1"),
            actions="SUCCESS,FAILURE"
        ).answer(snapshot=CHANGE1_NAME)

    app += 1

end = time.time()
reachability_time = end - start

with open('result', 'w') as f:
    json.dump(reachability_time, f)
