"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

  def __str__(self):
      return f'{self.value},{self.next_node}'

class LinkedList:
    def __init__(self):
        # first node in the list 
        self.head = None

    def add_to_head(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node 
        new_node = Node(value)
        # what if the list is empty? 
        if not self.head:
            self.head = new_node
        # what if the list isn't empty?
        else:
            # what node do we want to add the new node to? 
            # the last node in the list 
            # we can get to the last node in the list by traversing it 
            current = self.head 
            current = current.set_next(current)
            # we're at the end of the linked list 
            self.head = new_node

   

    def getCount(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.get_next()
        return count

    def __str__(self):
        return f'{self.head}'
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size = self.storage.getCount()

    def pop(self):
        if self.size == 0:
            return None
        else:
            value = self.storage.pop(0)
            self.size = self.storage.getCount()
            return value

stack = Stack()
stack.push(4)
stack.push(5)
stack.push(6)
print(stack.storage)
