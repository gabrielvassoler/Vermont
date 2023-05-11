import json

path = ''
with open('path', 'r') as f:
    path = json.load(f)

src = path['src']
dst = path['dst']
port = path['port']

path['waypoint'] = '3'

srcip = '10.0.'+str(src) + '.' +str(src)
dstip = '10.0.'+str(dst) + '.' +str(dst)

flowid = ''

file = ''
with open('s'+str(dst)+'-runtime.json', 'r') as f:
    file = json.load(f)

file = file['table_entries']

for x in file:
    if x['action_name'] != "ingress.set_flow_ID":
        continue

    if x['match']['hdrs.ipv4.dst_addr'] != dstip or x['match']['hdrs.ipv4.src_addr'] != srcip or x['match']['hdrs.ipv4.identification'] != port:
        continue

    flowid = x['action_params']['flow_ID']
    break
vermon_json = {}

vermon_json["waypoint"] = [{"startLocation": int(src), "endLocation": int(dst), "flowID": int(flowid), "expectedWaypoints": ["s"+str(path['waypoint'])], "unexpectedWaypoints": []}]
vermon_json["reachability"] = [{"startLocation": int(src), "endLocation": int(dst), "flowID": int(flowid)}]

app = 0
for flow in path['cflows']:
    src = int(flow[0])
    dst = int(flow[1])
    port = flow[2]

    srcip = '10.0.'+str(src) + '.' +str(src)
    dstip = '10.0.'+str(dst) + '.' +str(dst)

    flowid = ''

    file = ''
    with open('s'+str(dst)+'-runtime.json', 'r') as f:
        file = json.load(f)

    file = file['table_entries']

    for x in file:
        if x['action_name'] != "ingress.set_flow_ID":
            continue

        if x['match']['hdrs.ipv4.dst_addr'] != dstip or x['match']['hdrs.ipv4.src_addr'] != srcip or x['match']['hdrs.ipv4.identification'] != port:
            continue

        flowid = x['action_params']['flow_ID']
        break

    if (app % 2 == 0):
        vermon_json["waypoint"].append({"startLocation": int(src), "endLocation": int(dst), "flowID": int(flowid), "expectedWaypoints": ["s"+str(path['waypoint'])], "unexpectedWaypoints": []})
    else:
        vermon_json["reachability"].append({"startLocation": int(src), "endLocation": int(dst), "flowID": int(flowid)})

    app += 1

with open('vermon.json', 'w') as f:
    json.dump(vermon_json, f)

f = open('path_ID_decoder.txt', 'r')
g = f.read()
remov = ["'"]
for character in remov:
    g = g.replace(character, "\"")
f.close()
f = open('path_ID_decoder.txt', 'w')
f.write(g)
