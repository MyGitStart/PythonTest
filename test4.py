# -*- coding: utf-8 -*-
base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# noinspection PyInterpreter
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


print dec2bin(123)
byte = bytearray(123)
print byte
name = "qw,rt,ty,ry"
print name.split(',', 2)
name = name.split(',', 2)
spe = ","
print spe.join(name)
