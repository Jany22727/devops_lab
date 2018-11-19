def hamming(s1, s2):
    """Calculate the Hamming distance between two bit strings"""
    s1 = format(s1, '8b')
    s2 = format(s2, '8b')
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


if __name__ == '__main__':
    x = [5]
    y = [6]
    hamming(x, y)
'''
x = int((input('1st Hemming namber (in dec): ')))
y = int((input('2nd Hemming namber (in dec): ')))
c = hamming(x, y)

print('The hemming distance =' + str(c))
'''