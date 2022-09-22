

graph = {
    'A': ['B', 'F', 'E'],
    'B': ['G', 'F'],
    'C' : ['D'],
    'D' : [],
    'E': ['F'],
    'F': [],
    'G': ['C', 'H'],
    'H' : ['D']
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph, neighbour)


print("Hasil penelusuran graf menggunakan DFS: ")
dfs(visited, graph, 'A')
