# coding=utf-8
a='12321fa'

try:
    a=int(a)
except ValueError:
    print('error')
finally:
    print(a)