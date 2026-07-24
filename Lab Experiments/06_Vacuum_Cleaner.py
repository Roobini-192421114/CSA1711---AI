rooms = {'A':'Dirty','B':'Dirty'}

location = 'A'

while True:
    if rooms[location] == 'Dirty':
        print("Cleaning",location)
        rooms[location] = 'Clean'
    else:
        print(location,"already clean")

    if location == 'A':
        location = 'B'
    else:
        break

print(rooms)
