# Depth-First Search (DFS)

A Python implementation of Depth-First Search over a graph, using an explicit stack instead of recursion.

## What this is

This is my simple implementation of DFS on a graph represented as an adjacency list. It uses:

- A `Node` class that keeps track of `state`, `parent`, and `depth`, so I can reconstruct the path once the goal is found.
- An iterative, stack-based search (LIFO) instead of a recursive one.
- A `visited` set to avoid revisiting states and to prevent infinite loops on cyclic graphs.

## How it works

- **`Node`** — represents a single state in the search, along with a pointer to its parent and its depth.
- **`expand(graph, node)`** — returns the children of a node based on the graph. Uses `graph.get(node.state, [])` so nodes with no outgoing edges don't need to be explicitly listed in the graph dictionary.
- **`goal_path(node)`** — walks back from the goal node to the start using `parent` pointers, then reverses the result to get the path in the right order.
- **`DFS(graph, start, goal)`** — the main search:
  - Uses a list as a stack (`append`/`pop`).
  - Marks nodes as visited as soon as they're pushed, not when they're popped, to avoid pushing duplicates.
  - Reverses each node's children before pushing them, so traversal order matches the natural left-to-right order in the graph, despite the stack being LIFO.
  - Returns the path to the goal if one is found, or `None` if it isn't.

## Graph format

The graph is a dictionary mapping each state to a list of its neighbors:

```python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'E': ['F']
}
```

Leaf nodes don't need to be listed as keys.

## Usage

```python
from dfs import DFS

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'E': ['F']
}

path = DFS(graph, 'A', 'F')
print(path)  # ['A', 'B', 'E', 'F']
```

If no path exists, `DFS` returns `None`.

## Possible next steps

- Depth-limited search (the `depth` field is already tracked, just not used for control flow yet).
- Iterative deepening DFS.
- Comparing against BFS or other search strategies on the same graphs.
