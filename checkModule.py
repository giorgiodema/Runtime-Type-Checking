
from inspect import getmembers, ismethod
from check import check
from pprint import pprint as print

def merda():
	pass

def checkModule(modname):
	obj_list = dir(modname)

	print(obj_list)
	for obj in obj_list:
		func = obj[1]
		#print(str(type(func)))
		# skip non-functions
		#if str(type(func)) == "<class 'builtin_function_or_method'>":
		#	continue

		# skip builtins
		try:
			fname = func.__name__
			#print(func.__name__)
		except:
			continue

		if fname.startswith('__') and fname.endswith('__'):
			continue

		# patch __call__ with check wrapper
		try:
			func.__call__ = check(func.__call__)
		except:
			pass
		
		



