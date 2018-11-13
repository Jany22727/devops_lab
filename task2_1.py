

# initialize a list (number of command in programm)
L = []
# input commands
max = int(input("type number of command: "))
for i in range(0, max):
    inVal = input("type command: ").split()
# insert (position) (number)
    if inVal[0] == "insert":
        L.insert(int(inVal[1]), int(inVal[2]))
# if we edit in terminal not insert - print list
    elif inVal[0] == "print":
        print(L)
# remove  number from list (the first occurrence)
    elif inVal[0] == "remove":
        L.remove(int(inVal[1]))
# add a single element to the end of list
    elif inVal[0] == "append":
        L.append(int(inVal[1]))
# sort the list
    elif inVal[0] == "sort":
        L.sort()
# removes the last element of a list.
    elif inVal[0] == "pop":
        L.pop()
# reverse the list
    elif inVal[0] == "reverse":
        L.reverse()
        print(L)
# count the number of  occurrences
    elif inVal[0] == "count":
        c = L.count(int(inVal[1]))
        print(c)
# returns the first index of a value in the list
    elif inVal[0] == "index":
        t = L.index(int(inVal[1]))
        print(t)
