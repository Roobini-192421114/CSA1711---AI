from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    q = deque([(0,0)])

    while q:
        x, y = q.popleft()

        if (x,y) in visited:
            continue

        visited.add((x,y))
        print((x,y))

        if x == target or y == target:
            print("Target Reached")
            return

        q.extend([
            (jug1,y),
            (x,jug2),
            (0,y),
            (x,0),
            (min(jug1,x+y), y-(min(jug1,x+y)-x)),
            (x-(min(jug2,x+y)-y), min(jug2,x+y))
        ])

water_jug(4,3,2)
