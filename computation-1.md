## Computation Part I: Models of computation

The questions I want to answer in this post are:

1. What does it mean for a thing to "compute"?
2. What are some examples of things that compute?
3. How do you figure out what a given computer is capable of computing?

I'll start by describing several different models of computation, and look at the limitations of each. Then at the end I'll take the intersection of their characteristics to define what it means for something to compute.

People aren't the only things that can add. So can calculators. A calculator does 

There are three elements:

* Input
* A sequence of steps that generate an output based on the input
* Output

_Anything_ that has these three elements I'll consider to be a computer. This definition is extremely general. 

### Arithematic

Motivating example: addition. The most familiar way to add is to start with two numbers, such as 1923 and 649, and follow a sequence of steps which adds individual digits together one-by-one from the least significant to the most significant, resulting in something that looks like this:

### Combinational logic

### Sequential logic & finite state machines

### Cellular automata

### Finite State Automata

An FSA is defined by:

* A set of states: one is a "start" state, one or more are "accepting" states, and the rest are just normal states
* A transition rule which determines the next state based on the current state and the current symbol being read

FSAs can be specified by a diagram or a table that includes the transitions.

The input to an FSA is a string, such as $$\texttt{001010}$$, or $$\texttt{Ab10*2}$$, where each character in the string comes from a specified alphabet $$\Sigma$$. The set of all possible strings you can make with the alphabet is called $$\Sigma^*$$. For example, if $$\Sigma = \{0,1\}$$, then $$\Sigma^* = \{\epsilon,0,1,00,01,10,...\}$$.

Now, there are some strings in $$\Sigma^*$$ which when fed to $$A$$ will cause $$A$$ to end an accepting state. The set of such strings is called $$A$$'s _language_, and is denoted by $$L$$. The FSA is said the "recognize" this language.

* "Marbe rolling toy" example
* Can be deterministic or non-deterministic. Non-deterministic ones have equivalent deterministic versions, but they tend to contain many more transitions

### Turing Machines

### Brainfuck

### Chemical computers

### Last

What do they have in common? _They all take a set of inputs and follow a series of operations to derive a meaningful output._

## Computation Part II: Making a computer (basically)

* Circuits & binary functions
* Arithematic
* Programming

## Computation Part III: Thermodynamics of computation