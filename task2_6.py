def ip2bin(ip):
    octets = map(int, ip.split('/')[0].split('.'))
    binary = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*octets)
    range = int(ip.split('/')[1]) if '/' in ip else None
    return binary[:range] if range else binary


def netw(ip1, ip2, mask):
    s = 0
    p = 0
    for n in mask:
        if (n == '1'):
            s += 1
    # print('Prefiks - /'+ str(s))
    for i1, i2 in zip(IP1, IP2):
        if (p < s):
            if (i1 == i2):
                p += 1
            else:
                break
    return 1 if p == s else 0


# Вводим маску и ip
Mask = (input('Mask: '))
Mask2 = (input('Mask2: '))
IP1 = (input('IP1: '))
IP2 = (input('IP2: '))
# Преобразуем ip во bin (str) значение
Mask = ip2bin(Mask)
Mask2 = ip2bin(Mask2)
# Mask2 = ip2bin(Mask2)
IP1 = ip2bin(IP1)
IP2 = ip2bin(IP2)
# Выведем в двоичном формате
# print (Mask+'\n'+Mask2+'\n'+IP1+'\n'+IP2)
c = netw(IP1, IP2, Mask)
b = netw(IP1, IP2, Mask2)
print(c, b, c + b)
print('IP adresses consist on ' + str(c + b) + ' subnets')
