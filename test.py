from check import check


@check
def test(a:int,b:int)->int:
    c = a+b
    return c

res = test(3.2,2)
print("res:"+str(res))
