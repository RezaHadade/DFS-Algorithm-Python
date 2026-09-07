# Depth-First Search (DFS)

Depth-First Search (DFS) is an **uninformed search algorithm** that explores the state-space search tree by going as deep as possible along one branch before backtracking. In other words, it fully explores a path before trying an alternative one.

## LIFO Stack

To achieve this deep-first exploration, DFS uses a **LIFO (Last-In, First-Out)** data structure for its frontier.

In this implementation, the frontier is a plain Python `list`, where `append()` pushes a node and `pop()` removes the most recently added one.

The LIFO behavior of the stack ensures that the most recently generated node is expanded next, which is what allows DFS to plunge deep into one branch before backtracking to explore others.

## Goal Test

An important aspect of this implementation is the placement of the goal test.

Unlike BFS, DFS in this implementation performs the goal test when a node is **selected for expansion** (popped from the stack), not when it is generated. Children are still checked against the `visited` set before being pushed, to avoid redundant work, but the goal itself is only confirmed once a node reaches the top of the stack.

Before pushing a node's children, they are reversed. This keeps the traversal order consistent with the order children appear in the graph, since a stack would otherwise visit them in reverse.

## Path Reconstruction

If the goal is found, the `goal_path()` function can be used to reconstruct the path from the initial node to the goal node.

This is achieved by keeping track of the relationship between each node and its parent during the search, then walking back from the goal to the start via `parent` pointers and reversing the result.

## Properties

### Completeness

DFS is **not complete** in general. On an infinite or very deep search space, it can get stuck exploring one branch indefinitely and never find a goal that lies on a different branch.

In this implementation, the `visited` set prevents infinite loops on cyclic graphs, but DFS still offers no guarantee of finding a solution if one exists.

### Optimality

DFS is **not optimal**. It returns the first goal it happens to reach, regardless of depth, so the path found is not guaranteed to be the shortest one.

### Time Complexity

**O(b^m)**

Where:

- `b` = branching factor
- `m` = maximum depth of the search space

### Space Complexity

**O(bm)**

DFS only needs to store a single path from the root to the current node, along with the remaining siblings at each level. This is its main advantage over BFS, which must keep an exponential number of nodes in memory.

## Limitations

The biggest drawback of DFS is the lack of completeness and optimality.

Because DFS commits to a branch before knowing whether it leads anywhere useful, it can spend a long time exploring a deep, unproductive path while a shorter solution exists elsewhere in the tree.

For this reason, plain DFS is often unsuitable for problems where finding the shortest path matters, or where the search space contains very deep or infinite branches.

---

**In summary, DFS is memory-efficient thanks to its linear space complexity, but it is neither complete nor optimal, which limits its use in problems that require finding the best solution.**

## Example

```python
graph = {
    'Arad': ('Zerind', 'Sibiu', 'Timisoara'),
    'Zerind': (),
    'Timisoara': (),
    'Sibiu': ('Arad', 'Fagaras', 'Rimnicu Vilcea'),
    'Fagaras': ('Sibiu', 'Bucharest'),
    'Rimnicu Vilcea': ('Sibiu', 'Pitesti'),
    'Pitesti': ('Rimnicu Vilcea', 'Bucharest'),
    'Bucharest': ()
}

Start: Arad
Goal: Bucharest

Output:
Arad → Sibiu → Fagaras → Bucharest
```
