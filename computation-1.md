## Computation Part I: Models of computation

The questions I want to answer here are:

1. What is the definition of a computer?
2. What are some examples of computers?
3. How do you determine what a given computer can/can't do?

A computer is a physical system that transforms the state of another physical system. The process of this tranformation is called a computation, and by "transforms" I mean that if the state of B before the computation is b, then the state after is simply some other one b'.

This definition may sound unusual. Typically computers are defined in terms of circuits and hardware, but ultimately those things are physical and therefore can be modelled as such. This definition is extremely general, but as I'll show computers are too!

Let's look at some examples to ground this definition.

### Arithematic

Much of what computers originally did was crunch numbers, so I'll start by describing computational models for arithematic, which leads naturally into the next section on combinational logic.

**Addition**. There are a couple ways to think about addition. The first is in terms of the familiar addition _algorithm_, which pairs digits place-wise and then adds each pair using a rule to handle carry values. This algorithm is a complete _specification_ of addition because it always finishes with the correct sum.

The second way to think of addition is in terms of a table. A very long table like the one below:

[addition table here]

Like the algorithm, this table completely specifies addition because it associates each pair of inputs with the corresponding sum. 

Neither the algorithm nor the table, however, is a computer. So where does the computer come in? The computer is the *thing* that implements the function. It's _any_ physical system that converts inputs to outputs like in the table. I emphasize _any_ because the computer could be digital, analog, quantum, made of water, sand, whatever, just as long as its i/o matches the table. 

What does it mean for a physical system to "match" the table?



This may be accompliIt may do this by following the addition algorithm, or it may do it following some other algorithm, or it may simply check an existing look-up table  



To add two numbers, you start by pairing up their digits in each position. For example, to add 8125 and 394, you make the pairs [(5,4), (2,9), (1,3), (8,0)]. Then you add the pairs together. If any pair sums to more than 9, then 1 is added to next most significant pair and what's left is assigned to the current pair. This process takes place from the right-most digit position to the left. For example, 

[(5,4), (2,9), (1,3), (8,0)] --> [(5,4), (2,9), (1,3), (8,0)].

The result is 8519.

What I've just described is not a computer. It's an **algorithm** for addition. A sequence of steps that produces a desired output given some input. So what's the computer? The compuer is anything that _implements_ this algorithm. Or, more generally, it's anything that gives the desired output for every pair of inputs we can possibly give it. 





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