'''Implementatiom of Depth-first EARCH IN Python, step by step'''

graph = {
    'Arad': ('Zerind','Sibiu', 'Timisoara'),
    'Zerind': ('Arad', 'Oradea'),
    'Sibiu': ('Arad', 'Rimniciu Vilcea', 'Fagaras'),
    'Timisoara': ('Arad', 'Lugoj'),
    'Oradea': (),
    'Lugoj': (),
    'Fagaras': ('Sibiu', 'Bucharest'),
    'Rimniciu Vilcea': ('Sibiu', 'Pitesti'),
    'Bucharest': ('Pitesti', 'Fagaras'),
    'Pitesti': ('Rimniciu Vilcea', 'Bucharest')
}
start = 'Arad'
goal = 'Bucharest'


class Node:
    def __init__(self, state, parent, depth):
        self.state = state
        self.parent = parent
        self.depth = depth


def expand(graph, node):
     
    children = graph[node.state]
    children_nodes = []
    
    for child in children:
        child_node = Node(child, node, node.depth+1)
        children_nodes.append(child_node)
    
    return children_nodes


stack = []                                      # LIFO frontier queue: push = append() , pop = pop()
visited = set()                                 # Prevent redundant exploration
path = []                                       # Goal path

def DFS(graph, start, goal):    
        
    stack.append(Node(start, None, 0))
    visited.add(start)           

    while stack:
        node = stack.pop()
        
        if node.state == goal:                  # Goal test at expansion time
            return node
        children = expand(graph, node)
        children.reverse()
        
        for child in children:
            if child.state not in visited:
                visited.add(child.state)        # Mark as visisted when the node generates 
                stack.append(child)
    
    return 'Failure'