def dfs(graph, n, visited):
    print(n)
    visited.append(n)
    for n in graph[n]:
        if n not in visited:
            dfs(graph, n, visited)



