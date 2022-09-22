import queue


graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : ['H'],
    'G' : ['H'],
    'H' : ['G']
}

visited = []    #List to keep track of visited nodes
queue = []      #Initialize a queue

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s,end = " ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
        
        #coba print isi v
        print("\nvisited: ")
        for v in visited:
            print(v, end=" ")
        print("\n")

        #coba print queue 
        print("queue: ")
        for q in queue:
            print(q, end=" ")
        print("\n")
        

print("Hasil penelusuran graf menggunakan BFS:")
bfs(visited, graph, 'A')