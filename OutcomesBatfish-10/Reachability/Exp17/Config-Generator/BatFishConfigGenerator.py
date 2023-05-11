import json


def main():

    top = open("Topology/topology.json", "r")

    topology = json.load(top)

    hasLoop = open('../path', 'r')

    data = json.load(hasLoop)

    path = data['path']
    loop = data['loop']

    n_nodes = topology['network']['n_nodes']
    hosts_per_node = 1 #constant
    edges = topology['network']['edges']

    node_config = {}
    host_config = {}
    for a in range(0, n_nodes):
        node_config[a+1] = {"interfaces" : []}
        for b in (0, hosts_per_node):
            host_config[a] = {"ip" : "", "gateway": "", "h_name": ""}
    

    node_config, finder = node_to_node_interface_generator(n_nodes, edges, node_config)
    node_config, host_config = node_to_host_interface_generator(n_nodes, edges, hosts_per_node, node_config, host_config)
    node_gen(n_nodes, node_config, path, loop, finder)
    host_gen(host_config)
    #print(node_config)
    #print(host_config)

def node_gen(n_nodes, node_config, path, loop, finder):
    f = open("Bases/first.txt", "r")
    f1 = f.read()
    f = open("Bases/second.txt", "r")
    f2 = f.read()
    f = open("Bases/third.txt", "r")
    f3 = f.read()
    f = open("Bases/fourth.txt", "r")
    f4 = f.read()
    f = open("Bases/fifth.txt", "r")
    f5 = f.read()

    for a in range(1, n_nodes+1):
        dt = ""
        out = open("Outcomes/configs/sw"+str(a)+".cfg", "w")
        dt += f1

        dt += "\nhostname sw" + str(a) +"\n"

        dt += f2
        dt += "\n"
        
        dt += "logging host 2."+str(a)+".2.2 \n"

        dt += f3
        dt += "\n"

        dt += "ip address 2."+str(a)+".2.1 255.255.255.255 \n!\n"

        dt += f4
        dt += "\n"

        c = 0
        for b in range(0, len(node_config[a]["interfaces"])):
            dt += "interface GigabitEthernet"+str(c)+"/0\n" + " "+node_config[a]["interfaces"][b]+" \n" + " media-type gbic\n" + " speed 1000\n" + " duplex full\n" + " negotiation auto\n" + " ip ospf cost 1\n" + "!\n"
            c += 1
        
        if(path != []):
            for l in range(0, len(path)-1):
                if(path[l] == a):
                    dt+= 'ip route '+ "2."+str((10*path[-1])+1)+".10.2 255.255.255.0 " + finder[str(path[l])+'-'+str(path[l+1])]
                    dt+= '\n'
            if(loop == 1):
                if(a == len(path)-1):
                    dt+= 'ip route '+ "2."+str((10*path[-1])+1)+".10.2 255.255.255.0 " + finder[str(path[-1])+'-'+str(path[0])]
                    dt+= '\n'
        dt += f5
        dt += "\n"

        out.write(dt)
        out.close()

def host_gen(host_config):
    f = open("Bases/host.json", "r")
    base = json.load(f)
    for a in range(0, len(host_config)):
        hname = host_config[a]["h_name"]
        pre = host_config[a]["ip"]
        gt = host_config[a]["gateway"]
        out = open("Outcomes/hosts/"+hname+".json", "w")
        base["hostname"] = hname
        base["hostInterfaces"]["eth0"]["prefix"] = pre 
        base["hostInterfaces"]["eth0"]["gateway"] = gt 
        json.dump(base, out, indent=4)
        out.close()


def node_to_host_interface_generator(n_nodes, edges, hosts_per_node, node_config, host_config):
    host = 0
    for a in range(0, n_nodes):
        node = a + 1
        subnet = 10 * node
        counter = 1
        for b in range(0, hosts_per_node):
            host_config[host+b]["h_name"] = "h_"+str(node)+"_"+str(b+1)
            node_config[node]["interfaces"].append("ip address 2."+str(subnet+counter)+".10.1 255.255.255.0")
            host_config[host+b]["ip"] = "2."+str(subnet+counter)+".10.2/24"
            host_config[host+b]["gateway"] = "2."+str(subnet+counter)+".10.1"
            host += 1
            counter += 1
    
    return node_config, host_config

def node_to_node_interface_generator(n_nodes, edges, node_config):
    counter = 0
    finder = {}
    for edge in edges:
        subnet = 10 + counter
        counter += 1
        node_config[edge["start"]]["interfaces"].append("ip address 2.10."+str(subnet)+".1 255.255.255.0")
        node_config[edge["end"]]["interfaces"].append("ip address 2.10."+str(subnet)+".2 255.255.255.0")
        finder[str(edge["start"])+'-'+str(edge["end"])] = "2.10."+str(subnet)+".2"
        finder[str(edge["end"])+'-'+str(edge["start"])] = "2.10."+str(subnet)+".1"
    return node_config, finder

main()