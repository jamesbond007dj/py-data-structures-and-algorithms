from stacks_and_queues import Node, Stack, Queue
import pytest

"""
Below test happy feet
function push  argument
"""
def test_push():
    st = Stack()
    values = [1,2,3,8]
    for el in values:
        st.push(el)
    actual = st.push(6)
    assert "68321" == str(actual)

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
Below test happy feet
kth node value shown
"""
def test_peek():
    st = Stack()
    values = [1,2,3,8]
    for el in values:
        st.push(el)
    actual = st.peek(3)
    assert 8 == actual

"""
Below test happy feet
kth node value shown
"""
def test_peek_2():
    st = Stack()
    values = [1,2,3,8]
    for el in values:
        st.push(el)
    actual = st.peek(1)
    assert 2 == actual
"""
Below test happy feet
kth node value shown
"""
def test_peek_3():
    st = Stack()
    values = [1,2,3,8]
    for el in values:
        st.push(el)
    actual = st.peek(0)
    assert 1 == actual

"""
Below test edge situation
kth node value if k is negative number 
then even can not ask to top, so it is no value
"""
def test_peek_negative():
    st = Stack()
    values = [1,2,3,8]
    for el in values:
        st.push(el)
    actual = st.peek(-1)
    assert 'Negative k has no value' == actual

"""
Below test edge situation
kth node value if k is bigger than Stack len, 
can not fined value so says no value
"""
def test_peek_bigger__than_len():
    st = Stack()
    values = [1,2,3,8]
    for el in values:
        st.push(el)
    actual = st.peek(4)
    assert 'No value' == actual
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
Below test happy feet
function adds argument to rear of queue
"""
def test_enqueue():
    q = Queue()
    values = [1,2,3,8]
    for el in values:
        q.enqueue(el)
    actual = q.enqueue(6)
    assert "68321" == actual

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
function pops integer argument
"""
def test_dequeue():
    q = Queue()
    values = [1,2,3,8]
    for el in values:
        q.enqueue(el)
    actual = q.dequeue()
    assert 1 == actual.value
"""
Below test happy feet
function peek integer argument
"""
def test_peek():
    q = Queue()
    values = [1,2,3,8]
    for el in values:
        q.enqueue(el)
    actual = q.peek()
    assert 3 == actual.value

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