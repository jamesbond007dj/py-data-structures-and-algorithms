from collections import deque

class Graph:
  
  def __init__(self):

    self._adjacency_list = {}

  def add(self, value):

    n = Vertex(value)
    self._adjacency_list[n] = []
    return n

  def add_edge(self, start, end, weight=0):
 
    self.__valid_vertex(start)
    self.__valid_vertex(end)

    for edge in self._adjacency_list[start]:

      if edge == (end, int):
        edge = (end, weight)
        return

    self._adjacency_list[start].append((end, weight))


  def size(self):
    return len(self._adjacency_list)


  def get_vertexices(self):
    return list(self._adjacency_list.keys())


  def get_neighbors(self, vertex):
    self.__valid_vertex(vertex)
    return self._adjacency_list[vertex]


  def breath_first(self, vertex):
    output = []

    def action(vertex):
      output.append(vertex.value)

    self.__traverse(vertex, action)

    return output


  def depth_first(self, vertex):

    output = []

    def action(vertex):
      output.append(vertex.value)

    self.__recurse(vertex, action)

    return output


  def add_double_edge(self, vertex1, vertex2, weight=0, weight2=None):

    weight2 = weight if weight2 == None else weight2 or 0
    self.add_edge(vertex1, vertex2, weight)
    self.add_edge(vertex2, vertex1, weight2)


  def get_edge(self, flagged_lst):


    def contains_vertex(value, lst):
      
      for vertex in lst:
       
        if isinstance(vertex, Vertex):
          if vertex.value == value:
            return vertex
        
        elif vertex[0].value == value:
          return vertex
      
      return False, 0

    
    current = contains_vertex(flagged_lst[0], self.get_vertexices())
    if isinstance(current, Vertex):
      travel_sum = 0
     
      for index in range(1,len(flagged_lst)):
        
        current,cost = contains_vertex(flagged_lst[index], self.get_neighbors(current))
        travel_sum += cost
        
        if not current:
          return (False, '$0')
      
      return (True, f'${str(travel_sum)}')
   
    return (False, '$0')


  def __traverse(self, vertex, action):

    self.__valid_vertex(vertex)

    q = Queue()
    q.enqueue(vertex)
    visited = set([vertex])

    while not q.empty():
      current = q.dequeue()

      for vertex in self.get_neighbors(current):
        vertex = vertex[0]
        if vertex not in visited:
          visited.add(vertex)
          q.enqueue(vertex)

      action(current)


  def __recurse(self, vertex, action):
 
    visited = set()

    def recurse(vertex, action):

      visited.add(vertex)
      action(vertex)

      for vertex in self.get_neighbors(vertex):
        if vertex[0] not in visited:
          recurse(vertex[0], action)

    recurse(vertex, action)


  def __valid_vertex(self, vertex):
  
    if vertex not in self._adjacency_list.keys():
      raise KeyError(f'{vertex} is not in graph')
    return True


  def __len__(self):
    return len(self._adjacency_list)



class Vertex:
 
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return self.value



class Queue:
 
  def __init__(self):
    self.dq = deque()

  def enqueue(self, value):
    self.dq.appendleft(value)

  def dequeue(self):
    return self.dq.pop()

  def empty(self):
    return len(self.dq) == 0

class Stack:
 
  def __init__(self):
    self.dq = deque()

  def push(self, value):
    self.dq.append(value)

  def pop(self):
    return self.dq.pop()

  def empty(self):
    return len(self.dq) == 0