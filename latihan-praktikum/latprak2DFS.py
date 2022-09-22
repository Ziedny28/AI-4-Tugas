graph = {
    'A': ['B'],
    'B': ['G', 'F'],
    'C': ['D'],
    'D': ['H'],
    'E': ['F'],
    'F': ['E'],
    'G': ['C'],
    'H' : []
}


visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("Hasil penelusuran graf menggunakan DFS: ")
dfs(visited, graph, 'A')
