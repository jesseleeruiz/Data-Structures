"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    """
    Case 1 - Value is less than self.value
        If there is no left child, insert value here

        Else
            Repeat the process on left subtree
            self.left.insert(value)

    Case 2 - Value is greater than or equal self.value
    """

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: if self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: if target is less than self.value
        if target < self.value:
            # If self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Ignore the left side completely
        # Keep going down until you hit a None value
            # When that right value has a None that value is the highest
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)
        # node_values = [self.value]
        # if not self.right is None:
        #     node_values.append(self.right)
        #     return self.right.for_each(fn)
        # elif not self.left is None:
        #     node_values.append(self.left)
        #     return self.left.for_each(fn)
        # else:
        #     return node_values
        # return node_values

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is not None:
            node.in_order_print(node.left)
            print(node.value)
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # Uses a Queue
    def bft_print(self, node):
        if node is None:
            return
        queue = []
        queue.append(node)
        
        while(len(queue) > 0):
            print(queue[0].value)
            pop_node = queue.pop(0)

            if pop_node.left is not None:
                queue.append(pop_node.left)

            if pop_node.right is not None:
                queue.append(pop_node.right)

            # if node.left is None and node.right is None:
            #     queue = 0

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # Uses a Stack
    def dft_print(self, node):
        if node is None:
            return
        stack = []
        stack.append(node)
        
        while(len(stack) > 0):
            pop_node = stack.pop()
            print(pop_node.value)

            if pop_node.left is not None:
                stack.append(pop_node.left)

            if pop_node.right is not None:
                stack.append(pop_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            node.pre_order_dft(node.left)
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            node.post_order_dft(node.left)
            node.post_order_dft(node.right)
            print(node.value)
