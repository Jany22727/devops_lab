

N = int(input("number homes: "))
per = []

if N > 0 and N <= 100:
    for i in range(N):
        V, S = map(int, input(
                  "Type years old, and who is it (1-man, 0-woman):").split())
        if S == 1:
            per.append((V, S))
            m = max(per)
            d = per.index(m)
    if per:
        print("The older man lives at home #", d + 1)
        print("He is", m[0])
    if not per:
        print("-1")
elif N > 100 and N <= 0:
    print("N must be [1;100]")
