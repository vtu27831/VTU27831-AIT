
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'D': 1},
    'D': {'G': 2},
    'E': {'G': 2},
    'G': {}
}
h = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 1,
    'G': 0
}
def a_star(start, goal):
    open_list = {start}
    closed_list = set()
    g = {start: 0}
    parents = {start: start}

    while open_list:
        n = min(open_list, key=lambda x: g[x] + h[x])

        if n == goal:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start)
            path.reverse()
            return path

        open_list.remove(n)
        closed_list.add(n)

        for m, cost in graph[n].items():
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + cost

            elif g[m] > g[n] + cost:
                g[m] = g[n] + cost
                parents[m] = n

                if m in closed_list:
                    closed_list.remove(m)
                    open_list.add(m)

    return None


path = a_star('A', 'G')
print("Optimal path:", path)

output:Optimal path: ['B', 'E', 'G']
