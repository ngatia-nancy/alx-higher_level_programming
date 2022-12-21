                                                          Python - Exceptions
0.0-safe_print_list.py - Write a function that prints x elements of a list.

Prototype: def safe_print_list(my_list=[], x=0):
my_list can contain any type (integer, string, etc.)
All elements must be printed on the same line followed by a new line.
x represents the number of elements to print
x can be bigger than the length of my_list
Returns the real number of elements printed
You have to use try: / except:
You are not allowed to import any module
You are not allowed to use len()

1. 1-safe_print_integer.py - Write a function that prints an integer with "{:d}".format().

Prototype: def safe_print_integer(value):
value can be any type (integer, string, etc.)
The integer should be printed followed by a new line
Returns True if value has been correctly printed (it means the value is an integer)
Otherwise, returns False
You have to use try: / except:
You have to use "{:d}".format() to print as integer
You are not allowed to import any module
You are not allowed to use type()

2. 2-safe_print_list_integers.py - Write a function that prints the first x elements of a list and only integers.

Prototype: def safe_print_list_integers(my_list=[], x=0):
my_list can contain any type (integer, string, etc.)
All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
x represents the number of elements to access in my_list
x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
Returns the real number of integers printed
You have to use try: / except:
You have to use "{:d}".format() to print an integer
You are not allowed to import any module
You are not allowed to use len()

3. 3-safe_print_division.py - Write a function that divides 2 integers and prints the result.

Prototype: def safe_print_division(a, b):
You can assume that a and b are integers
The result of the division should print on the finally: section preceded by Inside result:
Returns the value of the division, otherwise: None
You have to use try: / except: / finally:
You have to use "{}".format() to print the result
You are not allowed to import any module

4. 4-list_division.py - Write a function that divides element by element 2 lists.

Prototype: def list_division(my_list_1, my_list_2, list_length):
my_list_1 and my_list_2 can contain any type (integer, string, etc.)
list_length can be bigger than the length of both lists
Returns a new list (length = list_length) with all divisions
If 2 elements can’t be divided, the division result should be equal to 0
If an element is not an integer or float:
print: wrong type
If the division can’t be done (/0):
print: division by 0
If my_list_1 or my_list_2 is too short
print: out of range
You have to use try: / except: / finally:
You are not allowed to import any module

5. 5-raise_exception.py - Write a function that raises a type exception.

Prototype: def raise_exception():
You are not allowed to import any module

6. 6-raise_exception_msg.py - Write a function that raises a name exception with a message.

Prototype: def raise_exception_msg(message=""):
You are not allowed to import any module

7. 100-safe_print_integer_err.py - Write a function that prints an integer.

Prototype: def safe_print_integer_err(value):
value can be any type (integer, string, etc.)
The integer should be printed followed by a new line
Returns True if value has been correctly printed (it means the value is an integer)
Otherwise, returns False and prints in stderr the error precede by Exception:
You have to use try: / except:
You have to use "{:d}".format() to print as integer
You are not allowed to use type()

8. 101-safe_function.py - Write a function that executes a function safely.

Prototype: def safe_function(fct, *args):
You can assume fct will be always a pointer to a function
Returns the result of the function,
Otherwise, returns None if something happens during the function and prints in stderr the error precede by Exception:
You have to use try: / except:

9. 102-magic_calculation.py - Write the Python function def magic_calculation(a, b): 

10. 103-python.c - Create three C functions that print some basic info about Python lists, Python bytes an Python float objects.
           
       Python lists:

Prototype: void print_python_list(PyObject *p);
Format: see example
If p is not a valid PyListObject, print an error message (see example)
Python bytes:

Prototype: void print_python_bytes(PyObject *p);
Format: see example
Line “first X bytes”: print a maximum of 10 bytes
If p is not a valid PyBytesObject, print an error message (see example)
Python float:

Prototype: void print_python_float(PyObject *p);
Format: see example
If p is not a valid PyFloatObject, print an error message (see example)
Read /usr/include/python3.4/floatobject.h
