from collections import deque

def valid(m,c):
    return (m==0 or m>=c) and (3-m==0 or 3-m>=3-c)

def solve():
    start = (3,3,1)
    goal = (0,0,0)

    q = deque([(start,[])])

    visited = set()

    while q:
        state,path = q.popleft()

        if state == goal:
            print(path+[goal])
            return

        if state in visited:
            continue

        visited.add(state)

        m,c,b = state

        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

        for dm,dc in moves:
            if b:
                nm,nc = m-dm,c-dc
            else:
                nm,nc = m+dm,c+dc

            if 0<=nm<=3 and 0<=nc<=3 and valid(nm,nc):
                q.append(((nm,nc,1-b),path+[state]))

solve()
