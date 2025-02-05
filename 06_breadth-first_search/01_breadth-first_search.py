from collections import deque

def person_is_seller(name):
      return name[-1] == 'm'

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    out_str = ''
    search_queue = deque()
    search_queue += [name]
    # This is how you keep track of which people you've searched before.
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        print(person)
        # Only search this person if you haven't already searched them.
        if person in searched:
            continue
        if person_is_seller(person):
            out_str+= f' {person}'
            print(out_str)
            print(person + " is a mango seller!")
            return True
        out_str+= f'{person} -> '
        search_queue += graph[person]
        # Marks this person as searched
        searched.add(person)
    print(out_str)
    return False

search("you")
