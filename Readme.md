# Check Type

## Description
Python runtime type checking using decorators and annotations.

## Usage

To specify the type of each parameter and the return type in the function definition use annotations, like in the example.
```python
def foo(a:int,b:int)->int:
    c = a+b
    return c
```

If you want foo to throw type exceptions (wrong parameter or return type, missing parameter or return type during definition) simply add the decorator ` @check ` to the function definition, like in the example.
```python
from check import check

@check
def foo(a:int,b:int)->int:
    c = a+b
    return c
```