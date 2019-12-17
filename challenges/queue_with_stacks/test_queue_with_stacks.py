import pytest
from queue_with_stacks import PseudoQueue, Node, Stack

"""
connection test
"""
def test_queue():
  assert PseudoQueue()


"""
happy feet test
"""
def test_value():
  queue = PseudoQueue()
  queue.enqueue(2)
  expected = 2
  actual = queue.dequeue()
  assert expected == actual

