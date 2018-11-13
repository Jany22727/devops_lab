

# input logo
s = input("Type logo with 3 different repeating letters: ")

# inicialize list, (results)
res = []

for i in sorted(set(s)):
    res.append((i, s.count(i)))

res.sort(key=lambda x: x[1], reverse=True)

print(res[0][0], res[0][1])
print(res[1][0], res[1][1])
print(res[2][0], res[2][1])
