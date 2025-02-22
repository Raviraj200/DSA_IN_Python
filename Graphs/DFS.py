def DFS(graph,start):
    stack = [start]
    visited=set()

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            stack.extend(graph[node]-visited)
graph={
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F', 'G'},
    'D': {'B'},
    'E': {'B', 'H'},
    'F': {'C'},
    'G': {'C'},
    'H': {'E'} 
}
DFS(graph,'A')