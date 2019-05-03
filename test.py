
from checkModule import checkModule
from check import check

#print('test')
checkModule('aaa')


def foo(a:int, b:float)->int:
	return a+b


def manz(c:int)->int:
	return c

print(foo(3,4), manz(4))

print(dir())
