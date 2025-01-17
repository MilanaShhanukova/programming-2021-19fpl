"""
Programming for linguists

Implementation of the data structure "Queue with stacks"
"""
from typing import Iterable
from math import inf
from stack.stack import Stack


class QueueStack(Stack):
    """
    Stack Data Structure
    """
    def __init__(self, data: Iterable = None, max_size=inf):
        super().__init__(data)
        self.data = self.data[::-1][:min(max_size, self.size())]
        self.max_size = max_size

    def push(self, element):
        """
        Add the element ‘element’ at the top of stack
        :param element: element to add to stack
        """
        assert self.max_size > self.size(), 'Too many elements in a queue.'
        self.data.insert(0, element)
