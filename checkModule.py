
import sys
import types
from check import check



def checkModule(modname):
	for modulename, module in sys.modules.items():
		if modulename != modname:
			continue

		for fname in dir(module):
			func = getattr(module, fname)
			if type(func) != types.FunctionType:
				continue

			print('patching function', fname)
			setattr(module, fname, check(func))




