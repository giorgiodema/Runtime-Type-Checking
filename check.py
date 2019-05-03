class CheckTypeError(Exception):
    def __init__(self, funcname, parname=None, recvtype=None, exptype=None,recvret=None,expret=None,message=None):
        if parname:
            msg =   'Error in function '+'"'+funcname+'"'+' on parameter '+\
                    '"'+parname+'"'+': '+'"'+recvtype+'"'+" received while "+'"'+exptype+'"'+' expected'
            super().__init__(msg)
            return
        if recvret:
            msg =   'Error in function '+'"'+funcname+'"'+': returned a '+'"'+recvret+'"'+" while "+'"'+expret+'"'+' expected'
            super().__init__(msg)
            return
        if message:
            msg =   'Error in function '+'"'+funcname+'"'+': '+message
            super().__init__(msg)
            return


def check(func):

    def wrapper(*args,**kwargs):

        ann = func.__annotations__
        args_names = list(ann.keys())

        print("ann:"+str(ann))
        print("args:"+str(args))
        print("kwargs:"+str(kwargs))
        
        # Check args
        for i in range(len(args)):
            parname = args_names[i]
            exptype = ann[parname]
            rectype = type(args[i])

            if parname=='args' or parname=='kwargs':
                break
            if rectype!=exptype:
                raise CheckTypeError(func.__name__,parname=parname,recvtype=str(rectype),exptype=str(exptype))

        # Check kwargs
        for k in kwargs.keys():
            exptype = ann['kwargs'] if k not in ann.keys() else ann[k]
            recvtype = type(kwargs[k])
            
            if rectype!=exptype:
                raise CheckTypeError(func.__name__,parname=parname,recvtype=str(rectype),exptype=str(exptype))

        ret =  func(*args)
        if "return" in ann.keys():
            if type(ret) != ann["return"]:
                raise CheckTypeError(func.__name__,recvret=str(type(ret)),expret=str(ann["return"]))
        return ret
    
    return wrapper



@check
def foo(a:int,b:int,**kwargs:int)->int:
    return a+b

d = {"uno":1,"due":2}

foo(3,2,d=8,uno=1, due=2)