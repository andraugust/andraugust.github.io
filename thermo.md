## Thermo Notes

Thermal physics is the study of systems having a very large number of states or objects, so many that we can't practically study them directly. Instead, we study them at a macroscopic scale where two things are true:

1. The exact details of the system's underlying states don't need to be known in order to make useful predictions about the system's bulk properties.
2. The statistical properties of the system fluctuate so minimally that we can treat them as fixed and make useful statistic predictions (such how often two atoms in a gas collide, or how likely they are to have a certain speed).

These two things are what thermal physics is about. And in this post I'll 

As an example, a mole of a gas is a system that falls within the domain of thermodynamics. To represent its state we have to make a list of each atom's position and momentum, about $$10^{23}$$ numbers in total. This is an absurdly large number of numbers. It would take about $$10^9$$ supercomputers-worth of storage space to represent them all. Imagine the energy required to propogate the state one step forward in time. It's not happening.

Instead of following every atom, we compute a small number of functions of the system's state to get manageable bulk properties like temperature, pressure and energy. But this raises an obvious question: if we're calculating functions of state, don't we still need to know the state? The answer is technically yes, but practically no. Practically no because, as we'll see, when thermal systems come to equilibrium, quantities such as pressure, temperature and energy are effectively constant even as their underlying states change, so we can ignore the states.

Before going further, I should mention that the word _state_ can be ambiguous in thermal physics. Sometimes it refers to the state of macroscopic variables and sometimes it refers to the configuration of the system, which is what I've been calling "the state" so far. To disambiguate, configurations get called _microstates_ (even though they may be bigger or smaller than a micron), and macroscopic states get called, surprise, _macrostates_. I'll use these words from now on.

Now, in order to start _doing_ thermodynamics, I have to state its fundamental assumption: _when a system is in thermal equilibrium, microstates transition between each other uniformly randomly such that each microstate is equally likely to be observed at any given time_.

This is a major assumption. From a classical mechanics perspective microstates follow a single deterministic trajectory through phase space, one determined by the system's initial conditions and whatever forces are involved. Looked at this way, transition probabilities are delta functions along the system's one and only trajectory, not uniform distributions throughout phase space. Then how do we get away with this uniformity assumption? The answer has to do with the definition of thermal equilibrium, which is that a system in "thermal equilibrium" has its energy spread throughout its parts such that statistical fluctuations of macroscopic properties go to zero. And since it's the macroscopic properties we're ultimately after

To get some intuition for thermal equilibrium I like to think of a gas in a box. Imagine the gas starts far from equilibrium, with initial conditions such that its atoms are all bunched up together in the upper left corner of the box and move together with the same velocity to the right. A moment later the atoms are still bunched up together, but shifted slightly. This is a very specific trajectory, one that's not uniform, but that's ok because the system isn't in equilibrium yet. If we wait longer, the atoms eventually hit the wall of the box, bouncing backward into each other, some before others, some later, some transferring lots of energy to their collision partner, some transferring less. Eventually, the distribution of atomic speeds, for example, becomes stationary (despite each individual atom's speed changing in each of its collisions). Similarly, the force per unit area exerted on the walls of the box by the atoms, i.e., the box's pressure, becomes constant. Now the gas is in equilibrium where the assumption holds and we can model it thermodynamically.

---

### Isolated Systems

Isolated systems are a simple starting point. What can we say about them? Not a lot—we can talk about their total energy $$U$$, number of particles $$N$$, and the number of ways $$U$$ can be split amongst the $$N$$ particles. This last quantity is the number of microstates available to the system, called its multiplicity $$\Omega$$. In the next section when we look at two interacting systems $$\Omega$$ will be key to understanding how the systems exchange energy and "choose" which equilibrium macrostate to occupy. So let's get a feel for $$\Omega$$ by calculating it for three example systems: a magnet, a solid, and a gas.

__The Magnet.__ The two-state paramagnet's "particles" are dipole moments that align either with or against an external magnetic field. If we work in energy units of $$\mu B$$, where $$\mu$$ is each dipole's moment and $$B$$ is the exteral field, the energy of an aligned dipole is $$-1$$ and the energy of an anti-aligned dipole is $$+1$$ (so dipoles want to align with the field).

The total energy is
$$
U = N_\downarrow-N_\uparrow = N-2N_\uparrow
$$
where $$N_\uparrow$$ and $$N_\downarrow$$ are the number of aligned and anti-aligned dipoles, respectively, and $$N=N_\downarrow+N_\uparrow$$ is the total number of dipoles.

A microstate for this system is a binary list of each dipole's alignment, for example $$[\uparrow,\downarrow,...,\downarrow]$$. Macrostates are things like $$U$$, $$N_\uparrow$$, and the total magnetization $$M$$—ggregate functions of the microstate.

The multiplicity is
$$
\Omega(N_\uparrow) = \begin{pmatrix} N \\ N_\uparrow \end{pmatrix} = \frac{N!}{N_\uparrow ! (N-N_\uparrow)!}
$$
In terms of energy and number of particles,
$$
\Omega(U,N) = \frac{N!}{\frac{N-U}{2}!\frac{N+U}{2}!}
$$
__The Solid.__ The Einstein solid is a simple model of a solid where "particles" are spring-like oscillators connecting atoms in a cubic lattice. Oscillators are defined as identical so they have the same frequency parameter, and they're treated quantum mechanically so their energy is discretized in units of $$\hbar \omega$$.

The total energy of the oscillators (relative to the ground state and in units of $$\hbar\omega$$) is just the total number of energy units in the system: $$U$$.

A microstate is specified by listing each oscillator's energy. For example, if there are 5 energy units and 3 oscillators, microstates can be $$[2,0,3]$$ or $$[1,1,3]$$, etc. 

The multiplicity is
$$
\Omega(U,N) = \begin{pmatrix} U+N-1 \\ U \end{pmatrix}
$$
__The Gas.__ The ideal gas is an interesting example. Classically it's modeled as a collection of monatomic atoms that scatter elastically off each other and off the walls of the volume they're in. (For this to be accurate the gas needs to be at a low enough density and high enough energy that the atoms spend their time either far apart, where inter-atomic forces are zero, or really close, where inter-atomic forces are strongly repulsive). How are states counted here? Classically, the gas's state is a list of each atom's position and momentum. But these are continuous quantities that can't be counted—there are an infinite number of them. If, on the other hand, the gas is modeled quantum mechanically, states become discritized and they can be counted. So let's look at a quantum gas.

In the quantum model, one atom's energy is
$$
U = 
$$


### Interacting Systems





* Multiplicity is the number of ways of arranging



__Temperature & Energy.__ Temperature is defined as the willingness of a system to exchange energy with another system. Energy exchanged in this way is called _heat_. Any other form of energy transfer is called _work_. Heat and work describe energy _in transit_, so it doesn't make sense to say something like "the coffee cup has a lot of heat", but you can say "the coffee cup has a lot of energy".



__Thermodynamic limit.__ The _thermodynamic limit_ is the regime where fluctuations are negligable relative to the average of whatever quantity is being considered.

__Ensembles.__ Consider two systems $$A$$ and $$B$$ that exchange energy with each other but are otherwise isolated. $$A$$ is in a state $$x_A$$ whose specific details we do not know. For example $$A$$ could be a mole of gas, in which case $$x_A$$ is the position and momenta of all the constituent particles. What we'll assume we do know, however, is the state's energy $$E_A$$. In addition we know that there are many _other_ states that have this same energy, and we denote the number of them by $$\Omega(E_A)$$.

What does this have to do with thermodynamics? There's a principal in thermodynamics which states that:

1. When a system has $$E$$, all of the states having $$E$$ are equally likely to be the one the system is actually in.
2. State transitions are uniformly random.

What this implies is that the system spends a disproportionately large amount of time in states that  $$\Omega(E_A)\Omega(E_B)$$.  
