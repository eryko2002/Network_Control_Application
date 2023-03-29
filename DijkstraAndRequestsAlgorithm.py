import sys
import json
import requests
import numbers
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
    def construct_graph(self, nodes, init_graph):
        "Funkcja construct_graph sprawdza czy ścieżka z węzła A do B ma taką samą wartość, co ścieżka z węzła B do A"
        graph = {}
        for node in nodes:
            graph[node] = {}
        graph.update(init_graph)
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
        return graph
    def get_nodes(self):
        "Funkcja get_nodes zwraca węzły"
        return self.nodes
    def get_outgoing_edges(self, node):
        "Funkcja get_outgoing_edges zwraca sąsiadów danego węzłą"
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    def value(self, node1, node2):
        "Funkcja zwraca wartość skrajną między dwoma węzłami"
        return self.graph[node1][node2]

odwroconalista = []
def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Add the start node manually
    path.append(start_node)
    reversedlist = list(reversed(path))
    print(reversedlist)
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))
    return reversedlist

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    "We'll use this dict to save the cost of visiting each node and update it as we move along the graph"
    shortest_path = {}
    "We'll use this dict to save the shortest known path to a node found so far"
    previous_nodes = {}
    "We'll use max_value to initialize the infinity value of the unvisited nodes"
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    "However, we initialize the starting node's value with 0"
    shortest_path[start_node] = 0
    "The algorithm executes until we visit all nodes"
    while unvisited_nodes:
        "The code block below finds the node with the lowest score"
        current_min_node = None
        for node in unvisited_nodes:  # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        "The code block below retrieves the current node's neighbors and updates their distances"
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                "We also update the best path to the current node"
                previous_nodes[neighbor] = current_min_node
        "After visiting its neighbors, we mark the node as visited"
        unvisited_nodes.remove(current_min_node)
    return previous_nodes, shortest_path

def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values
def convertToSwitch_startNode(start_node):
    if (start_node=="warszawa"):
        start_node="of:0000000000000001"
    elif (start_node=="bialystok"):
        start_node="of:0000000000000002"
    elif (start_node=="gdansk"):
        start_node = "of:0000000000000003"
    elif (start_node=="szczecin"):
        start_node = "of:0000000000000004"
    elif (start_node=="poznan"):
        start_node = "of:0000000000000005"
    elif (start_node=="bydgoszcz"):
        start_node = "of:0000000000000006"
    elif (start_node=="lodz"):
        start_node = "of:0000000000000007"
    elif (start_node=="krakow"):
        start_node = "of:0000000000000008"
    elif (start_node=="wroclaw"):
        start_node = "of:0000000000000009"
    elif (start_node=="rzeszow"):
        start_node = "of:000000000000000a"
    return start_node
def convertToSwitch_targetNode(target_node):
    if (target_node == "warszawa"):
        target_node = "of:0000000000000001"
    elif (target_node == "bialystok"):
        target_node = "of:0000000000000002"
    elif (target_node == "gdansk"):
        target_node = "of:0000000000000003"
    elif (target_node == "szczecin"):
        target_node = "of:0000000000000004"
    elif (target_node == "poznan"):
        target_node = "of:0000000000000005"
    elif (target_node == "bydgoszcz"):
        target_node = "of:0000000000000006"
    elif (target_node == "lodz"):
        target_node = "of:0000000000000007"
    elif (target_node == "krakow"):
        target_node = "of:0000000000000008"
    elif (target_node == "wroclaw"):
        target_node = "of:0000000000000009"
    elif (target_node == "rzeszow"):
        target_node = "of:000000000000000a"
    return target_node
if __name__=="__main__":
    usedlist = []
    odwroconalista = []
    nodes = ["of:0000000000000001", "of:0000000000000002", "of:0000000000000003", "of:0000000000000004", "of:0000000000000005", "of:0000000000000006", "of:0000000000000007", "of:0000000000000008", "of:0000000000000009", "of:000000000000000a"]
    init_graph = {}
    for node in nodes:
        init_graph[node] = {}

    init_graph["of:0000000000000001"]["of:0000000000000002"] = 1.41  # Warszawa-Bialystok
    init_graph["of:0000000000000001"]["of:0000000000000003"] = 2.40  # Warszawa-Gdansk
    init_graph["of:0000000000000003"]["of:0000000000000004"] = 2.55  # Gdansk-Szczecin
    init_graph["of:0000000000000001"]["of:0000000000000005"] = 2.20  # Warszawa-Poznan
    init_graph["of:0000000000000005"]["of:0000000000000006"] = 0.98  # Poznan-Bydgoszcz
    init_graph["of:0000000000000001"]["of:0000000000000007"] = 0.96  # Warszawa-Lodz
    init_graph["of:0000000000000001"]["of:0000000000000008"] = 2.05  # Warszawa-Krakow
    init_graph["of:0000000000000008"]["of:0000000000000009"] = 1.91  # Krakow-Wroclaw
    init_graph["of:0000000000000008"]["of:000000000000000a"] = 1.18  # Krakow-Rzeszow

    init_graph["of:0000000000000001"]["of:000000000000000a"] = 2.33  # Warszawa-Rzeszow 330km
    init_graph["of:0000000000000001"]["of:0000000000000006"] = 2.13  # Warszawa-Bydgoszcz 302km
    init_graph["of:0000000000000007"]["of:0000000000000008"] = 1.97  # Lodz-Krakow 280 km
    init_graph["of:0000000000000007"]["of:0000000000000009"] = 1.56  # Lodz-Wroclaw 221km
    init_graph["of:0000000000000007"]["of:0000000000000005"] = 1.50  # Lodz-Poznan 212km
    init_graph["of:0000000000000005"]["of:0000000000000009"] = 1.29  # Poznan-Wroclaw 183km
    init_graph["of:0000000000000005"]["of:0000000000000004"] = 1.88  # Poznan-Szczecin 266km
    init_graph["of:0000000000000004"]["of:0000000000000009"] = 2.94  # Szczecin-Wroclaw 416km
    init_graph["of:0000000000000004"]["of:0000000000000006"] = 1.83  # Szczecin-Bydgoszcz 259km
    init_graph["of:0000000000000002"]["of:000000000000000a"] = 3.41  # Bialystok-Rzeszow 482km
    init_graph["of:0000000000000003"]["of:0000000000000002"] = 2.76  # Gdansk-Bialystok 391km
    init_graph["of:0000000000000003"]["of:0000000000000006"] = 1.18  # Gdansk-Bydgoszcz 167km

    vall = int(input("Enter your value: "))
    for trial in range(vall):
        if (trial==0):
            graph = Graph(nodes, init_graph)

            start_node = input(str("Type start_node:"))
            target_node = input(str("Type target_node:"))
            start_node = convertToSwitch_startNode(start_node)
            target_node = convertToSwitch_targetNode(target_node)
            previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=start_node)
            odwroconalista = print_result(previous_nodes, shortest_path, start_node=start_node, target_node=target_node)
            print(odwroconalista)

            host = "192.168.56.103"
            portX = "8181"
            username = "onos"
            password = "rocks"
            url = f"http://{host}:{portX}/onos/v1/flows"
            headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

            dictionary1 = {"flows": []}
            dictionary2 = {"flows": []}
            val1 = []
            val2 = []
            listContainingJsonRequests = []
            with open('daneLink.json', 'r') as f:
                data = json.load(f)
                device = json_extract(data, 'device')
                port = json_extract(data, 'port')

                "pętla dla wszystkich węzłów poza ostatnim i pierwszym"
                for x in range(1, len(odwroconalista) - 1):
                    tab = []
                    for y in range(1, len(odwroconalista) - 1):
                        for m in range(0, len(device)):
                            if (odwroconalista[x] == device[m] and odwroconalista[x + 1] == device[m + 1] and m % 2 == 0):
                                for p in range(0, len(device) - 1):
                                    if (odwroconalista[x] == device[p + 1] and odwroconalista[x - 1] == device[p]):
                                        dictionary = {"flows": []}

                                        if (odwroconalista[x + 1][-1] == 'a'):
                                            ipA = '10'
                                        else:
                                            ipA = odwroconalista[x + 1][-1]
                                        if (odwroconalista[x - 1][-1] == 'a'):
                                            ipB = '10'
                                        else:
                                            ipB = odwroconalista[x - 1][-1]

                                        a = {"priority": 40000, "timeout": 0, "isPermanent": "true",
                                             "deviceId": odwroconalista[x],
                                             "treatment": {"instructions": [{"type": "OUTPUT", "port": port[m]}]},
                                             "selector": {
                                                 "criteria": [{"type": "IN_PORT", "port": port[p + 1]},
                                                              {"type": "ETH_TYPE", "ethType": "0x0800"},
                                                              {"type": "IPV4_DST", "ip": "10.0.0." + ipA + "/32"}]}}
                                        b = {"priority": 40000, "timeout": 0, "isPermanent": "true",
                                             "deviceId": odwroconalista[x],
                                             "treatment": {"instructions": [{"type": "OUTPUT", "port": port[p + 1]}]},
                                             "selector": {
                                                 "criteria": [{"type": "IN_PORT", "port": port[m]},
                                                              {"type": "ETH_TYPE", "ethType": "0x0800"},
                                                              {"type": "IPV4_DST",
                                                               "ip": "10.0.0." + ipB + "/32"}]}}
                                        dictionary["flows"].append(a)
                                        dictionary["flows"].append(b)
                                        tab.append(a)
                                        tab.append(b)

                                        with open("filename" + odwroconalista[x][-1] + ".json", "w") as outfile:
                                            if (("filename" + odwroconalista[x][-1] + ".json") not in listContainingJsonRequests):
                                                listContainingJsonRequests.append(
                                                    "filename" + odwroconalista[x][-1] + ".json")
                                            json.dump(dictionary, outfile, indent=4)
                                            urL = f"http://{host}:{portX}/onos/v1/flows/" + "of:000000000000000" + \
                                                  odwroconalista[x][-1]
                                            for val in tab:
                                                requests.post(url=urL, json=val, headers=headers,
                                                              auth=(username, password))
                                        tab.clear()
                                        dictionary.clear()
                "pętla dla pierwszego i ostatniego węzła"
                for d in range(0, len(device)):
                    if (odwroconalista[0] == device[d] and odwroconalista[1] == device[d + 1]):
                        for k in range(0, len(device) - 1):
                            if (odwroconalista[-1] == device[k + 1] and odwroconalista[-2] == device[k]):

                                if (device[d + 1][-1] == 'a'):
                                    ipE = '10'
                                else:
                                    ipE = device[d + 1][-1]
                                if (device[d][-1] == 'a'):
                                    ipF = '10'
                                else:
                                    ipF = device[d][-1]
                                if (device[k + 1][-1] == 'a'):
                                    ipG = '10'
                                else:
                                    ipG = device[k + 1][-1]
                                if (device[k + 1][-1] == 'a'):
                                    ipH = '10'
                                else:
                                    ipH = device[k + 1][-1]
                                if (device[k][-1] == 'a'):
                                    ipI = '10'
                                else:
                                    ipI = device[k][-1]
                                if (device[d][-1] == 'a'):
                                    ipJ = '10'
                                else:
                                    ipJ = device[d][-1]
                                e = {"priority": 40000, "timeout": 0, "isPermanent": "true",
                                     "deviceId": odwroconalista[0],
                                     "treatment": {"instructions": [{"type": "OUTPUT", "port": port[d]}]}, "selector": {
                                        "criteria": [{"type": "IN_PORT", "port": "1"},
                                                     {"type": "ETH_TYPE", "ethType": "0x0800"},
                                                     {"type": "IPV4_DST", "ip": "10.0.0." + ipE + "/32"}]}}
                                f = {"priority": 40000, "timeout": 0, "isPermanent": "true",
                                     "deviceId": odwroconalista[0],
                                     "treatment": {"instructions": [{"type": "OUTPUT", "port": "1"}]}, "selector": {
                                        "criteria": [{"type": "IN_PORT", "port": port[d]},
                                                     {"type": "ETH_TYPE", "ethType": "0x0800"},
                                                     {"type": "IPV4_DST", "ip": "10.0.0." + ipF + "/32"}]}}
                                g = {"priority": 40000, "timeout": 0, "isPermanent": "true",
                                     "deviceId": odwroconalista[0],
                                     "treatment": {"instructions": [{"type": "OUTPUT", "port": port[d]}]}, "selector": {
                                        "criteria": [{"type": "IN_PORT", "port": "1"},
                                                     {"type": "ETH_TYPE", "ethType": "0x0800"},
                                                     {"type": "IPV4_DST", "ip": "10.0.0." + ipG + "/32"}]}}
                                h = {"priority": 40000, "timeout": 0, "isPermanent": "true",
                                     "deviceId": odwroconalista[-1],
                                     "treatment": {"instructions": [{"type": "OUTPUT", "port": "1"}]}, "selector": {
                                        "criteria": [{"type": "IN_PORT", "port": port[k + 1]},
                                                     {"type": "ETH_TYPE", "ethType": "0x0800"},
                                                     {"type": "IPV4_DST", "ip": "10.0.0." + ipH + "/32"}]}}
                                i = {"priority": 40000, "timeout": 0, "isPermanent": "true",
                                     "deviceId": odwroconalista[-1],
                                     "treatment": {"instructions": [{"type": "OUTPUT", "port": port[k + 1]}]},
                                     "selector": {
                                         "criteria": [{"type": "IN_PORT", "port": "1"},
                                                      {"type": "ETH_TYPE", "ethType": "0x0800"},
                                                      {"type": "IPV4_DST", "ip": "10.0.0." + ipI + "/32"}]}}
                                j = {"priority": 40000, "timeout": 0, "isPermanent": "true",
                                     "deviceId": odwroconalista[-1],
                                     "treatment": {"instructions": [{"type": "OUTPUT", "port": port[k + 1]}]},
                                     "selector": {
                                         "criteria": [{"type": "IN_PORT", "port": "1"},
                                                      {"type": "ETH_TYPE", "ethType": "0x0800"},
                                                      {"type": "IPV4_DST", "ip": "10.0.0." + ipJ + "/32"}]}}
                                dictionary1["flows"].append(e)
                                dictionary1["flows"].append(f)
                                dictionary1["flows"].append(g)

                                dictionary2["flows"].append(h)
                                dictionary2["flows"].append(i)
                                dictionary2["flows"].append(j)

                                val1.append(e)
                                val1.append(f)
                                val1.append(g)

                                val2.append(h)
                                val2.append(i)
                                val2.append(j)

                                with open("filename" + "START" + ".json", "w") as outfile1:
                                    listContainingJsonRequests.append("filename" + "START" + ".json")
                                    json.dump(dictionary1, outfile1, indent=4)
                                    urL1 = f"http://{host}:{portX}/onos/v1/flows/" + "of:000000000000000" + \
                                           odwroconalista[0][-1]
                                    for l in val1:
                                        requests.post(url=urL1, json=l, headers=headers, auth=(username, password))
                                with open("filename" + "END" + ".json", "w") as outfile2:
                                    listContainingJsonRequests.append("filename" + "END" + ".json")
                                    json.dump(dictionary2, outfile2, indent=4)
                                    urL2 = f"http://{host}:{portX}/onos/v1/flows/" + "of:000000000000000" + \
                                           odwroconalista[-1][-1]
                                    for z in val2:
                                        requests.post(url=urL2, json=z, headers=headers, auth=(username, password))
            continue
        else:
            for liczba in range(len(odwroconalista)-1):
                if (isinstance(init_graph[odwroconalista[liczba]][odwroconalista[liczba + 1]],numbers.Number) == True or
                        isinstance(init_graph[odwroconalista[liczba + 1]][odwroconalista[liczba]].isnumeric,numbers.Number) == True):
                    del init_graph[odwroconalista[liczba]][odwroconalista[liczba + 1]]
                    del init_graph[odwroconalista[liczba + 1]][odwroconalista[liczba]]

            graph = Graph(nodes, init_graph)
            start_node = input(str("Type start_node:")) #Użytkownik podaje z konsoli węzeł początkowy
            target_node = input(str("Type target_node:")) #Użytkownik podaje z konsoli węzeł docelowy
            start_node = convertToSwitch_startNode(start_node)
            target_node = convertToSwitch_targetNode(target_node)
            previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=start_node)
            odwroconalista = print_result(previous_nodes, shortest_path, start_node=start_node, target_node=target_node)
            print(odwroconalista)

            host = "192.168.56.103"
            portX = "8181"
            username = "onos"
            password = "rocks"
            url = f"http://{host}:{portX}/onos/v1/flows"
            headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

            dictionary1 = {"flows": []}
            dictionary2 = {"flows": []}
            val1 = []
            val2 = []
            listContainingJsonRequests = []
            with open('daneLink.json', 'r') as f:
                data = json.load(f)
                device = json_extract(data, 'device')
                port = json_extract(data, 'port')
                "pętla dla wszystkich poza ostatnim i pierwszym"
                for x in range(1, len(odwroconalista) - 1):
                    tab = []
                    for y in range(1, len(odwroconalista) - 1):
                        for m in range(0, len(device)-1):
                            if (odwroconalista[x] == device[m] and odwroconalista[x + 1] == device[m + 1] and m % 2 == 0):
                                for p in range(0, len(device) - 1):
                                    if (odwroconalista[x] == device[p + 1] and odwroconalista[x - 1] == device[p]):
                                        dictionary = {"flows": []}

                                        if (odwroconalista[x + 1][-1] == 'a'):
                                            ipA = '10'
                                        else:
                                            ipA = odwroconalista[x + 1][-1]
                                        if (odwroconalista[x - 1][-1] == 'a'):
                                            ipB = '10'
                                        else:
                                            ipB = odwroconalista[x - 1][-1]

                                        a = {"priority": 40000, "timeout": 0, "isPermanent": "true",
                                             "deviceId": odwroconalista[x],
                                             "treatment": {"instructions": [{"type": "OUTPUT", "port": port[m]}]},
                                             "selector": {
                                                 "criteria": [{"type": "IN_PORT", "port": port[p + 1]},
                                                              {"type": "ETH_TYPE", "ethType": "0x0800"},
                                                              {"type": "IPV4_DST", "ip": "10.0.0." + ipA + "/32"}]}}
                                        b = {"priority": 40000, "timeout": 0, "isPermanent": "true",
                                             "deviceId": odwroconalista[x],
                                             "treatment": {"instructions": [{"type": "OUTPUT", "port": port[p + 1]}]},
                                             "selector": {
                                                 "criteria": [{"type": "IN_PORT", "port": port[m]},
                                                              {"type": "ETH_TYPE", "ethType": "0x0800"},
                                                              {"type": "IPV4_DST",
                                                               "ip": "10.0.0." + ipB + "/32"}]}}

                                        dictionary["flows"].append(a)
                                        dictionary["flows"].append(b)

                                        tab.append(a)
                                        tab.append(b)

                                        with open("filename" + odwroconalista[x][-1] + ".json", "w") as outfile:
                                            if (("filename" + odwroconalista[x][-1] + ".json") not in listContainingJsonRequests):
                                                listContainingJsonRequests.append(
                                                    "filename" + odwroconalista[x][-1] + ".json")
                                            json.dump(dictionary, outfile, indent=4)
                                            urL = f"http://{host}:{portX}/onos/v1/flows/" + "of:000000000000000" + \
                                                  odwroconalista[x][-1]
                                            for val in tab:
                                                requests.post(url=urL, json=val, headers=headers,
                                                              auth=(username, password))
                                        tab.clear()
                                        dictionary.clear()
                "pętla dla pierwszego i ostatniego"
                for d in range(0, len(device)):
                    if (odwroconalista[0] == device[d] and odwroconalista[1] == device[d + 1]):
                        for k in range(0, len(device) - 1):
                            if (odwroconalista[-1] == device[k + 1] and odwroconalista[-2] == device[k]):

                                if (device[d + 1][-1] == 'a'):
                                    ipE = '10'
                                else:
                                    ipE = device[d + 1][-1]
                                if (device[d][-1] == 'a'):
                                    ipF = '10'
                                else:
                                    ipF = device[d][-1]
                                if (device[k + 1][-1] == 'a'):
                                    ipG = '10'
                                else:
                                    ipG = device[k + 1][-1]
                                if (device[k + 1][-1] == 'a'):
                                    ipH = '10'
                                else:
                                    ipH = device[k + 1][-1]
                                if (device[k][-1] == 'a'):
                                    ipI = '10'
                                else:
                                    ipI = device[k][-1]
                                if (device[d][-1] == 'a'):
                                    ipJ = '10'
                                else:
                                    ipJ = device[d][-1]
                                e = {"priority": 40000, "timeout": 0, "isPermanent": "true",
                                     "deviceId": odwroconalista[0],
                                     "treatment": {"instructions": [{"type": "OUTPUT", "port": port[d]}]}, "selector": {
                                        "criteria": [{"type": "IN_PORT", "port": "1"},
                                                     {"type": "ETH_TYPE", "ethType": "0x0800"},
                                                     {"type": "IPV4_DST", "ip": "10.0.0." + ipE + "/32"}]}}
                                f = {"priority": 40000, "timeout": 0, "isPermanent": "true",
                                     "deviceId": odwroconalista[0],
                                     "treatment": {"instructions": [{"type": "OUTPUT", "port": "1"}]}, "selector": {
                                        "criteria": [{"type": "IN_PORT", "port": port[d]},
                                                     {"type": "ETH_TYPE", "ethType": "0x0800"},
                                                     {"type": "IPV4_DST", "ip": "10.0.0." + ipF + "/32"}]}}
                                g = {"priority": 40000, "timeout": 0, "isPermanent": "true",
                                     "deviceId": odwroconalista[0],
                                     "treatment": {"instructions": [{"type": "OUTPUT", "port": port[d]}]}, "selector": {
                                        "criteria": [{"type": "IN_PORT", "port": "1"},
                                                     {"type": "ETH_TYPE", "ethType": "0x0800"},
                                                     {"type": "IPV4_DST", "ip": "10.0.0." + ipG + "/32"}]}}
                                h = {"priority": 40000, "timeout": 0, "isPermanent": "true",
                                     "deviceId": odwroconalista[-1],
                                     "treatment": {"instructions": [{"type": "OUTPUT", "port": "1"}]}, "selector": {
                                        "criteria": [{"type": "IN_PORT", "port": port[k + 1]},
                                                     {"type": "ETH_TYPE", "ethType": "0x0800"},
                                                     {"type": "IPV4_DST", "ip": "10.0.0." + ipH + "/32"}]}}
                                i = {"priority": 40000, "timeout": 0, "isPermanent": "true",
                                     "deviceId": odwroconalista[-1],
                                     "treatment": {"instructions": [{"type": "OUTPUT", "port": port[k + 1]}]},
                                     "selector": {
                                         "criteria": [{"type": "IN_PORT", "port": "1"},
                                                      {"type": "ETH_TYPE", "ethType": "0x0800"},
                                                      {"type": "IPV4_DST", "ip": "10.0.0." + ipI + "/32"}]}}
                                j = {"priority": 40000, "timeout": 0, "isPermanent": "true",
                                     "deviceId": odwroconalista[-1],
                                     "treatment": {"instructions": [{"type": "OUTPUT", "port": port[k + 1]}]},
                                     "selector": {
                                         "criteria": [{"type": "IN_PORT", "port": "1"},
                                                      {"type": "ETH_TYPE", "ethType": "0x0800"},
                                                      {"type": "IPV4_DST", "ip": "10.0.0." + ipJ + "/32"}]}}

                                dictionary1["flows"].append(e)
                                dictionary1["flows"].append(f)
                                dictionary1["flows"].append(g)

                                dictionary2["flows"].append(h)
                                dictionary2["flows"].append(i)
                                dictionary2["flows"].append(j)

                                val1.append(e)
                                val1.append(f)
                                val1.append(g)

                                val2.append(h)
                                val2.append(i)
                                val2.append(j)

                                with open("filename" + "START" + ".json", "w") as outfile1:
                                    listContainingJsonRequests.append("filename" + "START" + ".json")
                                    json.dump(dictionary1, outfile1, indent=4)
                                    urL1 = f"http://{host}:{portX}/onos/v1/flows/" + "of:000000000000000" + \
                                           odwroconalista[0][-1]
                                    for l in val1:
                                        requests.post(url=urL1, json=l, headers=headers, auth=(username, password))
                                with open("filename" + "END" + ".json", "w") as outfile2:
                                    listContainingJsonRequests.append("filename" + "END" + ".json")
                                    json.dump(dictionary2, outfile2, indent=4)
                                    urL2 = f"http://{host}:{portX}/onos/v1/flows/" + "of:000000000000000" + \
                                           odwroconalista[-1][-1]
                                    for z in val2:
                                        requests.post(url=urL2, json=z, headers=headers, auth=(username, password))

        listContainingAPI=[]
        #print("Lista zawierająca prośby:",listContainingJsonRequests)

        for jsonRequest in listContainingJsonRequests:
            api = 'curl --user onos:rocks -X POST "{}" -d @{} -H "Content-Type: application/json" -H "Accept: application/json"'.format(
                url, jsonRequest)
            listContainingAPI.append(api)

        with open("OnosPython1.bat","w") as rules:
            for element in listContainingAPI:
                rules.write(element + "\n")
