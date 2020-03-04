# Rough outline Day 1: Code Craftsmanship and Python Language Introduction
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


### Activities
#### Instructor Do: Light Introduction (10 minutes)
* Introduce myself and background
* Explain why pydata stack has been ueeful for me professionally and personally

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
* Introduce python language fundamentals in following order
  * Interpreters
  * Data Types
  * Loops
  * Control flow
  * String interpolation
  * Exception Handling
  * Functions
  * Classes
  * Imports
  * Multi Module "scripts"

### Section 2.1 Executing Code
#### Instructor Do: Explain interpreters, repl and executing code (10 minutes)
* Explain how python is
  * language spec, and there are numerous versions
  * that there are numerous interpreters, cython being most common
  * There are multiple ways to execute python code. We're starting with 2
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
* Explain that python has different interpreters
* Most important point at the moment is use Python 3. 2 is dead
* In terminal show students the following basic datatypes
  * Numeric (int/floats)
  * Strings
  * Bools
  * None

* Show how variables are assigned in python with `=` operator
* Explain how duck typing in python works using `+` operator
  * Show that adding `2 + 2` returns `4` but `'2' + '2'` return `22`
  * Show how if pythong can't "figure it out" an exception is raised
* Showcase python builtins, in particular `type, len, str, int, bool`

#### Students Do: Fix the broken examples (10 minutes)
* Give students a .py with various working and failing lines, due to object
mismatch. Ask students to inspect data types and fix to achieve intended result

#### Instructor Do: Review broken examples exercise (5 minutes)
* Answer any questions from exercise



## Section 3: Scientific Python Tools
* Introduction to Anaconda and environment management?
* Introduction to Jupyter notebook?

## Section 3:??
## Section 4:??
