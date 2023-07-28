# Directed Graph

'''
    Graph traversal
    Add components (nodes, edges) to the graph
    Find the shortest path from a node to another
    Find the path with the lower weight between two nodes
    Check if a node exists in a graph
    
    Adjacency matrix: https://www.programiz.com/dsa/graph-adjacency-matrix
    Adjacency List: https://www.programiz.com/dsa/graph-adjacency-list
    BFS: https://www.programiz.com/dsa/graph-bfs
'''

class Node:
    def __init__(self, value, isStart:bool=False):
        # Cast node value to string
        self.value = str(value)
        self.children = []
        self.parents = []
        self.isStart = isStart
        self.isEnd = True
        
    def _addParentNode_(self, node):
        self.parents.append(node)
    
    def addChildNode(self, node):
        self.isEnd = False
        node._addParentNode_(self)
        self.children.append(node)
    
    def __str__(self): 
        return self.value
    
# # Initialize nodes and their values
# a = Node('a', isStart=True)
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')

# # Create relationships
# a.addChildNode(b)
# a.addChildNode(c)

# b.addChildNode(c)
# b.addChildNode(d)
# b.addChildNode(e)

# c.addChildNode(e)

# d.addChildNode(f)

# e.addChildNode(d)
# e.addChildNode(f)

# Initialize nodes and their values
a = Node('a', isStart=True)
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')


# Create relationships
a.addChildNode(b)
a.addChildNode(c)

b.addChildNode(c)

c.addChildNode(b)
c.addChildNode(d)

d.addChildNode(e)


class DirectedGraph:
    def __init__(self, nodes: [Node]):
        self.nodes = nodes
    
    def isParent(self, node1: Node, node2: Node):
        return node1 in node2.parents
    
    def isChild(self, node1: Node, node2: Node):
        return node1 in node2.children
        
    def areConnected(self, node1: Node, node2: Node):
        return self.isParent(node1, node2) or self.isParent(node2, node1) or self.isChild(node1, node2) or self.isChild(node2, node1)
    
    def __str__(self):
        # Print adjacency list
        output = ''
        for node in self.nodes:
            output+=f'\n {node} ->'
            for child in node.children:
                output+=f' {child}'
        
        return output   
        
# graph = DirectedGraph([a, b, c, d, e, f])
graph = DirectedGraph([a, b, c, d, e])
print(graph)
print(b.parents)

'''
todo: 
[X] fix str output. change to match this: https://www.techiedelight.com/graph-implementation-python/
[X] accept any input as node but stringify in node class
[] implement DFS and DFS
'''




