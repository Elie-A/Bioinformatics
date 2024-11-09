from collections import defaultdict

def parse_input(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        n = int(lines[0].strip())  # number of nodes
        edges = [tuple(map(int, line.strip().split())) for line in lines[1:]]
    return n, edges

def count_connected_components(n, edges):
    # Build the adjacency list for the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Function to perform DFS and mark nodes in the same component
    def dfs(node, visited):
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                stack.extend(graph[current])
    
    # Count connected components using DFS
    visited = set()
    components = 0
    for node in range(1, n + 1):
        if node not in visited:
            dfs(node, visited)
            components += 1
    
    return components