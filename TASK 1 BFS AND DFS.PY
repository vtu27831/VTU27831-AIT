#BFS
graph = {
    'A': ['B','C'],
    'B':[ ],
    'C':[ ]
}
visited = [ ]
queue = ['A']
while queue:
  node = queue.pop(0)
  if node not in visited:
    print(node,end=" ")
    visited.append(node)
    queue.extend(graph[node])
OUTPUT:A B C

#DFS
graph = {
    'A': ['B','C'],
    'B':[],
    'C':[]
}
visited = []

def dfs (node):
  if node not in visited:
    print(node,end=" ")
    visited.append(node)
    for i in graph[node]:
      dfs(i)

dfs('A')

OUTPUT:A B C
