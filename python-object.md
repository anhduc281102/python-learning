# Python Objects 

## Function

* Basically, it's actually a 'function' in maths with the format f(x)

* Usage: reuse a block of codes

*note*: every code block is defined by identation (a 'tab')

* How to define a `function`:

```
def <function_name>(<variable_name1>, [variable_name2],..):
	<code block>
```


## OOP - Object Oriented Programming

### Class and Instance 

Class is a "blueprint" to create an instance.

### Class:

* A `Class` consists of 2 main components:

	* Attributes: variables
	
	* Methods: funtions 


* How to design (given a an activity in real life):

	* noun: Object, Instance of a Class or even an attribute of the Class

	* verb: a method (mostly) and sometime an Object or attribute  

* How to create a `Class` in python:

```
class <class_name>:
	# constructor
	def __init__(self, [<var1>], [var2,..]):
		self.<attribute_1> = <var1>
		... 	

	def <function_name>(self, <var1>, [var2,...]):
		<code block>
```

* How to call a function within a class:

> self.<function_name>(<value>)

* How to call a function of an Instance:

```
p = Person()

p.<function_name>()

p.<attribute_1>
```
