'''Implementatiom of Depth-first EARCH IN Python, step by step'''

graph = {
    'Arad': ('Zerind','Sibiu', 'Timisoara'),
    'Zerind': ('Arad', 'Oradea'),
    'Sibiu': ('Arad', 'Fagaras', 'Rimniciu Vilcea'),
    'Timisoara': ('Arad', 'Lugoj'),
    'Oradea': (),
    'Lugoj': (),
    'Fagaras': ('Sibiu', 'Bucharest'),
    'Rimniciu Vilcea': ('Sibiu', 'Pitesti'),
    'Bucharest': ('Pitetsi', 'Fagaras'),
    'Pitesti': ('Rimniciu Vilcea', 'Bucharest')
}

stack  = ['Arad']
visited = {'Arad'}
parent = {'Arad': None}    # for keeping the track of goal path

goal = 'Bucharest'

while stack:
    
    node = stack.pop()
    if node == goal:
        print(node)
        break
    
    node_children = reversed(graph[node]) 
     
    for i in node_children:
        if i not in visited:
            visited.add(i)            # mark the node immediately
            parent[i] = node       
            stack.append(i)

