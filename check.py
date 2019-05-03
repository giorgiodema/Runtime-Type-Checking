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
        parname = None
        count = 0
        for i in range(len(args)):
            # if i >= arg_names-1 it means that args[i] is a *arg, so i do not update the
            # expected type, since it's the last specified
            if i<len(args_names)-1:
                parname = args_names[i]
                exptype = ann[parname]
                count+=1
            recvtype = type(args[i])
            parname = args_names[count-1]

            if recvtype!=exptype:
                raise CheckTypeError(func.__name__,parname=parname,recvtype=str(recvtype),exptype=str(exptype))

        # Check kwargs
        for k in kwargs.keys():
            exptype = None
            # if k is not in annotations, it means that k is a kwarg, so i take the type of the
            # last annotation (kwarg is the last argument in the function definition)
            if k not in ann.keys():
                keys = list(ann.keys())
                exptype = ann[keys[-2]] 
            else:
                exptype = ann[k]
            recvtype = type(kwargs[k])
            
            if recvtype!=exptype:
                raise CheckTypeError(func.__name__,parname=k,recvtype=str(recvtype),exptype=str(exptype))

        ret =  func(*args)
        if "return" in ann.keys():
            if type(ret) != ann["return"]:
                raise CheckTypeError(func.__name__,recvret=str(type(ret)),expret=str(ann["return"]))
        return ret
    
    return wrapper



@check
def foo(a:int,b:int,**params:list)->int:
    return a+b

d = {"uno":1,"due":2}

foo(3,2,c=[1,2])