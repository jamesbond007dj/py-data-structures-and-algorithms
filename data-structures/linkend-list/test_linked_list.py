from linked_list import LinkedList

def test_insert():
    ll = LinkedList()
    ll.insert(2)
    expected = '2'
    actual = ll.to_string()
    assert actual == expected

def test_include_empty():
    ll =  LinkedList()
    expected = False
    actual = ll.includes(1)
    assert actual == expected

def test_include_true():
    ll =  LinkedList()
    ll.insert(1)
    expected = True
    actual = ll.includes(1)
    assert actual == expected

def test_include_false():
    ll =  LinkedList()
    ll.insert(1)
    expected = False
    actual = ll.includes(2)
    assert actual == expected

def test_include_three_true():
    ll =  LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    expected = True
    actual = ll.includes(2)
    assert actual == expected

def test_to_string():
    ll =  LinkedList()
    ll.insert(1)
    expected = '1'
    actual = ll.to_string()
    assert actual == expected

def test_to_string_empty():
    ll = LinkedList()
    expected = ''
    actual = ll.to_string()
    assert actual == expected

def test_to_string_two():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    expected = '2 1'
    actual = ll.to_string()
    assert actual == expected