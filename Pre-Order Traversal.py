class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def pre_order(root, nodes):
  if root is not None:
    nodes.append(root.data)            # Visit root first
    pre_order(root.left, nodes)        # Then left subtree
    pre_order(root.right, nodes)       # Then right subtree
return nodes

root = Node('A')  
n1 = Node('B')    
n2 = Node('C')    
n3 = Node('D')    
n4 = Node('E')

root.left=n1
root.right=n2
n1.left=n3
n1.right=n4
print("Pre Order Traversal is:",pre_order(root,[]))
