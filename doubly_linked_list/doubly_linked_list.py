"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
import gc
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete_list_node(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        gc.collect()
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def delete_node(self):
        self.head = None
        self.tail = None
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # Create instance of ListNode with value
        new_node = ListNode(value)

        # Increment the DLL Length Attribute
        self.length += 1

        # Check if DLL is empty
            # If it is empty: 
                # Set head and tail to the new node instance
        if self.head == None:
            self.head = new_node
            self.tail = new_node

            # If not:
                # Set new nodes next to current head
                # Set head's previous to new node
                # Set head to new node head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        """
        value = self.head.value
        self.delete(self.head)
        return value
        """
        # Store the Value of the Head
        removed = self.head.value
        # Decrement Length
        self.length -= 1
        # Delete the Head
        self.delete_node()

        # Return the Value
        return removed
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        """
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        """
        # Create instance of ListNode with value
        new_node = ListNode(value)

        # Increment the DLL Length Attribute
        self.length += 1

        # Check if DLL is empty
            # If it is empty: 
                # Set head and tail to the new node instance
        if self.head == None:
            self.head = new_node
            self.tail = new_node

        # If DLL is NOT empty:
            # Set new node's previous to the current tail
            # Set Tail's Next to new node
            # Set Tail to New node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        """
        value = self.tail.value
        self.delete(self.tail)
        return value
        """
        # Store the Value of the Tail
        removed = self.tail.value
        # Decrement Length
        self.length -= 1
        # Delete the Tail
        self.delete_node()
            # If current Tail's previous is not None
                # Set head node's next value to None
                # Set tail to current Head's next value
        # if removed.prev != None:
        #     head_node = removed.prev
        #     head_node.next = removed

        #     # Else if tail.prev is None
        #         # Set Head to None
        #         # Set Tail to None
        # else:
        #     removed = None
        #     self.head = None

        # Return the Value
        return removed
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete_list_node()
            self.length -= 1
        self.add_to_head(value)
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        if node is self.head:
            self.remove_from_head()
            self.add_to_tail(node.value)
        else:
            node.delete_list_node()
            self.length -= 1
            self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        """
        if not self.head and not self.tail:
            return
        self.length -= 1
        ## Checking if DLL is length of 1 ##
        if self.head is self.tail: ## is because checking reference
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        """
        node.delete_list_node()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max = None
        temp = None

        temp = max = self.head
        while temp != None:
            if temp.value > max.value:
                max = temp
            else:
                temp = temp.next
        return max.value

# python3 test_doubly_linked_list.py