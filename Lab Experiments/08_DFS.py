graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)

        for i in graph[node]:
            dfs(i)

dfs('A')

print("DFS:",visited)
