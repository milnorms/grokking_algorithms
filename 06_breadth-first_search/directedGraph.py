# Directed Graph

from collections import deque

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
    def __init__(self, value: str):
        self.value = value
        self.children = []
        self.parents = []

        
    def _addParentNode_(self, node):
        self.parents.append(node)
    
    def _addChildNode(self, node):
        node._addParentNode_(self)
        self.children.append(node)

    def addChildren(self, nodes):
        pass
    
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
you_node = Node('you')
bob_node = Node('bob')
alice_node = Node('alice')
claire_node = Node('claire')
anuj_node = Node('anuj')
peggy_node = Node('peggy')
thom_node = Node('thom')
johnny_node = Node('johnny')


# Create relationships
you_node.addChildNode(alice_node)
you_node.addChildNode(bob_node)
you_node.addChildNode(claire_node)

bob_node.addChildNode(anuj_node)
bob_node.addChildNode

'''
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
'''


class DirectedGraph:
    def __init__(self, nodes: List[Node]):
        self.nodes = nodes

        # Build graph
        self.graph = {}
        for node in self.nodes:
            self.graph[node] = node.children

    def isParent(self, node1: Node, node2: Node):
        return node1 in node2.parents
    
    def isChild(self, node1: Node, node2: Node):
        return node1 in node2.children
        
    def areConnected(self, node1: Node, node2: Node):
        return self.isParent(node1, node2) or self.isParent(node2, node1) or self.isChild(node1, node2) or self.isChild(node2, node1)
    
    def bfs(self, start_node: Node, end_node: Node) -> int:
        '''
        Performs the breadth first search algorithm to find the shortest path between two points in a graph
        '''

        check_queue = deque()
        num_steps = 0

        # edge case. start is same as end
        if start_node == end_node:
            return num_steps
        
        check_queue+=start_node

        while len(check_queue) > 0:
            print(start_node)
            num_steps += 1
            # get current node to check from queue (FIFO)
            current_node = check_queue.popleft()

            # check if we find end, return number of steps
            if end_node in self.graph[current_node]:
                return num_steps
            
            # didnt find end, add children of current node to queue
            check_queue+=current_node.children
        
        return num_steps
        

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
print(graph.bfs(a, e))

'''
todo: 
[X] fix str output. change to match this: https://www.techiedelight.com/graph-implementation-python/
[X] remove start and end
[X] create graph building functinality
[] implement addCHildren()
[] implement BFS
'''




