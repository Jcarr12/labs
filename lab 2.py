Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 1/2
0.5
>>> int(1/2)
0
>>> 1 // 2
0
>>> "bye" * 5
'byebyebyebyebye'
>>> "bye" / 5
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    "bye" / 5
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> 1+2/5
1.4
>>> (1+2)/5
0.6
>>> sqrt(5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    sqrt(5)
NameError: name 'sqrt' is not defined
>>> from math import sqrt
>>> sqrt(5)
2.23606797749979
>>> sqrt(5)*sqrt(5)
5.000000000000001
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i*5)
	
