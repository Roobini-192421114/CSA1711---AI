from queue import PriorityQueue

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

def heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                h += 1
    return h

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def neighbors(state):
    x, y = find_zero(state)
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    result = []

    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            result.append(new_state)
    return result

def astar(start):
    pq = PriorityQueue()
    pq.put((heuristic(start), start))
    visited = []

    while not pq.empty():
        cost, state = pq.get()

        if state == goal:
            print("Goal Reached")
            for row in state:
                print(row)
            return

        visited.append(state)

        for n in neighbors(state):
            if n not in visited:
                pq.put((heuristic(n), n))

start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

astar(start)
