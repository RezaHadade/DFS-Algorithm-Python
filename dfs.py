'''Depth-first Search'''

class Node:
    def __init__(self, state, parent, depth):
        self.state = state
        self.parent = parent
        self.depth = depth


def expand(graph, node):   
    children = graph.get(node.state, [])
    children_nodes = []
    
    for child in children:
        child_node = Node(child, node, node.depth+1)
        children_nodes.append(child_node)
    
    return children_nodes


def goal_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]
 

def DFS(graph, start, goal):    
    stack = []                                      # LIFO frontier queue: push = append() , pop = pop()
    visited = set()                                 # Prevent redundant exploration        
    
    stack.append(Node(start, None, 0))
    visited.add(start)           

    while stack:
        node = stack.pop()
        
        if node.state == goal:                  # Goal test at expansion time
            return goal_path(node)
            
        children = expand(graph, node)
        children.reverse()
        
        for child in children:
            if child.state not in visited:
                visited.add(child.state)        # Mark as visisted when the node generates 
                stack.append(child)
    
    return 'Failure'