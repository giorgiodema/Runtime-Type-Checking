
from inspect import getmembers, isfunction

def checkModule(modname):
	obj_list = getmembers(modname)
	for obj in obj_list:
		# skip non-functions
		if not isfunction(obj):
			continue

		# skip builtins
		fname = obj.__name__
		if fname.startswith('__') and fname.endswith('__'):
			continue
		
		



