class WrongParameterError(Exception):
    def __init__(self, funcname, parname, recvtype, exptype):
        msg =   'Error in function '+'"'+funcname+'"'+' on parameter '+\
                '"'+parname+'"'+': '+'"'+recvtype+'"'+" received while "+'"'+exptype+'"'+' expected'
        super().__init__(msg)

def check(func):

    def wrapper(*params):
        print("params:"+str(params))
        print("decorations:"+str(func.__annotations__))

        args = func.__annotations__
        args_names = list(args.keys())
        
        for i in range(len(args_names)-1):
            parname = args_names[i]
            exptype = args[parname]
            rectype = type(params[i])

            if rectype!=exptype:
                raise WrongParameterError(func.__name__,parname,str(rectype),str(exptype))

        return func(*params)
    
    return wrapper


@check
def test(a:int,b:int)->int:
    c = a+b
    return c

res = test(3,2.2)
print("res:"+str(res))

