# Rough Outline Day 1: Code Craftsmanship and Python Language Introduction
Note: This is the rough outline meant scaffold full tutorial development

## Section 1: Introductions and Class format
Purpose of this section is to establish social familiarity with everyone
participating in class and ensure code environments are working

### Objectives
* Introduce myself to class and provide my background
* Instructor to learn the names of all the individuals
* Have class introduce themselves to each other 
* Learn specific motivations of why students are in class
* Run simple code example to be sure everyone has working environment
* Communicate agenda and set pacing for class


### Section 1.1 Intros
#### Instructor Do: Light Introduction (10 minutes)
* Introduce myself and background
* Explain why pydata stack has been useful for me professionally and personally

#### Students Do: Introductions to each other (10 minutes)
* Ask students to pair up
* Talk to each other about their motivations
* In last 5 minutes call on students and ask them to speak for their partner
as to why they came to class


## Section 2: Introduction to Python 
Introduce python language spec to class. Give some "soft" history
and explain relevant details of why python differs from other popular
languages like java, or matlab.


### Objectives
* Introduce python language fundamentals 
* Build up a rock paper scissors game over a series of examples


### Section 2.1 Executing Code
#### Instructor Do: Explain interpreters, repl and executing code (10 minutes)
* Explain how python is
  * language spec, and there are numerous versions
  * that there are numerous interpreters, cython being most common
  * There are multiple ways to execute python code. We're starting with 2
  * Note how python 2 is dead
* Show how to start a repl and run `print("Hello World!")` in a terminal
* Show how these same commands can be saved in a file and run
* Show the most important language feature, how to add comments

#### Students do: Start at terminal and print hello world (5 minutes)
* Start a terminal and execute `print("Hello World!")` in repl
* Run a `hello.py` file from disk
* Secondary purpose is to verify everyone's python installations are working

#### Buffer: (15 Minutes)
* Buffer of time in case issues arise in All do that require trouble shooting

### Section 2.2 Basic Datatypes
#### Instructor Do: Python interpreters, basic data types, and operators (25 Minutes)
* In terminal show students the following basic datatypes
  * Numeric (int/floats)
  * Strings
  * Bools
  * None
* Show comparison operators such as `<`, `==`, 

* Show how variables are assigned in python with `=` operator
* Explain how duck typing in python works using `+` operator
  * Show that adding `2 + 2` returns `4` but `'2' + '2'` return `22`
  * Show how if python can't "figure it out" an exception is raised
* Showcase python builtins, in particular `type, len, str, int, bool`

#### Students Do: Fix the broken examples (10 minutes)
* Give students a .py with various working and failing lines, due to object
mismatch. Ask students to inspect data types and fix to achieve intended result

#### Instructor Do: Review broken examples exercise (5 minutes)
* Answer any questions from exercise

### Section 2.3 Everything is an object and python documentation
#### Instructor Do: Python interpreters, basic data types, and operators (10 Minutes)
* Show how everything is python is an object with methods associated with it
* Showcase examples like `str.lower()` or `.isupper()`
* Point students to python documentation https://docs.python.org/3/library/stdtypes.html#string-methods 

#### Students Do: Try out various methods (10 minutes)
* Students try various methods on and ints from documentation

#### Instructor Do: Review various methods exercise (5 minutes)

### Section 2.4 Collections
#### Instructor Do: Introduce Collections and in operator (20 minutes)
* In terminal show students the following datatypes
  * Lists
  * Tuples
  * Dictionaries
  * Sets
* Show python in operator
* Showcase python slicing `[]` syntax

#### Students Do: Collection practice (15 minutes)
* Collections golf: Get particular values from collections
* Mutate collection, (or don't if its a tuple)
* Check what's in a collection
  * With dictionaries check keys vs values

#### Instructor Do: Collection practice review (10 minutes)
* Collections golf: Get particular values from collections
* Mutate collection, (or don't if its a tuple)
* Check what's in a collection
  * With dictionaries check keys vs values

#### Instructor Do: Collection practice review (5 minutes)

### Section 2.5 Control Flow, Conditionals, and builtins

#### Instructor Do: For, While, Try, Except Conditionals (25 minutes)
* Show python syntax for
  * For
  * While
  * Conditionals
  * How to accept user input with `input()` and `range` function
    * Mention the idea of generators but don't cover deeply
* Show python syntax for Try Except
* Provide guidelines on when to catch exception and when to let them raise

#### Students Do: Conditionals practice (20 minutes)
* Programatic counter from user input
* Continous ask for input until exit command is given
* Mutate collection, (or don't if its a tuple)
* Check what's in a collection
  * With dictionaries check keys vs values
 

#### Instructor Do: Review Conditionals practice (10 minutes)

### Section 2.6 Functions
#### Instructor Do: Functions and args (20 minutes)
* Introduce functions syntax, In particular
  * Positional args
  * Keyword args
  * Return

#### Students Do: Write reusable code (20 minutes)
* Introduce functions syntax, In particular
  * Positional args
  * Keyword args

#### Instructor Do: Write reusable code (10 minutes)

### Section 2.7 Imports

#### Instructor Do: Import syntax (10 minutes)
* Show how python can import built in modules like random
  * Cover import from and as 

#### Students Do: Import random, generate random numbers (10 minutes)
* Import the random module and generate random numbers
* Import math and perform operations on numbers

#### Instructors Do: Review random, generate random numbers (5 minutes)

### Section 2.8 Objects and classes

#### Instructor Do: Object syntax (25 minutes)
* Show object definition, including methods
* Demonstrate object inheritance

#### Students Do: Defining cars (20 minutes)
* Ask students to create a vehicle base class
* Define methods to describe vehicle

#### Instructors Do: Review classes (10 minutes)

### Section 2.9 Splitting code apart

#### Instructor Do: Creating own modules (10 minutes)
* Show object definition, including methods
* Demonstrate object inheritance

### Section 2.10: Advanced topics

#### Instructor Do: Topics not covered by of interest (10 minutes)
* Mention advanced topics such as 
  * Generators
  * Context Manager
  * Python packaging

