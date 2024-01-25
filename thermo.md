## Thermo Notes

* Thermodynamics vs statistical thermodynamics vs statistical mechanics vs nonequilibrium 

Statistical mechanics is the study of systems having a very large number of elementary objects, so many that we can't practically study them directly. Instead, we study them at a macroscopic scale where two things are true:

1. The details of the elementary objects don't need to be known in order to make useful predictions about the system's macroscopic properties.
2. The statistical properties of the system fluctuate so minimally that they can be treated as constant, and we can make meaningful statistic predictions (such how often two atoms in a gas collide, or how likely they are to have a certain energy).

These two things are what thermal physics is about. And in this post I'll 

As an example, a mole of a gas is a system that falls within the jurisdiction of thermodynamics. To represent its state we would have to list of each atom's position and momentum—about $$10^{23}$$ numbers in total. This is an absurdly large number of numbers. It would take about $$10^9$$ supercomputers-worth of storage space to represent them all. Imagine the energy required to propogate the state one step forward in time—it's not happening.

Instead of tracking every atom in the gas, it's much more practical to compute a small number of _functions of its state_ and get a manageable number of bulk properties such as temperature, pressure and energy. But this approach raises a question: if we're calculating functions of state, don't we need to know the state? The answer is technically yes, but practically no. Practically no because, as we'll see, when thermal systems come to equilibrium, quantities such as pressure, temperature and energy are effectively constant even as the underlying states change, allowing us to ignore the state's specific details.

Before going further, I should mention that the word _state_ is ambiguous in thermal physics. Sometimes it refers to the state of macroscopic variables and sometimes it refers to the configuration of the system, which is what I've been calling "the state" so far. To disambiguate, configurations are called _microstates_ (even though they may be bigger or smaller than a micron), and macroscopic states are called _macrostates_.

Now, in order to start _doing_ thermodynamics, I have to state its fundamental assumption: _when a system is in thermal equilibrium, microstates transition between each other uniformly randomly such that each microstate is equally likely to be observed at any given time_.

This is a major assumption. From a classical mechanics perspective microstates follow a single deterministic trajectory through phase space, one determined by the system's initial conditions and whatever forces are involved. Looked at this way, transition probabilities are delta functions along the system's one and only trajectory, not uniform distributions over phase space. So then how do we get away with this uniformity assumption? The answer is…_it works_. It makes useful predictions that match experiments. As long as the system is in thermal equilibrium where its energy is spread approximately evenly  parts evenly.

To get some intuition for thermal equilibrium I like to think of a gas in a box. Imagine the gas starts far from equilibrium, with initial conditions such that its atoms are all bunched up together in the upper left corner of the box and move together with the same velocity to the right. A moment later the atoms are still bunched up together, but shifted slightly. This is a very specific trajectory, one that's not uniform, but that's ok because the system isn't in equilibrium yet. If we wait longer, the atoms eventually hit the wall of the box, bouncing backward into each other, some before others, some later, some transferring lots of energy to their collision partner, some transferring less. Eventually, the distribution of atomic speeds, for example, becomes stationary (despite each individual atom's speed changing in each of its collisions). Similarly, the force per unit area exerted on the walls of the box by the atoms, i.e., the box's pressure, becomes constant. Now the gas is in equilibrium where the assumption holds and we can model it thermodynamically.


## Isolated Systems

Isolated systems are a simple starting point. What can we say about them? We can say they have a number of particles $$N$$, a total energy $$U$$, and perhaps there are some constraints, like that the system be within a volume $$V$$. Given these things we can calculate (or approximate) the number of possible ways to split $$U$$ amongst the particles while satisfying their constraints. 

This number, called the system's multiplicity $$\Omega$$, is the number of microstates available to the system. It plays an important role in determining which equilibrium macrostate the system will settle to when it's allowed to interact with another system. To get a feel for $$\Omega$$ lets calculate it for three example systems and then in the next section I'll show how it determines equilibrium states. The three example systems are a magnet, a solid, and a gas.

__The Magnet.__ A simple model of a magnet is the two-state paramagnet. Its "particles" are dipole moments that align either with or against an external magnetic field. If we use energy units of $$\mu B$$, where $$\mu$$ is each dipole's moment (the same for all dipoles) and $$B$$ is the exteral field, then the energy of an aligned dipole is $$-1$$ and the energy of an anti-aligned dipole is $$+1$$ (so dipoles want to align with the field).

The total energy is


$$
U = N_\downarrow-N_\uparrow = N-2N_\uparrow
$$


where $$N_\uparrow$$ and $$N_\downarrow$$ are the number of aligned and anti-aligned dipoles, and $$N=N_\downarrow+N_\uparrow$$ is the total number of dipoles.

A microstate for this system is specified by a binary list of each dipole's alignment, for example $$(\uparrow,\downarrow,...,\downarrow)$$. Macrostates are aggregate functions of microstates—things like $$U$$, $$N_\uparrow$$, and the total magnetization $$M$$ are macrostates.

The multiplicity is


$$
\Omega(N_\uparrow) = \begin{pmatrix} N \\ N_\uparrow \end{pmatrix} = \frac{N!}{N_\uparrow ! (N-N_\uparrow)!}
$$


or in terms of energy and number of particles,


$$
\Omega(U,N) = \frac{N!}{\frac{N-U}{2}!\frac{N+U}{2}!}
$$


Note that the fractions in the denominator actually work out to be integers because adding or subtracting a particle always changes the energy by one unit. 

__The Solid.__ A simple model of a solid is the Einstein solid. Its "particles" are spring-like oscillators that connect atoms into a cubic lattice. Oscillators are defined as identical so they have the same frequency parameter $$\omega$$, and they're treated quantum mechanically so their energy is in units of $$\hbar \omega$$.

The total energy of the oscillators (relative to the ground state) is just the total number of energy units in the system: $$U$$.

A microstate is specified by listing each oscillator's energy. For example, if there are 5 energy units and 3 oscillators, possible microstates are $$(2,0,3)$$ or $$(1,1,3)$$, etc. 

The multiplicity is


$$
\Omega(U,N) = \begin{pmatrix} U+N-1 \\ U \end{pmatrix}
$$


__The Gas.__ A simple model of a gas is the ideal gas. It's a gas at low density and high energy such that its atoms scatter elastically off eachother and the walls of the container they're in. As it turns out, many gases fall within this regime, so it's an incredibly useful model.

To derive the multiplicity of an ideal gas containing $$N$$ atoms, it's easiest to start by thinking about what happens when $$N=1$$. With one atom the microstate is given by that atom's position and momentum 3-vectors $$(\mathbf{x},\mathbf{p})$$, where $$\mathbf{x}$$ is bound within a volume $$V$$, and $$\mathbf{p}$$ is related to energy by


$$
U = \frac{1}{2m}\lvert \mathbf{p} \rvert ^2
$$


We're going to assume for now that the atoms have no internal energy-bearing degrees of freedom, such as rotations or vibrations—they're assumed to be monatonic atoms.

Classically a single particle can occupy a continuously infinite number of positions and momenta while satisfying the energy and volume constraints, so it seems like the multiplicity should likewise be continuously infinite. Quantumly, however, there's a limit to the simultaneous "resolution" of $$\mathbf{x}$$ and $$\mathbf{p}$$. In particular, they can only be known together up to the Heisenberg limit $$\Delta x_i \Delta p_i = \hbar/2$$, where $$i$$ indexes the three spatial dimensions. So if we imagine phase space as being chopped up into a grid of $$\Delta x$$s and $$\Delta p$$s that are at this limit, then we can count the number of microstates in a finite, discrete way. Let's see what happens.

The number of position states is


$$
\Omega_x = \frac{V}{\Delta x_1 \Delta x_2 \Delta x_3}
$$


The number of momentum states is


$$
\Omega_p = \frac{S_d(r)}{\Delta p_1 \Delta p_2 \Delta p_3}
$$


Here, $$S_d(r)$$ is the surface area of a sphere of radius $$r$$ and dimension $$d$$. Why the surface area of a sphere? Because the energy-momentum relation is the equation of a sphere, and the momenta satisfying the energy constraint lie on its surface. For one particle, $$d = 3$$ and $$r = \sqrt{2mU}$$. The total multiplicity is


$$
\Omega = \Omega_x \Omega_p
$$


For $$N$$ particles we use the same approach, but now the position-space volume is $$V^N$$ and the momentum-space dimensionality is $$d=3N$$. Also, we have to account for the fact that the atoms are indistinguishable. To see why, consider a _distinguishable_ three-atom gas. One of its microstate might be


$$
((\mathbf{x},\mathbf{p})_1,(\mathbf{x},\mathbf{p})_2,(\mathbf{x},\mathbf{p})_3)
$$


If the atoms switch places, another, distinct, microstate is


$$
((\mathbf{x},\mathbf{p})_3,(\mathbf{x},\mathbf{p})_1,(\mathbf{x},\mathbf{p})_2)
$$


In this case there are two states to count, but if the particles are indistinguishable then there are no subscripts on the individual states and the first overall state is the same as the second. The way we're calculating $$\Omega$$, however, doesn't account for such _permutation redundancy_, that is unless $$\Omega$$ is divided by $$N!$$ to un-count the redundant states. So really the multiplicity is $$\Omega_x \Omega_p/N!$$.

The final result after dividing by $$N!$$ and approximating for large $$N$$ is


$$
\Omega(U,V,N) = f(N) V^N U^{3N/2}
$$


where 


$$
f(N) = \frac{(2\pi m)^{3N/2}}{h^{3N}N!(3N/2)!}
$$

So much for isolated systems, on to interactions. 

## Interacting Systems

Suppose that two thermodynamic systems interact by exchanging something with eachother. "Something" could be energy, particles, volume, or anything else that's macroscopic. The big question of this section is: what macroscopic state does each system equilibrate to, and why?

__Energy Exchange.__ To start, consider two systems having energies $$U_1$$ and $$U_2$$. As they interact they pass energy back and forth (by assumption), so that at one point in time their energies may be $$(U_1-a, U_2+a)$$, while at another point in time they may be $$(U_1-a', U_2+a')$$, etc. but always $$U_1+U_2 = \text{const.}$$ Do the energies fluctuate forever, or do they reach an equilibrium state?

It turns out that some energy configurations, i.e. macrostates, have more microstates associated with them than others, and because microstates are all equally likely (as per the uniformity assumption), it will ultimately be the macrostate with the most microstates that the system equilibrates to. So let's look at multiplicities.

The multiplicity of the joint system is
$$
\Omega(U_1, U_2) = \Omega_1(U_1) \Omega_2(U_2)
$$
and because of the uniformity assumption, the probability of observing a pair of energies is
$$
P(U_1,U_2) \propto \Omega(U_1, U_2)
$$
If $$\Omega$$ were to be constant, then all macrostates would be equally likely, but remarkably, for systems like those three examples above, $$\Omega$$ tends to be very sharply peaked around a _single_ pair of energies, and the peak is so sharp that no matter when we observe the system we're basically guarantted to observe that pair of energies, despite the fact that the systems continue to exchange energy.



The answer is of course, yes, and the way it's done is based on the uniformity assumption. Recall that the uniformity assumption states that if a system is in equilibrium, then each of its allowed microstates are equally likely to be occupied. This means that if a system's energy value can be associated with more microstates can be used to 





BIG SYSTEMS


$$
\ln \binom{n}{k} \approx \frac{1}{2}\ln(\frac{n}{2\pi k(n-k)}) + n\ln n - k\ln k - (n-k)\ln (n-k)
$$




__Temperature & Energy.__ Temperature is defined as the willingness of a system to exchange energy with another system. Energy exchanged in this way is called _heat_. Any other form of energy transfer is called _work_. Heat and work describe energy _in transit_, so it doesn't make sense to say something like "the coffee cup has a lot of heat", but you can say "the coffee cup has a lot of energy".



__Thermodynamic limit.__ The _thermodynamic limit_ is the regime where fluctuations are negligable relative to the average of whatever quantity is being considered.

__Ensembles.__ Consider two systems $$A$$ and $$B$$ that exchange energy with each other but are otherwise isolated. $$A$$ is in a state $$x_A$$ whose specific details we do not know. For example $$A$$ could be a mole of gas, in which case $$x_A$$ is the position and momenta of all the constituent particles. What we'll assume we do know, however, is the state's energy $$E_A$$. In addition we know that there are many _other_ states that have this same energy, and we denote the number of them by $$\Omega(E_A)$$.

What does this have to do with thermodynamics? There's a principal in thermodynamics which states that:

1. When a system has $$E$$, all of the states having $$E$$ are equally likely to be the one the system is actually in.
2. State transitions are uniformly random.

What this implies is that the system spends a disproportionately large amount of time in states that  $$\Omega(E_A)\Omega(E_B)$$.  
