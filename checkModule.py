
from inspect import getmembers, isfunction

def checkModule(modname):
	obj_list = getmembers(modname)
	for func in obj_list:
		# skip non-functions
		if not isfunction(func):
			continue

		# skip builtins
		fname = func.__name__
		if fname.startswith('__') and fname.endswith('__'):
			continue

		# patch __call__ with check wrapper
		func.__call__ = check(func.__call__)
		
		



