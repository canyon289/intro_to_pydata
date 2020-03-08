# Rough Outline Day 2: PyData tools
Note: This is the rough outline meant scaffold full tutorial development

## Section 1: PyData/Scientific Tooling
Go through pydata tooling showing use cases but also explaining history
and community around the tools 

### Objectives
* Demonstrate use of notebooks
* Explain how efficient numerical computation is typically performed
* Demonstrate how to generate visualizations in python
* Demonstrate file IO in python
* Show how data cleaning and munging is done using Pandas


### Section 1.1: Intros and class welcome

#### Instructor Do: Introduction to class (15 minutes)
* If class is different from Day 1 repeat below
  * Introduce myself and background
  * Explain why pydata stack has been useful for me professionally and personally
* Talk through agenda

#### Partners Do: Fizzbuzz Warmup (15 minutes)
* Write fizbuzz from scratch with a partner
  * Exercise ensures students are comfortable with python and have a working
  environment

#### Instructor Do: Review Fizzbuzz Warmup (5 minutes)
* Assumption is that students know python so review is short

#### All Do: What are you interested in today? (10 minutes)
* Purpose is to have students think ahead as to what they want to learn
* Instructor learns what students specifically want to know to better
target lecture



## Section 2: Pydata Tooling

### Section 2.0 Conda?
* Question: Are students familiar with conda or virtual envs? If not will
need to cover

### Section 2.1 Jupyter Notebooks

#### Instructor Do: Show jupyter notebook functionality (25 minutes)
* Explain jupyter notebook to students
* Show to start server and get to web interface
* Explain portions of interface, covering common widgets
* Show how to create a python notebook with kernel
* Show how to add cells and run code
* Show how to add markdown cells for annotation
* Ensure students understand that notebooks don't have to execute top to bottom
* Show how to export notebooks to html
* Preview remainder of day showing an end to end example of loading a file in pandas
and plotting a couple of graphs


#### Students Do: Fizzbuzz in notebooks (15 minutes)
* Have students start a jupyter notebook
* Have them run their fizbuzz program in the notebook
* Ask them to add human understandable notes in markdown cells
* Have them export their results to html


#### Instructor Do: Review Fizzbuzz in notebooks (10 minutes)


### Section 2.2 Numpy

#### Instructor Do: Numpy primer (20 minutes)
* Explain why numpy is the foundational library to scientific ecosystem
* Explain how numpy differs from lists
* Demonstrate
  * Array creation
  * Array broadcasting
  * Array slicing
* Show other methods available in numpy
* Show students speed difference of numpy over python lists


#### Students Do: Ordinary Least Squares Regression in Numpy (20 minutes)
* Solve ordinary least squares regression using numpy matrix algebra
* Solve using numpy lin alg method


#### Instructor Do: Review Least Squares Regression (20 minutes)

### Section 2.3: Scipy Overview

#### Instructor Do: Scipy Overview (20 minutes)
  * General overview of api
  * Generating random distributions
  * Using optimizer functions
  * [Reading matlab files](https://scipy-cookbook.readthedocs.io/items/Reading_mat_files.html)


#### Students Do: Optimize newspaper inventory holding (20 minutes)
  * Given parameters for newspaper sales distribution
  determine the optimal amount of inventory to hold
  
#### Instructor Do: Review newspaper inventory holding (15 minutes)

### Section 2.4: Matplotlib Overview
* Cover matplotlib object oriented api
  * Mention stateful api and encourage students to use OO api
* Show how to plot various 2D plots
* Show how to plot 3D plots

#### Instructor Do: Show matplotlib basics and api (20 minutes)
* Showcase matplotlib functionality, in particular
  * Fig and axes
  * Anatomy of plot
  * Multiple subplots
  * [3D plots](https://matplotlib.org/3.1.1/gallery/mplot3d/subplot3d.html)


#### Partners do: Plot the previous data in 2D (20 minutes)
* Have students revisit previous exercises and plot
  * Linear regression from numpy section
  * Demand histogram bin in second example

#### Instructor Do: Review 2D plots (15 minutes)

#### Everyone Do: 3D plots (20 minutes)
* Show how 3D plots can be generated using similar api
* Have students follow along while instructor produces plot


### Section 2.5: Pandas
* Explain history of pandas
* Why its so useful in data space
* Why its one of my most used tools

#### Instructor do: Pandas Basics and Data Selection (15 minutes)
* Show manual creation of Pandas Dataframe
* Indexing and selecting or rows
  * Bracket api, iloc and loc
* Adding a column
* Difference between Series and Dataframe
* How to read pandas documentation


#### Instructor do: Loading external data (20 minutes)
* Show how to load data from
  * CSV
  * Excel
  * Relational Database (we'll use postgres)
  * [HDF5](https://www.neonscience.org/hdf5-intro-python)
* Show to to save data to disk as well

#### Students do: Loading external data (10 minutes)
* Load the iris dataset from the internet
* Write the dataframe to disk in various formats

#### Instructor do: Loading external data (5 minutes)

#### Instructor Do: Groupby (15 minutes)
* Show group by's functionality using standard functions
* How to write custom group by functions

#### Students Do: Count and average flowers (10 minutes)
* Using iris dataset count number and average of attributes in each group

#### Instructor Do: Review groupby (5 minutes)

#### Instructor Do: Advanced dataframe manipulation (20 minutes)
* Show API for multiindex and pivot tables
* Show `pd.join` and `pd.merge` functionality

#### Students Do: Clean dataset for analysis and presentation (25 minutes)
* Give students a couple messy datasets
* Ask them to either mutate the dataframe for presentation or for analysis

#### Instructor Do: Review Dataset Cleaning (10 minutes)

## Section 3: Conclusion
### Section 3.1 Wrap up (20 minutes)
* Ask students how they can apply what they learned to their work
* Answer any remaining questions

