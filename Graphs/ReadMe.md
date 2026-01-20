# Graphs – Complete Revision Notes (FAANG / NeetCode 150)

These notes are designed to take you **from scratch to FAANG interview-ready** for graph problems. They align closely with **NeetCode 150 – Graph section**, with added tricks, patterns, and Python templates.

---

## 1. What is a Graph?

A **graph** is a collection of:

* **Vertices (nodes)**
* **Edges (connections between nodes)**

### Types of Graphs

| Type         | Description                  |
| ------------ | ---------------------------- |
| Undirected   | Edge works both ways (u ↔ v) |
| Directed     | Edge works one way (u → v)   |
| Weighted     | Edge has a cost/weight       |
| Unweighted   | All edges equal              |
| Cyclic       | Contains a cycle             |
| Acyclic      | No cycles                    |
| Connected    | Every node reachable         |
| Disconnected | Some nodes isolated          |
| DAG          | Directed Acyclic Graph       |

---

## 2. Graph Representations

### 2.1 Adjacency List (Most Common)

```python
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: []
}
```

Or using list of lists:

```python
graph = [[1,2], [2], [0,3], []]
```

**Why preferred?**

* Space efficient: O(V + E)
* Fast iteration over neighbors

---

### 2.2 Adjacency Matrix

```python
matrix = [
  [0,1,1,0],
  [0,0,1,0],
  [1,0,0,1],
  [0,0,0,0]
]
```

* Space: O(V²)
* Rare in interviews unless V is very small

---

## 3. Core Traversals (MOST IMPORTANT)

### 3.1 Depth First Search (DFS)

Used for:

* Cycle detection
* Connected components
* Topological sort
* Backtracking on graphs

#### Recursive DFS

```python
def dfs(node):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei)
```

#### Iterative DFS

```python
stack = [start]
visited = set()

while stack:
    node = stack.pop()
    if node in visited:
        continue
    visited.add(node)
    for nei in graph[node]:
        stack.append(nei)
```

---

### 3.2 Breadth First Search (BFS)

Used for:

* Shortest path in **unweighted** graph
* Level order traversal
* Multi-source problems

```python
from collections import deque

queue = deque([start])
visited = set([start])

while queue:
    node = queue.popleft()
    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            queue.append(nei)
```

**Key Trick**: BFS guarantees shortest path (edges = 1 cost)

---

## 4. Connected Components

### Undirected Graph

Count how many groups exist.

```python
count = 0
visited = set()

for node in range(n):
    if node not in visited:
        dfs(node)
        count += 1
```

**Appears in:**

* Number of Provinces
* Number of Islands

---

## 5. Cycle Detection

### 5.1 Undirected Graph

Use **parent tracking**.

```python
def hasCycle(node, parent):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            if hasCycle(nei, node):
                return True
        elif nei != parent:
            return True
    return False
```

---

### 5.2 Directed Graph

Use **3-state DFS**:

* 0 = unvisited
* 1 = visiting (in recursion stack)
* 2 = visited

```python
def dfs(node):
    if state[node] == 1:
        return True
    if state[node] == 2:
        return False

    state[node] = 1
    for nei in graph[node]:
        if dfs(nei):
            return True
    state[node] = 2
    return False
```

**Used in:**

* Course Schedule
* Detect cycle in directed graph

---

## 6. Topological Sort (DAG)

### 6.1 DFS Based

```python
def dfs(node):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei)
    stack.append(node)
```

Reverse stack for topo order.

---

### 6.2 Kahn’s Algorithm (BFS)

```python
from collections import deque

indegree = [0]*n
for u in graph:
    for v in graph[u]:
        indegree[v] += 1

queue = deque([i for i in range(n) if indegree[i] == 0])
res = []

while queue:
    node = queue.popleft()
    res.append(node)
    for nei in graph[node]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            queue.append(nei)
```

**If res size < n → cycle exists**

---

## 7. Shortest Path Algorithms

### 7.1 BFS (Unweighted)

Already covered

---

### 7.2 Dijkstra (Weighted, no negative edges)

```python
import heapq

def dijkstra(start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for nei, w in graph[node]:
            if dist[nei] > d + w:
                dist[nei] = d + w
                heapq.heappush(pq, (dist[nei], nei))
    return dist
```

**Used in:**

* Network Delay Time
* Cheapest Flights

---

## 8. Union Find (Disjoint Set)

Used for **connectivity + cycle detection**.

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa
        self.parent[pb] = pa
        self.rank[pa] += self.rank[pb]
        return True
```

**Used in:**

* Redundant Connection
* Kruskal MST

---

## 9. Grid as Graph (VERY COMMON)

### Direction Array

```python
dirs = [(1,0), (-1,0), (0,1), (0,-1)]
```

### Islands Template

```python
def dfs(r, c):
    if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == '0':
        return
    grid[r][c] = '0'
    for dr, dc in dirs:
        dfs(r+dr, c+dc)
```

Used in:

* Number of Islands
* Flood Fill
* Rotting Oranges

---

## 10. Graph Coloring / Bipartite

```python
color = {}

def dfs(node, c):
    color[node] = c
    for nei in graph[node]:
        if nei not in color:
            if not dfs(nei, 1-c): return False
        elif color[nei] == c:
            return False
    return True
```

**Used in:**

* Is Graph Bipartite

---

## 11. NeetCode 150 – Must Do Graph Problems

### Core

* Number of Islands
* Clone Graph
* Max Area of Island
* Pacific Atlantic Water Flow

### DAG / Topo

* Course Schedule I & II
* Alien Dictionary

### Shortest Path

* Network Delay Time
* Cheapest Flights Within K Stops

### Advanced

* Word Ladder
* Evaluate Division
* Accounts Merge

---

## 12. FAANG Interview Tricks

* Always clarify **directed vs undirected**
* Ask about **negative weights**
* Use BFS if shortest path & no weights
* Use DFS for detection & traversal
* Grid = graph (most candidates miss this)
* Say time complexity clearly

---

## 13. Final Mental Checklist

* Graph type?
* Traversal needed?
* Visited handling correct?
* Cycle possible?
* BFS vs DFS?
* Extra data structure needed?

---
