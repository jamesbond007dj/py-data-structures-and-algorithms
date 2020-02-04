import inspect, re, collections

class Graph:

    def __init__(self):
        self._set_list = {}

        name = inspect.getframeinfo(inspect.currentframe().f_back)[3][0].split()[0]
        self.name = re.sub(r'[=]', '', name)

    def __repr__(self):
        return self.name

    def add_node(self, value):
 
        node_ = Node_(value)
        try: 
            self._set_list[node_].append([node_])
        except:
            self._set_list[node_] = [[node_]]

        return node_

    def add_edge(self, start_node_, end_node_, weight=0):

        if start_node_ not in self._set_list or end_node_ not in self._set_list:
            raise KeyError(f'{start_node_} is not in {self}')
    
        set_list = self._set_list[start_node_]
        for i in range(len(set_list)):
            adjacencies = set_list[i]

            if adjacencies[0] == start_node_:
                adjacencies += [(end_node_, weight)]


    def size(self):
  
        return len(self._set_list)

    def get_values(self, node_):
 
        try:
            for v in self._set_list[node_]:
                if v[0] == node_:
                    return v[0].value
            return None
        except:
            raise KeyError(f'{node_} is not in {self}')

    def get_nodes(self):
        if self.size() == 0:
            return None
        return [v for v in self._set_list]

    def get_neighbors(self, node_):
        try:
            lst = [v[i] for v in self._set_list[node_] for i in range(1,len(v))]
            if lst:
                return lst
            return []
        except:
            return []

    def breadth_first(self, node_):

        if node_ not in self._set_list:
            raise KeyError(f'{node_} is not in {self}')

        visited_vertices = set()
        q = collections.deque()
        q.appendleft(node_)
       
        while q:
            current = q.pop()
            visited_vertices.add(current)
            lst = self.get_neighbors(current)
            if lst:
                for vert in lst:
                    if isinstance(vert, node_) and vert not in visited_vertices:
                        q.appendleft(vert)
        
        return visited_vertices


def get_edge(graph, flights):
    cost = 0
    neighbor = False

    if not flights:
        return f'{neighbor} : ${cost}'

    nodes = graph.get_nodes()
    if not nodes:
        return f'{neighbor} : ${cost}'
        
    flight_nodes = []
    for flight in flights:
        for node in nodes:
            if flight == node.value:
                flight_nodes.append(node)
    if len(flights) != len(flight_nodes):
        return f'{neighbor} : ${cost}'

    neighbors = graph.get_neighbors(flight_nodes[0])

    for i in range(1, len(flight_nodes)):
        neighbor = False
        for neighbor in neighbors:
            if neighbor[0] == flight_nodes[i]:
                cost += neighbor[1]
                neighbor = True
                break
        if not neighbor:
            return f'{neighbor} : $0'
        neighbors = graph.get_neighbors(flight_nodes[i])

    return f'{neighbor} : ${cost}'

class Node_:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return self.value