'''
Less convoluted graph implementation.
Using the example in the chapter
'''

# importing queue data struture
from collections import deque


# initialize hashmap to store nodes and vertices
graph = {}

# populate graph with nodes as key and their neighbors (array) as values

graph['you'] = ['claire', 'bob', 'alice']
graph['claire'] = ['thom', 'johnny']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['thom'] = []
graph['johnny'] = []
graph['anuj'] = []
graph['peggy'] = []

def is_mango_seller(person: str) -> bool:
    # Check if person is thom (hes the only mango seller)
    if (person == 'thom'):
        return True
    return False

# implement bfs to find mango seller
def bfs_mango(start_node: str, graph: dict) -> str:
    # initialize queue for nodes to check
    check_queue = deque()
    # initialze set to store checked nodes
    checked_nodes = set()
    # add start node to check queue
    person = start_node
    # adding single string to queue (must use append instead of += operator)
    check_queue.append(person)

    # initialize output string for printing searched nodes
    out_str = ''

    # as long as the check queue is not empty, check for mango seller
    while check_queue:
        # pop current person from front of queue
        person = check_queue.popleft()
        # check if person has been checked. if they have, move onto the next person in the queue
        if person in checked_nodes:
            continue
        # check if current person a mango seller. if they are, the search has been completed!
        if is_mango_seller(person):
            # add person to output string
            out_str+= f' {person}'
            # print list of searched nodes
            print(out_str)
            print(f'{person} is the mango seller! 🥭')
            return person
        # add person to output string
        out_str+= f'{person} -> '
        # the current person is not a mango seller, add their neighbors to the queue. 
        # use the += operator to add an array as individual elements to the queue
        check_queue += graph[person]
        # mark the current person as checked
        checked_nodes.add(person)
    # print list of searched nodes
    print(out_str)
    # entire queue of people have been checked, the mango seller hasn't been found
    print('No mango seller found 😥')
    # Return an empty string
    return ''
        
print(bfs_mango('you', graph))



