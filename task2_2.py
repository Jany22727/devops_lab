#!/bin/python

a = list(input('a: '))
b = list(input('b: '))

if len(a) >= len(b):
    a.sort()
    a.reverse()
    if a[-1] == '-':
        a[-1], a[0] = a[0], a[-1]
    a1 = ''.join(list(a))
    a = int(a1)
    b.sort()
    if b[0] == '0':
        b[0], b[1] = b[1], b[0]
    b1 = ''.join(list(b))
    b = int(b1)
    print(a, b)
else:
    b.reverse()
    if b[-1] == '-':
        b[-1], b[0] = b[0], b[-1]
    a.sort()
    if a[0] == '0':
        a[0], a[1] = a[1], a[0]
    a1 = ''.join(list(a))
    a = int(a1)
    b = int(b)
    print(a, b)
rez = abs(a) - abs(b)
print(rez)
