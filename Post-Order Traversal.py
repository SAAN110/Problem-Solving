class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def post_order(root, nodes):
    if root is not None:
        post_order(root.left, nodes)        # Then left subtree
        post_order(root.right, nodes)       # Then right subtree
        nodes.append(root.data)            # Visit root first
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

print("Post Order Traversal is:",post_order(root,[]))
