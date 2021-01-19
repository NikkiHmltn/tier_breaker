import math, random

class Node:
    """ Binary tree node  """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_branches(self,left_value, right_value):
        """ Add both branches to node, with given values """
        self.left = left_value
        self.right = right_value

    def __str__(self):
        return f"value: {self.value}, \nright: [ {self.right} ],\n left: [ {self.left} ]"


class BinaryTree: 
    """ Bracket Binary Tree """
    def __init__(self):
        self.root = None

    def make_bracket(self, base_nodes):
        """ SET UP STEP: Create bracket tree, calls build_levels and add_values """
        # base_nodes is the number of first round options 
        # calculate rounds / tree levels
        levels = int(math.log2(len(base_nodes))) 
        # set up empty tree 
        self.root = Node(None)
        self.build_levels(levels, self.root)
        self.add_values(self.root, base_nodes)
            
    def build_levels(self, levels, root):
        """ SET UP STEP: Create balanced tree with appropriate number of nodes, Initializes all values as empty """
        if levels == 0: return 
        root.right = Node(None)
        root.left = Node(None)
        self.build_levels(levels-1, root.right)
        self.build_levels(levels-1, root.left)

    def add_values(self, root, values):
        """ SET UP STEP: Fill bottom 'row' of nodes with initial values """
        # values will always be even length, by the return 
        length = len(values)
        # all nodes have a left and a right except for the bottom "row"
        if not root.left: 
            if length != 1: raise ValueError('values develop faulty tree')
            root.value = values[0]
            return
        else:
            self.add_values(root.left, values[:length // 2])
            self.add_values(root.right, values[length // 2:])

    def set_winner(self, root):
        """ Bounce child node value with greater votes up a level """
        # every node.value is in the format { "option": "option_name", "votes": vote_count}
        if root.left.value and root.right.value :
            if root.left.value["votes"] > root.right.value["votes"]: root.value = root.left.value
            elif root.right.value["votes"] > root.left.value["votes"]: root.value = root.right.value
            else: # in case of tie, randomly pick one FOR NOW
                random.seed()
                root.value = [root.left.value, root.right.value][random.randint(0,1)]
        else: 
            self.set_winner(root.left)
            self.set_winner(root.right)


    def level_order_print(self, root):
        """ Breadth first transversal, returns array of values starting at the root """
        values = [root.value]
        nodes = [root]
        temp_node = root
        while len(nodes) > 0:
            temp_node = nodes[0]
            if temp_node.left:
                nodes = nodes + [temp_node.left, temp_node.right]
                values = values + [temp_node.left.value, temp_node.right.value]
            nodes.pop(0)
        return values


tree = BinaryTree()

options = [
    {"option": 1, "votes": 1},
    {"option": 2, "votes": 2},
    {"option": 3, "votes": 3},
    {"option": 4, "votes": 4},
    {"option": 5, "votes": 5},
    {"option": 6, "votes": 6},
    {"option": 7, "votes": 7},
    {"option": 8, "votes": 8},
]

tree.make_bracket(options)
print(tree.level_order_print(tree.root))
tree.set_winner(tree.root)
print(tree.level_order_print(tree.root))
tree.set_winner(tree.root)
print(tree.level_order_print(tree.root))
tree.set_winner(tree.root)
print(tree.level_order_print(tree.root))
 