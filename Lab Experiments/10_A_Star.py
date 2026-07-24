from queue import PriorityQueue

graph = {
    'A':[('B',1),('C',3)],
    'B':[('D',3),('E',6)],
    'C':[('F',5)],
    'D':[],
    'E':[('G',2)],
    'F':[('G',2)],
    'G':[]
}

heuristic = {
    'A':7,
    'B':6,
    'C':4,
    'D':3,
    'E':2,
    'F':1,
    'G':0
}

pq = PriorityQueue()
pq.put((0,'A'))

visited = set()

while not pq.empty():
    cost,node = pq.get()

    if node in visited:
        continue

    visited.add(node)

    print(node,end=" ")

    if node == 'G':
        break

    for neighbor,w in graph[node]:
        pq.put((cost+w+heuristic[neighbor],neighbor))
