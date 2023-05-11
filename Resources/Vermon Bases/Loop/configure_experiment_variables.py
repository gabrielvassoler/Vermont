import json

path = ''
with open('path', 'r') as f:
    path = json.load(f)

src = path['src']
dst = path['dst']

srcip = '10.0.'+str(src) + '.' +str(src)
dstip = '10.0.'+str(dst) + '.' +str(dst)

flowid = ''

file = ''
with open('s'+str(src)+'-runtime.json', 'r') as f:
    file = json.load(f)

file = file['table_entries']

for x in file:
    if x['action_name'] != "ingress.set_flow_ID":
        continue
    
    if x['match']['hdrs.ipv4.dst_addr'] != dstip or x['match']['hdrs.ipv4.src_addr'] != srcip:
        continue

    flowid = x['action_params']['flow_ID']
    break
a = ''
if 'waypoint' in path.keys():
    a = {"waypoint":[{"startLocation": int(src), "endLocation": int(dst), "flowID": int(flowid), "expectedWaypoints": ["s"+str(path['waypoint'])]}]}
else:
    a = {"reachability":[{"startLocation": int(src), "endLocation": int(dst), "flowID": int(flowid)}]}

with open('vermon.json', 'w') as f:
    json.dump(a, f)

f = open('path_ID_decoder.txt', 'r')
g = f.read()
remov = ["'"]
for character in remov:
    g = g.replace(character, "\"")
f.close()
f = open('path_ID_decoder.txt', 'w')
f.write(g)

