---
layout: default
---

# Artificial Life, Neural Nets, and Genetic Algorithms

<div class="video-responsive">
  <iframe width="840" height="472" src="https://www.youtube.com/embed/UW8y_R7PE_c?rel=0" frameborder="0" allowfullscreen></iframe>
</div>
<br />

## Background

One of the challenges of using neural nets to control AI agents is the absence of a suitable learning algorithm. Gradient descent based methods work well for NN classifiers and regressors, but that's because in these cases inputs have well defined desired outputs, and the dependence of the objective function on the input-output mapping is explicit _and_ differentiable.  In many AI contexts, however, objective functions aren't evaluated until after a long sequence of NN outputs (actions) have occurred, so it isn't clear which outputs played what role in shaping the final value of the objective f'n.

Learning, however, is an optimization task, so any optimization algorithm is candidate to be a learner.  In this post I use a non-gradient based algorithm called a _genetic algorithm_ to learn good neural net weights, despite the absence of instant-by-instant feedback or a differentiable objective f'n.

## Artificial Life: The Setting

The context of the problem is artificial life: an agent moves in a 2-d world and must find food to survive.  But the world is a scary place and contains deadly moving circles that kill on contact, and there's a "metabolic clock" that kills if it reaches 0%, so agents have to find food before they starve.

Agents are controlled by feed-forward neural nets that convert sensory input into actions.  Actions are based solely on the parameters of the network and the input stimulus from the environment (more about inputs later).  To identify parameters that produce long-living agents, a genetic algorithm is used.  The GA searches through parameter space, and, as we'll see, is able to find good parameters that keep agents alive for progressively longer time-periods.

The video above shows agents at various stages of optimization, so-called _generations_.  In the beginning, agents move arbitrarily and get killed pretty quickly (the red bar indicates health).  After about 10 generations agents manage to navigate to food, but only sometimes.  By generation 25 agents expertly avoid balls and navigating to food.  Success.

## Neural Nets: The Brain

Agents have access to their environment through eight senses:

* The distance to food.
* The distance to the nearest blue ball.
* The sine and cosine of the angle between the agent's heading direction and food.
* The sine and cosine of the angle between the agent's heading direction and the nearest blue ball.
* The sine and cosine of the agent's heading direction relative to the world's coordinate system.

These measurements are fed into a single-layer feed-forward neural net that functions as the agent's brain.  The neural net outputs one of the following actions at each time-step:

* Rotate by a small pre-defined constant amount.
* Translate forward by a small pre-defined constant amount.
* Sit still.

Here's a diagram of the neural net:

<center><img src="neuroev/network.png"></center>
<br />
The network has six sigmoid nodes (tanh) and three linear nodes.  Actions are associated with each linear node and the action with the largest output is implementation by the agent.

The action performed at a given timestep is an index into the action-list:

$$a_t = \arg\max{[W_2\tanh{(W_1s_t)]}}$$

## Genetic Algorithms: The Optimizer
Brains are pretty standard neural nets, but they're optimized in an interesting way. Neural nets typically train using backpropagation which requires ground-truth feedback.  In the context of the simulated micro-organism there isn't really any ground-truth.  We do keep track of how long agents live, and use this to measure "error", but the length of time that an agent lives doesn't inform _what_ made the agent live that long.  For instance, if an agent rotates in place every few seconds and then moves towards food every few seconds, then was it the rotating in place that made the agent successful or the moving towards food?  Obviously we know it's the moving towards food, but the lifespan information doesn't make a distinction.  To deal with ambiguous feedback like this we use an optimization procedure that doesn't require continuous feedback, we use a genetic algorithm called Enforced SubPopulations, or ESP.

ESP, like most genetic algorithms, finds (or hopes to find) good parameters by combining parameters from networks that have been tested in the past and were successful.  In the context of our agent "tested" means running the network in the world and "successful" means the agent lived for a long time.

ESP is distinguished from other genetic algorithms by its assignments of _subpopulations_ to each network-node.  Subpopulations are a list of weight-lists,  each defined by the parameters going into and outof the corresponding node.  To make a fully-formed network one weight-list is selected from each node's subpopulation and applied the node's edges.  The fully-formed network is then placed "in" an agent and the agent is evaluated in the world.

Identifying good weights is the primary challenge of this problem.  It's solved through the following algorithm:
1. _Initialization_: Initialize all weights uniformly in [−1, 1], with 50 weight-lists per node.
2. _Evaluation_: Randomly select weight-lists from each node and use them to construct a fully-defined network. Run this network in an agent until it dies and record its lifetime.  Give each weight-list that participated in the network a score equal
to the lifetime. Do this until each weight-list in each subpopulation is used at least 100 times.
3. _Selection_: For each node, delete the lowest scoring 50% of weight-lists.
4. _Crossover_: Within each node, arbitrarily select two of the retained weight-lists and cross them at an arbitrary location.  Replace one of the deleted lists with this "child" list. Repeat until all deleted lists are replaced.
5. _Mutation_: Mutate all weights by adding a uniformly random number between −0.02 and 0.02 to them.
6. _Repeat_: Goto Step 2 until an agent's life-time exceeds a threshold, print this agent's weights and terminate training.

Each loop through this algorithm is called a _generation_.  Here's a plot of lifetime vs generation when different numbers of sigmoid nodes are used:

<center><img src="neuroev/lifetime_plot.png"></center>
<br />
Evidently there isn't a clear relationship between the lifetime and the number of sigmoid nodes used (at least in the range tested), but nonetheless the GA works and after about 20 generations the agents live for about 1000 (!) times longer than their arbitrarily generated ancestors.  Pretty awesome!

__Reference:__ Gomez, F. J. (2003). Robust Non-linear Control through Neuroevolution. PhD thesis, University of Texas, Austin, TX. [Link](http://www.cs.utexas.edu/users/nn/downloads/papers/gomez.phdtr03.pdf)

__Code:__ [https://github.com/andraugust/neuroevESP](https://github.com/andraugust/neuroevESP)

__Questions:__
* How necessary were genetic algorithms and sigmoid nets for this application?  Could successful agents have been found using simpler optimization procedures?  What if a linear neural net was used instead of a sigmoid net?  Can linear nets generate successful agents too?
* The agents in this application don't have any memory---their feedforward nets give the same output for the same input, regardless of past inputs.  If networks had feedback connections, could they learn faster?  The current environment doesn't require memory--agents are able to survive without it.  What types of environments do require memory?
<br />

{% include disqus.html %}
