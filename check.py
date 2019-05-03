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

    def wrapper(*params):

        args = func.__annotations__
        args_names = list(args.keys())

        if "return" not in args_names:
            raise CheckTypeError(func.__name__,message="Missing return type")

        if len(params)!=(len(args_names)-1):
            raise CheckTypeError(func.__name__,message="Missing parameter type")
        
        for i in range(len(args_names)-1):
            parname = args_names[i]
            exptype = args[parname]
            rectype = type(params[i])

            if rectype!=exptype:
                raise CheckTypeError(func.__name__,parname=parname,recvtype=str(rectype),exptype=str(exptype))

        ret =  func(*params)
        if type(ret) != args["return"]:
            raise CheckTypeError(func.__name__,recvret=str(type(ret)),expret=str(args["return"]))
        return ret
    
    return wrapper


