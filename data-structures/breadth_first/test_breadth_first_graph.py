import pytest
from breadth_first_graph import Graph , Node_

    
def test_no_edges():
    graph = Graph()

    naboo = graph.add_node('naboo')

    assert graph.breadth_first(naboo) == {naboo}


@pytest.mark.skip('pending')
def test_flight_none(test_graph):
    graph = test_graph
    set_list = ['naboo', 'pandora', 'earth']
    assert graph.breadth_first('earth') == 'earth is not in graph'

@pytest.mark.skip('pending')
def test_breadth_first():
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

    assert graph.breadth_first(naboo) == {naboo, oregon, pluto, narnia, saturn, pandora}

