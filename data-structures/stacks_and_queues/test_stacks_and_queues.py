from stacks_and_queues import Node, Stack, Queue
import pytest


"""
Below test edge situation
push function inserts argument when stack is empty
"""
def test_push_to_empty():
    st = Stack()
    st.push(8)
    assert "8" == str(st)

"""
Below test happy feet
function pops integer argument
"""
def test_pop():
    st = Stack()
    values = [1,2,3,8]
    for el in values:
        st.push(el)
    actual = st.pop()
    assert 8 == actual

"""
Below test happy feet
function pops string argument
"""
def test_pop_string():
    st = Stack()
    values = ['1','2','3','8']
    for el in values:
        st.push(el)
    actual = st.pop()
    assert '8' == actual


"""
Below test edge situation
you can not pop any argument when stack is empty
"""
def test_pop_empty():
    st = Stack()
    assert None == st.pop()


"""
Below test Stuck is not empty and is_empty function confirms it by Booleen False
"""
def test_is_empty_not_empty():
    st = Stack()
    values = [1,2,3,8]
    for el in values:
        st.push(el)
    actual = st.is_empty()
    assert False == actual

"""
Below test Stuck is empty and is_empty function confirms it by Booleen True
"""
def test_is_empty_really_empty():
    st = Stack()
    values = []
    for el in values:
        st.push(el)
    actual = st.is_empty()
    assert True == actual


"""
Below test edge situation
push function inserts argument when Queue is empty
"""
def test_enqueue_to_empty():
    q = Queue()
    q.enqueue(8)
    assert "8" == str(q)


"""
Below test happy feet
function peek integer argument
"""
def test_peek():
    q = Queue()
    values = [1,2,3,8]
    for el in values:
        q.enqueue(el)
    expected = 3
    actual = q.peek()
    assert expected == actual

"""
Below test Queue is not empty and is_empty function confirms it by Booleen False
"""
def test_is_empty_not_empty_Queue():
    q = Queue()
    values = [1,2,3,8]
    for el in values:
        q.enqueue(el)
    actual = q.is_empty_queue()
    assert False == actual

"""
Below test Queue is empty and is_empty function confirms it by Booleen True
"""
def test_is_empty_really_empty_Queue():
    q = Queue()
    values = []
    for el in values:
        q.push(el)
    actual = q.is_empty_queue()
    assert True == actual