def hamming(s1, s2):
    """Calculate the Hamming distance between two bit strings"""
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


a = int((input('1st Hemming namber (in dec): ')))
b = int((input('2nd Hemming namber (in dec): ')))
x = format(a, '32b')
y = format(b, '32b')
print('In binary\n' + str(a) + '-->\t|' + x + '\n' + str(b) + '-->\t|' + y)
c = hamming(x, y)
print('The hemming distance =' + str(c))
