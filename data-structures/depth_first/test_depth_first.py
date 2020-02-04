import pytest
from depth_first import Graph 

def create_graph():
  graph = Graph()

  austin = graph.add('austin')
  boston = graph.add('boston')
  chicago = graph.add('chicago')
  detroit = graph.add('detroit')
  seattle = graph.add('seattle')
  sanFransisco = graph.add('sanfransisco')
  newOrleans = graph.add('neworleans')
  graph.add_double_edge(austin, boston)
  graph.add_double_edge(austin, detroit)
  graph.add_double_edge(boston, chicago)
  graph.add_double_edge(boston, detroit)
  graph.add_double_edge(chicago, newOrleans)
  graph.add_double_edge(detroit, seattle)
  graph.add_double_edge(detroit, sanFransisco)


  return (graph, austin)

def test_import():
  graph = Graph()
  assert graph.add_double_edge

def test_graph():
  graphOne = create_graph()
  graph = graphOne[0]
  root = graphOne[1]

  assert root.value == 'austin'
  assert graph.depth_first(root) == ['austin','boston','chicago','neworleans','detroit','seattle','sanfransisco']


def test_depth_first_single():
  graph = Graph()
  austin = graph.add('austin')
  assert graph.depth_first(austin) == ['austin']

def test_one_way_depth_first():
  graph = Graph()
  austin = graph.add('austin')
  boston = graph.add('boston')
  graph.add_edge(austin, boston)
  assert graph.depth_first(austin) == ['austin', 'boston']
  assert graph.depth_first(boston) == ['boston']

