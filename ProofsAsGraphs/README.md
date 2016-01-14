# Encoding and using Graphs

### DOTTY

An early member of the graph encoding languages is `dotty` which is part of `Graphviz`. Files typically have the extension `.dot`

	digraph G {
	compound=true;
	subgraph cluster0 {
	a [label="this is A"];
	a -> b;
	a -> c;
	b -> d;
	c -> d;
	}
	subgraph cluster1 {
	e -> g;
	e -> f;
	
	}
	b -> f [lhead=cluster1];
	b [label="crazy"];
	d -> e;
	c -> g [ltail=cluster0,
	lhead=cluster1];
	c -> e [ltail=cluster0];
	d -> h;
	
When this code is compiled using the program `dotty` we get an image like this [Dot-Graph](https://raw.githubusercontent.com/zhenzhai/CSE103_edX/master/ProofsAsGraphs/examples/ClusteredGraph.jpg)

#### Examples in the directory `examples`

##### Simple.dot
A simple graph using Latex mathematical notation. Has to be compiled using 
`dot2tex | pdflatex` instead of `dotty`

##### CSE103Dependencies.dot
A graph describing the dependencies between subjects in the CSE103 course.

##### InfiniteNumberOfPrimes.dot, examples/InfiniteNumberOfPrimes.parts.dot
Figures for an excercise in proving that the number of primes is infinite

### Mermaid

Mermaid is a javascript system for creating graphs. It is similar to Dotty. To play with it, clone this repository and then open in your browser the file `mermaid/editor/index.html`

### Blockly

Blockly is a system that supports creating programs by connecting Blocks. This method, started by the MIT project `scratch`, is now used for many other design tasks. We want to use it to allow the creation of proof excercises in open-EdX

*Joe* has done some work in this direction which you can play with by opening the file `blockly_proofs/index.html`

# Parsing

Much of the work for this project involves translating between representations. The user-facing representation has to be intuitive and clutter-free, while the result of the translation is intended to be executed / displayed by a machine. This is the `mark-down` approach.

The main tool we use for translating between representation is [PLY](http://www.dabeaz.com/ply/). Which is a python version of the well known `yacc` (Yet Another Compiler Compiler).

