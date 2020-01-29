import pytest
from get_edges import get_edge , Graph , Node_


def test_graph_edges_happy_feet(test_graph):
    set_list = ['naboo','pandora','narnia','oregon','pluto','saturn']

    assert get_edge(test_graph,set_list) == 'True : $2560'
    
def test_graph_empty():
    graph = Graph()
    set_list = ['1','2']

    assert get_edge(graph, set_list) == 'False : $0'

def test_flights_empty(test_graph):
    graph = test_graph
    set_list = []
    assert get_edge(graph, set_list) == 'False : $0'

def test_flight_none(test_graph):
    graph = test_graph
    set_list = ['naboo', 'pandora', 'earth']
    assert get_edge(graph, set_list) == 'False : $0'


def test_one_fligt(test_graph):
    set_list = ['naboo']

    assert get_edge(test_graph,set_list) == 'False : $0'    

def test_graph_without_edges():
    graph = Graph()
    set_list = ['naboo', 'pandora', 'narnia']
    graph.add_node('naboo')
    graph.add_node('pandora')
    graph.add_node('narnia')
    graph.add_node('oregon')
    graph.add_node('pluto')
    graph.add_node('saturn')

    assert get_edge(graph, set_list) == 'False : $0'


@pytest.fixture
def test_graph():
    graph = Graph()

    naboo = graph.add_node('naboo')
    pandora = graph.add_node('pandora')
    narnia = graph.add_node('narnia')
    oregon = graph.add_node('oregon')
    pluto = graph.add_node('pluto')
    saturn = graph.add_node('saturn')

    graph.add_edge(naboo, pandora, 150)
    graph.add_edge(pandora, naboo, 200)
    graph.add_edge(pandora, narnia, 350)
    graph.add_edge(pandora, saturn, 360)
    graph.add_edge(narnia, pandora, 370)
    graph.add_edge(narnia, saturn, 500)
    graph.add_edge(narnia, oregon, 550)
    graph.add_edge(saturn, pandora, 600)
    graph.add_edge(saturn, narnia, 650)
    graph.add_edge(saturn, oregon, 700)
    graph.add_edge(saturn, pluto, 710)
    graph.add_edge(oregon, narnia, 730)
    graph.add_edge(oregon, saturn, 740)
    graph.add_edge(oregon, pluto, 750)
    graph.add_edge(pluto, saturn, 760)
    graph.add_edge(pluto, oregon, 800)

    return graph