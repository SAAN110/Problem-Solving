class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

  def in_order(root, nodes):
    if root is not None:
        in_order(root.left, nodes)        # Then left subtree
        nodes.append(root.data)            # Visit root first
        in_order(root.right, nodes)       # Then right subtree
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

print("In Order Traversal is:",in_order(root,[]))
