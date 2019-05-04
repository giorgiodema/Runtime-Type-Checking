
from checkModule import checkModule



def foo(a:int, b:float)->int:
	return a+1

def manz(c:int)->int:
	return c


checkModule(__name__)  #to be called after all functions definitions


print(foo(3,4.4), manz(4))
