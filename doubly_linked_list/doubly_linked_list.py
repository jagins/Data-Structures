"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    def __str__(self):
        return f'{self.value}, {self.prev}, {self.next}'

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        #checking to see if the stack is empty
        if self.head == None:
           #if it's empyty create the new node and track it as the head
           self.head = ListNode(value)
        else:
            #if the stack has something in it create the new node
            new_node = ListNode(value)
            #set the new node next link to the current head
            new_node.next = self.head
            #set current head's previous link to the new node
            self.head.prev = new_node
            #change the head tracker to the new node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        #check if the stack is empty
        if self.head == None:
            return None
        else:
            #get a reference to the top of the stack
            popped_node = self.head
            #delete will reaarnge the links
            self.head.delete()
            return popped_node.value


    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # checks if the queue is empty and sets the head and tail to the same node
        if self.tail == None:
            self.tail = ListNode(value)
            self.head = self.tail
        else:
            #create the new node and set the new node's previous to the current tail and then move the pointer to the newly creted node
            new_node = ListNode(value)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail == None:
            return None
        else:
            popped_node = self.tail
            self.tail.delete()
            return popped_node

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        temp = self.head
        while temp.next is not None:
            print(temp)
            if temp == node:
                popped_node = temp
                temp.delete()
                return popped_node
            else:
                temp.next
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        temp = self.head
        largest_number = temp.value
        # print(temp.next.value)
        while temp.next is not None:
            if temp.next.value > largest_number:
                largest_number = temp.next.value
            else:
                temp = temp.next
        return largest_number  
    def __str__(self):
        return f'{self.head.value}'

test = DoublyLinkedList()
test.add_to_tail(1)
test.add_to_tail(20000)
test.add_to_tail(3)
test.add_to_tail(100)
test.add_to_tail(4)
test.add_to_tail(500)

number = test.get_max()
print(number)