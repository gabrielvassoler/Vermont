from pkgutil import iter_importers
import networkx as nx
from networkx.readwrite import json_graph
import json
import sys
import random
import os, shutil

EXP_NUM = 35

CONCURRENT_FLOWS = 100


imported_network = ''

def genBatFishReach(r, g):
    nodes = len(g.nodes())
    hosts = 1
    edges = []
    for u,v in g.edges():
        e = {'start': int(u[1:]), 'end':int(v[1:])}
        edges.append(e)
    top = {"network": {"n_nodes": nodes, "n_hosts_per_node": hosts, "edges": edges}}

    for a in range(0, len(r)):
        c = os.getcwd()
        source_dir = c + "/Resources/Batfish Bases"
        destination_dir = c + "/Outcomes/Reachability/Exp"+str(a)+'/Batfish'
        shutil.copytree(source_dir, destination_dir)
        fil = open(c + "/Outcomes/Reachability/Exp"+str(a)+'/Batfish/Config-Generator/Topology/topology.json', 'w+')
        json.dump(top, fil)

        cflows = []
        for x in range(0, CONCURRENT_FLOWS):
            pair = getPairOfNodes(g)
            pair[0] = pair[0][1:]
            pair[1] = pair[1][1:]
            cflows.append(pair)

        p = r[a]['path']
        p1 = []
        for x in p:
            p1.append(int(x[1:]))
        path = {'port':1234,'src': r[a]['source'][1:], 'dst': r[a]['target'][1:], 'path': p1, 'loop': 0, 'cflows':cflows}
        with open("./Outcomes/Reachability/Exp"+str(a)+'/Batfish/path', 'w') as f:
            json.dump(path, f)

def genVermonReach(r, g):
    nodes = len(g.nodes())
    hosts = 1
    edg = []
    for u,v in g.edges():
        x = ['s'+str(u[1:]), 's'+str(v[1:])]
        edg.append(x)

    for a in range(0, len(r)):
        # c = os.getcwd()
        # source_dir = c + "/Resources/Vermon Bases/Reachability"
        # destination_dir = c + "/Outcomes/Reachability/Exp"+str(a)+'/Vermon'
        # shutil.copytree(source_dir, destination_dir)

        network = ''
        with open('./Resources/Vermon Bases/Reachability/experiments/general/network.json', 'r') as f:
            network = json.load(f)

        network['nodes'] = nodes
        network['hosts_per_node'] = hosts
        network['node_links'] = edg

        os.makedirs("./Outcomes/Reachability/Exp"+str(a)+"/Vermon/")
        with open("./Outcomes/Reachability/Exp"+str(a)+'/Vermon/network.json', 'w') as f:
            json.dump(network, f)

        workload = ''
        with open('./Resources/Vermon Bases/Reachability/experiments/general/workload.json', 'r') as f:
            workload = json.load(f)
        #
        # workload['tcpreplay'][0]['sender'] = 'h' + r[a]['source'][1:]
        # workload['tcpreplay'][0]['receiver'] = 'h' + r[a]['target'][1:]
        # workload['tcpreplay'][0]['receiver_opt'] = '10.0.'+str(r[a]['target'][1:]) + '.' +str(r[a]['target'][1:]) + ' 1234'
        #
        with open("./Outcomes/Reachability/Exp"+str(a)+'/Vermon/workload.json', 'w') as f:
            json.dump(workload, f)

        cflows = []
        c = 1
        for x in range(0, CONCURRENT_FLOWS):
            pair = getPairOfNodes(g)
            pair[0] = pair[0][1:]
            pair[1] = pair[1][1:]
            pair.append(1234+c)
            c += 1
            cflows.append(pair)

        p = r[a]['path']
        p1 = []
        for x in p:
            p1.append(int(x[1:]))
        path = {'port':1234,'src': r[a]['source'][1:], 'dst': r[a]['target'][1:], 'path': p1, 'loop': 0, 'cflows': cflows}
        with open("./Outcomes/Reachability/Exp"+str(a)+'/Vermon/path', 'w') as f:
            json.dump(path, f)

def genVermonReachIncorrect(r, g):
    nodes = len(g.nodes())
    hosts = 1
    edg = []
    for u,v in g.edges():
        x = ['s'+str(u[1:]), 's'+str(v[1:])]
        edg.append(x)

    for a in range(0, len(r)):
        # c = os.getcwd()
        # source_dir = c + "/Resources/Vermon Bases/Reachability"
        # destination_dir = c + "/Outcomes/Reachability/Exp"+str(a)+'/Vermon'
        # shutil.copytree(source_dir, destination_dir)

        network = ''
        with open('./Resources/Vermon Bases/Reachability/experiments/general/network.json', 'r') as f:
            network = json.load(f)

        network['nodes'] = nodes
        network['hosts_per_node'] = hosts
        network['node_links'] = edg

        os.makedirs("./Outcomes/ReachabilityIncorrect/Exp"+str(a)+"/Vermon/")
        with open("./Outcomes/ReachabilityIncorrect/Exp"+str(a)+'/Vermon/network.json', 'w') as f:
            json.dump(network, f)

        workload = ''
        with open('./Resources/Vermon Bases/Reachability/experiments/general/workload.json', 'r') as f:
            workload = json.load(f)
        #
        # workload['tcpreplay'][0]['sender'] = 'h' + r[a]['source'][1:]
        # workload['tcpreplay'][0]['receiver'] = 'h' + r[a]['target'][1:]
        # workload['tcpreplay'][0]['receiver_opt'] = '10.0.'+str(r[a]['target'][1:]) + '.' +str(r[a]['target'][1:]) + ' 1234'
        #
        # with open("./Outcomes/ReachabilityIncorrect/Exp"+str(a)+'/Vermon/workload.json', 'w') as f:
        #     json.dump(workload, f)

        cflows = []
        c = 1
        for x in range(0, CONCURRENT_FLOWS):
            pair = getPairOfNodes(g)
            pair[0] = pair[0][1:]
            pair[1] = pair[1][1:]
            pair.append(1234+c)
            c += 1
            cflows.append(pair)

        p = r[a]['path']
        p1 = []
        for x in p:
            p1.append(int(x[1:]))
        path = {'port':1234,'src': r[a]['source'][1:], 'dst': r[a]['target'][1:], 'path': p1, 'loop': 0, 'cflows': cflows}
        with open("./Outcomes/ReachabilityIncorrect/Exp"+str(a)+'/Vermon/path', 'w') as f:
            json.dump(path, f)

def genBatFishWp(r, g):
    nodes = len(g.nodes())
    hosts = 1
    edges = []
    for u,v in g.edges():
        e = {'start': int(u[1:]), 'end':int(v[1:])}
        edges.append(e)
    top = {"network": {"n_nodes": nodes, "n_hosts_per_node": hosts, "edges": edges}}

    for a in range(0, len(r)):
        c = os.getcwd()
        source_dir = c + "/Resources/Batfish Bases"
        destination_dir = c + "/Outcomes/Waypoint/Exp"+str(a)+'/Batfish'
        shutil.copytree(source_dir, destination_dir)
        with open(c + "/Outcomes/Waypoint/Exp"+str(a)+'/Batfish/Config-Generator/Topology/topology.json', 'w') as f:
            json.dump(top, f)

        cflows = []
        for x in range(0, CONCURRENT_FLOWS):
            pair = getPairOfNodes(g)
            pair[0] = pair[0][1:]
            pair[1] = pair[1][1:]
            cflows.append(pair)

        p = r[a]['path']
        p1 = []
        for x in p:
            p1.append(int(x[1:]))
        path = {'port':1234,'src': r[a]['source'][1:], 'dst': r[a]['target'][1:], 'path': p1, 'waypoint': int(r[a]['waypoint'][1:]), 'loop': 0, 'cflows':cflows}
        with open("./Outcomes/Waypoint/Exp"+str(a)+'/Batfish/path', 'w') as f:
            json.dump(path, f)

def genVermonWp(r, g):
    nodes = len(g.nodes())
    hosts = 1
    edg = []
    for u,v in g.edges():
        x = ['s'+str(u[1:]), 's'+str(v[1:])]
        edg.append(x)

    for a in range(0, len(r)):
        # c = os.getcwd()
        # source_dir = c + "/Resources/Vermon Bases/Waypoint"
        # destination_dir = c + "/Outcomes/Waypoint/Exp"+str(a)+'/Vermon'
        # shutil.copytree(source_dir, destination_dir)

        network = ''
        with open('./Resources/Vermon Bases/Waypoint/experiments/general/network.json', 'r') as f:
            network = json.load(f)

        network['nodes'] = nodes
        network['hosts_per_node'] = hosts
        network['node_links'] = edg

        os.makedirs("./Outcomes/Waypoint/Exp"+str(a)+"/Vermon/")
        with open("./Outcomes/Waypoint/Exp"+str(a)+'/Vermon/network.json', 'w') as f:
            json.dump(network, f)

        workload = ''
        with open('./Resources/Vermon Bases/Waypoint/experiments/general/workload.json', 'r') as f:
            workload = json.load(f)
        #
        # workload['tcpreplay'][0]['sender'] = 'h' + r[a]['source'][1:]
        # workload['tcpreplay'][0]['receiver'] = 'h' + r[a]['target'][1:]
        # workload['tcpreplay'][0]['receiver_opt'] = '10.0.'+str(r[a]['target'][1:]) + '.' +str(r[a]['target'][1:]) + ' 1234'
        #
        with open("./Outcomes/Waypoint/Exp"+str(a)+'/Vermon/workload.json', 'w') as f:
            json.dump(workload, f)

        cflows = []
        c = 1
        for x in range(0, CONCURRENT_FLOWS):
            pair = getPairOfNodes(g)
            pair[0] = pair[0][1:]
            pair[1] = pair[1][1:]
            pair.append(1234+c)
            c += 1
            cflows.append(pair)

        p = r[a]['path']
        p1 = []
        for x in p:
            p1.append(int(x[1:]))
        path = {'port':1234,'src': r[a]['source'][1:], 'dst': r[a]['target'][1:], 'path': p1, 'loop': 0, 'waypoint': r[a]['waypoint'][1:], 'cflows': cflows}
        with open("./Outcomes/Waypoint/Exp"+str(a)+'/Vermon/path', 'w') as f:
            json.dump(path, f)

def genVermonWpIncorrect(r, g):
    nodes = len(g.nodes())
    hosts = 1
    edg = []
    for u,v in g.edges():
        x = ['s'+str(u[1:]), 's'+str(v[1:])]
        edg.append(x)

    for a in range(0, len(r)):
        # c = os.getcwd()
        # source_dir = c + "/Resources/Vermon Bases/Waypoint"
        # destination_dir = c + "/Outcomes/Waypoint/Exp"+str(a)+'/Vermon'
        # shutil.copytree(source_dir, destination_dir)

        network = ''
        with open('./Resources/Vermon Bases/Waypoint/experiments/general/network.json', 'r') as f:
            network = json.load(f)

        network['nodes'] = nodes
        network['hosts_per_node'] = hosts
        network['node_links'] = edg

        os.makedirs("./Outcomes/WaypointIncorrect/Exp"+str(a)+"/Vermon/")
        with open("./Outcomes/WaypointIncorrect/Exp"+str(a)+'/Vermon/network.json', 'w') as f:
            json.dump(network, f)

        workload = ''
        with open('./Resources/Vermon Bases/Waypoint/experiments/general/workload.json', 'r') as f:
            workload = json.load(f)
        #
        # workload['tcpreplay'][0]['sender'] = 'h' + r[a]['source'][1:]
        # workload['tcpreplay'][0]['receiver'] = 'h' + r[a]['target'][1:]
        # workload['tcpreplay'][0]['receiver_opt'] = '10.0.'+str(r[a]['target'][1:]) + '.' +str(r[a]['target'][1:]) + ' 1234'
        #
        with open("./Outcomes/WaypointIncorrect/Exp"+str(a)+'/Vermon/workload.json', 'w') as f:
            json.dump(workload, f)

        cflows = []
        for x in range(0, CONCURRENT_FLOWS):
            pair = getPairOfNodes(g)
            pair[0] = pair[0][1:]
            pair[1] = pair[1][1:]
            cflows.append(pair)

        p = r[a]['path']
        p1 = []
        for x in p:
            p1.append(int(x[1:]))
        path = {'port':1234,'src': r[a]['source'][1:], 'dst': r[a]['target'][1:], 'path': p1, 'loop': 0, 'waypoint': r[a]['waypoint'][1:], 'cflows': cflows}
        with open("./Outcomes/WaypointIncorrect/Exp"+str(a)+'/Vermon/path', 'w') as f:
            json.dump(path, f)

def genBatFishLoop(r, g):
    nodes = len(g.nodes())
    hosts = 1
    edges = []
    for u,v in g.edges():
        e = {'start': int(u[1:]), 'end':int(v[1:])}
        edges.append(e)
    top = {"network": {"n_nodes": nodes, "n_hosts_per_node": hosts, "edges": edges}}

    for a in range(0, len(r)):
        c = os.getcwd()
        source_dir = c + "/Resources/Batfish Bases"
        destination_dir = c + "/Outcomes/Loop/Exp"+str(a)+'/Batfish'
        shutil.copytree(source_dir, destination_dir)
        with open(c + "/Outcomes/Loop/Exp"+str(a)+'/Batfish/Config-Generator/Topology/topology.json', 'w') as f:
            json.dump(top, f)

        cflows = []
        for x in range(0, CONCURRENT_FLOWS):
            pair = getPairOfNodes(g)
            pair[0] = pair[0][1:]
            pair[1] = pair[1][1:]
            cflows.append(pair)

        p = r[a]['path']
        p1 = []
        for x in p:
            p1.append(int(x[1:]))
        path = {'port':1234,'src': r[a]['source'][1:], 'dst': r[a]['target'][1:], 'path': p1, 'loop': 1, 'cflows': cflows}
        with open("./Outcomes/Loop/Exp"+str(a)+'/Batfish/path', 'w') as f:
            json.dump(path, f)

def genVermonLoop(r, g):
    nodes = len(g.nodes())
    hosts = 1
    edg = []
    for u,v in g.edges():
        x = ['s'+str(u[1:]), 's'+str(v[1:])]
        edg.append(x)

    for a in range(0, len(r)):
        # c = os.getcwd()
        # source_dir = c + "/Resources/Vermon Bases/Loop"
        # destination_dir = c + "/Outcomes/Loop/Exp"+str(a)+'/Vermon'
        # shutil.copytree(source_dir, destination_dir)

        network = ''
        with open('./Resources/Vermon Bases/Loop/experiments/general/network.json', 'r') as f:
            network = json.load(f)

        network['nodes'] = nodes
        network['hosts_per_node'] = hosts
        network['node_links'] = edg

        os.makedirs("./Outcomes/Loop/Exp"+str(a)+"/Vermon/")
        with open("./Outcomes/Loop/Exp"+str(a)+'/Vermon/network.json', 'w') as f:
            json.dump(network, f)

        workload = ''
        with open('./Resources/Vermon Bases/Loop/experiments/general/workload.json', 'r') as f:
            workload = json.load(f)
        #
        # workload['tcpreplay'][0]['sender'] = 'h' + r[a]['source'][1:]
        # workload['tcpreplay'][0]['receiver'] = 'h' + r[a]['target'][1:]
        # workload['tcpreplay'][0]['receiver_opt'] = '10.0.'+str(r[a]['target'][1:]) + '.' +str(r[a]['target'][1:]) + ' 1234'
        #
        with open("./Outcomes/Loop/Exp"+str(a)+'/Vermon/workload.json', 'w') as f:
            json.dump(workload, f)

        cflows = []
        c = 1
        for x in range(0, CONCURRENT_FLOWS):
            pair = getPairOfNodes(g)
            pair[0] = pair[0][1:]
            pair[1] = pair[1][1:]
            pair.append(1234+c)
            c += 1
            cflows.append(pair)

        p = r[a]['path']
        p1 = []
        for x in p:
            p1.append(int(x[1:]))
        path = {'port':1234,'src': r[a]['source'][1:], 'dst': r[a]['target'][1:], 'path': p1, 'loop': 1, 'cflows': cflows}
        with open("./Outcomes/Loop/Exp"+str(a)+'/Vermon/path', 'w') as f:
            json.dump(path, f)

def genPlayers():
    # c = os.getcwd()
    # source_dir = c + "/Resources/Vermon Bases/Loop"
    # destination_dir = c + "/Outcomes/Loop/Executable"
    # shutil.copytree(source_dir, destination_dir)
    #
    # c = os.getcwd()
    # source_dir = c + "/Resources/Vermon Bases/Waypoint"
    # destination_dir = c + "/Outcomes/Waypoint/Executable"
    # shutil.copytree(source_dir, destination_dir)
    #
    # c = os.getcwd()
    # source_dir = c + "/Resources/Vermon Bases/Waypoint"
    # destination_dir = c + "/Outcomes/WaypointIncorrect/Executable"
    # shutil.copytree(source_dir, destination_dir)

    c = os.getcwd()
    source_dir = c + "/Resources/Vermon Bases/Reachability"
    destination_dir = c + "/Outcomes/Reachability/Executable"
    shutil.copytree(source_dir, destination_dir)

    # c = os.getcwd()
    # source_dir = c + "/Resources/Vermon Bases/Reachability"
    # destination_dir = c + "/Outcomes/ReachabilityIncorrect/Executable"
    # shutil.copytree(source_dir, destination_dir)

def getPairOfNodes(g):
    first_node = random.choice(list(g.nodes()))                  # pick a random node
    possible_nodes = set(g.nodes())
    neighbours = [first_node]
    possible_nodes.difference_update(neighbours)    # remove the first node
    second_node = random.choice(list(possible_nodes))

    return [first_node, second_node]

def genReachabilityPair(g):
    pair = getPairOfNodes(g)

    path = nx.shortest_path(g, pair[0], pair[1])

    return {'source': pair[0], 'target': pair[1], 'path': path}

def genWaypointCorrect(g):
    path = []

    while(len(path) < 3):
        pair = getPairOfNodes(g)

        path = nx.shortest_path(g, pair[0], pair[1])

    wp = random.choice(path[1:-1])

    return {'source': pair[0], 'target': pair[1], 'waypoint': wp, 'path': path}

def genWaypointIncorrect(g):
    path = []

    while(len(path) < 3):
        pair = getPairOfNodes(g)

        path = nx.shortest_path(g, pair[0], pair[1])

    s = set(g.nodes())
    s.difference_update(path)
    wp = random.choice(list(s))

    return {'source': pair[0], 'target': pair[1], 'waypoint': wp, 'path': path}

def genLoop(G, source='S1', cycle_length_limit=5):
    """forked from networkx dfs_edges function. Assumes nodes are integers, or at least
    types which work with min() and > ."""
    if source is None:
        # produce edges for all components
        nodes=[i[0] for i in nx.connected_components(G)]
    else:
        # produce edges for components with source
        nodes=[source]
    # extra variables for cycle detection:
    cycle_stack = []
    output_cycles = set()

    def get_hashable_cycle(cycle):
        """cycle as a tuple in a deterministic order."""
        m = min(cycle)
        mi = cycle.index(m)
        mi_plus_1 = mi + 1 if mi < len(cycle) - 1 else 0
        if cycle[mi-1] > cycle[mi_plus_1]:
            result = cycle[mi:] + cycle[:mi]
        else:
            result = list(reversed(cycle[:mi_plus_1])) + list(reversed(cycle[mi_plus_1:]))
        return tuple(result)

    for start in nodes:
        if start in cycle_stack:
            continue
        cycle_stack.append(start)

        stack = [(start,iter(G[start]))]
        while stack:
            parent,children = stack[-1]
            try:
                child = next(children)

                if child not in cycle_stack:
                    cycle_stack.append(child)
                    stack.append((child,iter(G[child])))
                else:
                    i = cycle_stack.index(child)
                    if i < len(cycle_stack) - 2:
                      output_cycles.add(get_hashable_cycle(cycle_stack[i:]))

            except StopIteration:
                stack.pop()
                cycle_stack.pop()

    loop = random.choice([list(i) for i in output_cycles])
    return {'source': loop[0], 'target': loop[-1], 'path': loop}

def generator():

    #graph creation
    with open(sys.argv[1], 'r') as f:
        js_graph = json.load(f)
    imported_network = json_graph.node_link_graph(js_graph)

    reach = []
    for a in range(0,EXP_NUM):
        reach.append(genReachabilityPair(imported_network))

    correctwp = []
    for a in range(0,EXP_NUM):
        correctwp.append(genWaypointCorrect(imported_network))

    incorrectwp = []
    for a in range(0,EXP_NUM):
        incorrectwp.append(genWaypointIncorrect(imported_network))

    loop = []
    for a in range(0,EXP_NUM):
        loop.append(genLoop(imported_network, random.choice(list(imported_network.nodes()))))

    #showing imported network
    #nx.draw(imported_network, with_labels = True)
    #plt.show()
    genBatFishReach(reach, imported_network)
    #genBatFishWp(correctwp, imported_network)
    #genBatFishLoop(loop, imported_network)

    genVermonReach(reach, imported_network)
    #genVermonWp(correctwp, imported_network)
    #genVermonLoop(loop, imported_network)
    #genVermonWpIncorrect(incorrectwp, imported_network)
    #genVermonReachIncorrect(reach, imported_network)

    genPlayers()

if __name__ == "__main__":
    generator()
