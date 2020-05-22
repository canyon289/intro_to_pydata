# Rough Outline Day 3: PyData tools

## Section 1: Profiling Python Code

### Objectives
* Show various way to profile python code

### Section 1.1 "Easy Hacks" to profile python code
#### Instructor Do: Time.time and timeit (20 minutes)
* Show ways to profile snippets of code through taking start and end times
* Show more robust way using built in timeit 

#### Students Do: Fix numerical operation slowdowns (15 minutes)
* Use above methods to time numerical operations when performed in python
* Use numpy to vectorize and improve results

#### Instructor Do: Review fix numerical operation slowdowns (10 minutes)

### Section 1.2 Cprofiler
#### Instructor Do: Introduce cprofiler (15 minutes)
* Show basic use of cprofiler and how to read reports

#### Students Do: Find slow method in script (15 minutes)
* Using cprofiler find various slowdowns in a python script
* Fix slowdowns and measure results

## Section 2: Software Craftmanship
### Objectives
* Provide high level overview of good practices for python code organization

### Section 2.1 Code Craftsmanship
#### Partner Do: Talk about code craftmanship (5 minutes)
* Turn to partner and talk about why code organization is important
* How does it relate to work each persons work, and to their colleagues

#### All Do: Discuss why code craftsmanship is imporant (10 minutes)
* Go around the room and ask folks what they said in discussions
* Share examples from my work at SpaceX and sweetgreen

#### Instructor Do: Show examples of code craftsmanship (15 minutes)
* Show how to structure a typical python repository for various use cases
  * Importable module
  * Analysis
  * Generic scripting
* Explain general principles that work well for python

## Section 3: Integrating external code in other languages
### Objectives 
* Show methods for integrating C or Fortran code with python
* Note this section is most challenging. Full outline will need some more research,
Basic pattern of showcase and instruction will stay the same

### Section 3.1 Docker
#### All Do: Docker Basics (30 minutes)
* Optional section if docker is needed and students need introduction

### Section 3.2 Subprocess
Subprocess module allows python to make system calls. This means pythong
can execute some code, then call to the system to execute external code
in fortran or c or whatever, and if data needs to be shared it can be 
shared through the disk or OS.
#### All Do: Subprocess module (30 minutes)
* Need to scope specific lecture and activities. Still deciding approach

### Section 3.3 Integrating C code
Python has a couple of ways of integrating with C code, as does numpy
and scipy. Need to figure out which approach is most relevant for JPL
#### All Do: Integrating C code (30 minutes)
* *Unfinished* 

### Section 3.4 Integrating Fortran code
Likely going to teach use of f2py which was used in development of PyMC2.
Would like to understand JPL use case before adding further details
#### All Do: Integrating Fortran code (30 minutes)
* *Unfinished* 

