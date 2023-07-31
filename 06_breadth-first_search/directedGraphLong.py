# Directed Graph
# CONVOLUTED EXAMPLE #1

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
    
    def _addChildNode(self, node):
        self.children.append(node)

    def addChildren(self, nodes) -> None:
        for node in nodes:
            self._addChildNode(node)
    
    def __str__(self): 
        return self.value
    
# graph.add_edge(1, 2)
# graph.add_edge(1, 3)
# graph.add_edge(2, 4)
# graph.add_edge(2, 5)
# graph.add_edge(3, 6)
# graph.add_edge(3, 7)


one = Node('1')
two = Node('2')
three = Node('3')
four = Node('4')
five = Node('5')
six = Node('6')
seven = Node('7')

one.addChildren([two, three])
two.addChildren([four, five])
three.addChildren([six, seven])


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

# # Initialize nodes and their values
# cab_node = Node('cab')
# car_node = Node('car')
# cat_node = Node('cat')
# mat_node = Node('mat')
# bar_node = Node('bar')
# bat_node = Node('bat')

# # Create relationships
# cab_node.addChildren([cat_node, car_node])
# car_node.addChildren([bar_node, cat_node])
# cat_node.addChildren([bat_node, mat_node])
# bar_node.addChildren([bat_node])
# mat_node.addChildren([bat_node])


# # Initialize nodes and their values
# you_node = Node('you')
# bob_node = Node('bob')
# alice_node = Node('alice')
# claire_node = Node('claire')
# anuj_node = Node('anuj')
# peggy_node = Node('peggy')
# thom_node = Node('thom')
# johnny_node = Node('johnny')


# # Create relationships
# you_node.addChildren([alice_node, bob_node, claire_node])

# bob_node.addChildren([anuj_node, peggy_node])

# alice_node.addChildren([peggy_node])

# claire_node.addChildren([thom_node, johnny_node])

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
    def __init__(self, nodes: [Node]):
        self.nodes = nodes

        # Build graph
        self.graph = {}
        for node in self.nodes:
            self.graph[node] = node.children
    
    def isChild(self, node1: Node, node2: Node):
        return node1 in node2.children
    
    
    def stringifyNodes(self, nodes: any):
        out_str = ''
        for node in nodes:
            out_str+=f'[{node.value}]'
        return out_str
    
    def bfs(self, start_node: Node, end_node: Node) -> int:
        '''
        Performs the breadth first search algorithm to find the shortest path between two points in a graph
        '''

        check_queue = deque()
        num_steps = 0

        out_str = ''

        # edge case. start is same as end
        if start_node == end_node:
            return num_steps
        
        check_queue.append(start_node)
        
        # keep track of people checked
        checked = set()

        while len(check_queue) > 0:

            print(self.stringifyNodes(check_queue))
            # get current node to check from queue (FIFO)
            current_node = check_queue.popleft()

            #skip if node has beenchecked
            if current_node in checked:
                continue


            print(current_node)

            # check if we find end, return number of steps
            if end_node==current_node:
                out_str+= f'{current_node.value}'
                print(out_str)
                return num_steps
            
            # add current node to checked set
            checked.add(current_node)
            # didnt find end, add children of current node to queue. Use += to append list items as single items in qeue
            check_queue+=current_node.children

            num_steps += 1
            out_str += f'{current_node.value} -> '
        
        print(end_node.value, 'NOT FOUND!')
        # end_node not found, return -1
        return -1
        

    def __str__(self):
        # Print adjacency list
        output = ''
        for node in self.nodes:
            output+=f'\n {node} ->'
            for child in node.children:
                output+=f' {child}'
        
        return output   
        

# graph = DirectedGraph([you_node, bob_node, alice_node, claire_node, anuj_node, peggy_node, thom_node])
# print(graph.bfs(you_node, johnny_node))
# graph = DirectedGraph([cab_node, car_node, cat_node, bar_node, mat_node, bat_node])
# print(graph.bfs(cab_node, bat_node))
graph = DirectedGraph([one, two, three])
print(graph.bfs(one, seven))


'''
todo: 
[X] fix str output. change to match this: https://www.techiedelight.com/graph-implementation-python/
[X] remove start and end
[X] create graph building functinality
[X] implement addCHildren()
[X] fix print output (book example)
[X] implement BFS
[] refactor node class
'''




