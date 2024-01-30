## Statistical Thermodynamics

Statistical thermodynamics explores the way in which the thermal properties of a system emerge from the elementary objects that make it up. If the system is an air-filled balloon, for example, it's thermal properties are things like temperature, pressure and volume, while its elementary objects are the atoms and molecules making up the gas and the balloon itself.

Thermal properties are relatively intuitive—we can feel the difference between hot and cold, we can see steam rising from a boiling pot of water, and we can watch a helium balloon pull on whatever it's attached to. But that these things should occur due to the motion of atoms is far from obvious, and if we tried to predict any of them using classical or quantum mechanics directly we wouldn't get very far—there are too many objects to consider.

How many objects? A mole is the typical scale used to measure the number of objects in thermal systems, it's about $$10^{23}$$. To get a feel for this number, a mole of gas occupies about $$22$$ liters at standard temperature and pressure. To classically represent a mole of gas, we would have to list each atom's position and momentum—about $$10^{23}$$ numbers in total. This is an absurdly large number of numbers. It would take about $$10^9$$ supercomputers-worth of storage space to represent them all. Imagine the energy required to propogate the state one step forward in time, let alone accurately capture all of the relevant forces—it's not happening.

Instead of tracking every atom in the gas, it's much more practical to compute a small number of functions of its state and get a manageable number of bulk properties such as temperature, pressure and energy. But this raises a question: if we're calculating functions of state, don't we need to know the state? The answer is technically yes, but practically no. Practically no because, as we'll see, when thermal systems come to equilibrium, quantities such as pressure, temperature and energy are effectively constant even though the underlying states that define them are constantly changing.

Before going further, I'll mention that the word _state_ can be ambiguous in stat-thermo. It could refer to the state of macroscopic variables, like temperature and pressure, or it could refer to the configuration of the system, like the position and momenum of atoms (which is what I've been calling state so far). To disambiguate, configurations are called _microstates_ (even though they may be bigger or smaller than a micron) and macroscopic states are called _macrostates_. If I say "state" without a prefix, it should be clear from context which one it is, but I'll always try to include the prefix.

Also, the word _thermodynamics_ should be defined. Thermodynamics is about thermal things changing, like when energy is absorbed, or pressure increases, etc. But changes are assumed to happen in a special way. They happen such that the system can be _treated_ like it's in equilibrium at all times, even though it really is changing. The way to accomplish this so-called "quasi-static" change is by evolving the system _very_ slowy, so slowly that after every infinitesimal change the system has enough time to settle to equilibrium before changing further. The reason for doing this is because we want to treat thermal properties as constant throughout the system. For example, if we decrease the volume of a gas, initially its pressure will be higher near the surface that's contracting, so pressure becomes a function of position, which is fine except that thermodynamics associates _a_ (one) pressure, volume, etc., with the system, so we let the new pressure spread uniformly before doing any analysis. (Footnote—I was tempted to synonymize "dynamic equilibrium" with quasi-static due to the system being in equilibrium throughout its dynamics, but really dynamic equilibrium means something different.)

Now, in order to start _doing_ thermodynamics, we need its fundamental postulate: 

> In thermal equilibrium, each microstate of a system is equally likely to be observed at all times.

From a classical mechanics perspective this sounds wrong. In CM, microstates follow a single deterministic trajectory through phase space, one determined by the system's initial conditions and whatever forces are involved—state-transition probabilities are delta functions along the system's one and only trajectory, not uniform distributions over phase space. How do we get away with this postulate? Well, it's a postulate, so it can say whatever it wants to say!…just as long as it corresponds with physical reality. And as I'll show throughout this post, for large systems like those in thermodynamics, it does.


### Isolated Systems

Isolated systems are a simple starting point. What can we say about them? We can say they have a number of particles $$N$$, a total energy $$U$$, and perhaps there are some constraints, like that the system is inside a volume $$V$$. Given these things we can calculate (or try to calculate) the number of ways that $$U$$ can be split amongst the system's particles while satisfying any constraints. This number, called the system's multiplicity $$\Omega$$, is the number of microstates available to the system, it plays an important role in determining which macrostate the system equilibrates to when it undergoes dynamics.

To get a feel for $$\Omega$$ I'll calculate it for three example systems, then in the next section I'll show how it determines equilibrium states. The three example systems are a magnet, a solid, and a gas.

__The Magnet.__ A simple model of a magnet is the two-state paramagnet. Its "particles" are dipole moments that align either with or against an external magnetic field. If we use energy units of $$\mu B$$, where $$\mu$$ is each dipole's moment (the same for all dipoles) and $$B$$ is the exteral field, then the energy of an aligned dipole is $$-1$$ and the energy of an anti-aligned dipole is $$+1$$ (so dipoles want to align with the field).

The total energy is


$$
U = N_\uparrow-N_\downarrow = N-2N_\downarrow
$$


where $$N_\downarrow$$ and $$N_\uparrow$$ are the number of aligned and anti-aligned dipoles, and $$N=N_\downarrow+N_\uparrow$$ is the total number of dipoles.

A microstate for this system is specified by a binary list of each dipole's alignment, for example $$(\uparrow,\downarrow,...,\downarrow)$$. Macrostates are aggregate functions of microstates—things like $$U$$, $$N_\uparrow$$, and the total magnetization $$M$$ are macrostates.

The multiplicity is


$$
\Omega(N_\downarrow) = \begin{pmatrix} N \\ N_\downarrow \end{pmatrix}
$$


or in terms of energy and number of particles,


$$
\Omega(U,N) = \frac{N!}{\frac{N-U}{2}!\frac{N+U}{2}!}
$$

Note that the fractions in the denominator actually work out to be integers because adding or subtracting a particle always changes the energy by one unit.

For large $$N$$ and $$N \gg N_\downarrow$$ (the high energy limit) this simplifies to
$$
\left( \frac{Ne}{N_\downarrow} \right)^{N_\downarrow}
$$
__The Solid.__ A simple model of a solid is the Einstein solid. Its "particles" are spring-like oscillators that connect atoms into a cubic lattice. Oscillators are defined as identical so they have the same frequency parameter $$\omega$$, and they're treated quantum mechanically so their energy is in units of $$\hbar \omega$$.

The total energy of the oscillators (relative to the ground state) is just the total number of energy units in the system: $$U$$.

A microstate is specified by listing each oscillator's energy. For example, if there are 5 energy units and 3 oscillators, possible microstates are $$(2,0,3)$$ or $$(1,1,3)$$, etc. 

The multiplicity is


$$
\Omega(U,N) = \begin{pmatrix} U+N-1 \\ U \end{pmatrix}
$$


For large $$N$$ and $$U$$ this is approximately


$$
\frac{(U+N)^{U+N}}{U^U N^N}
$$


In the high-energy limit where $$U \gg N$$ this further approximates to


$$
\left( \frac{Ue}{N} \right)^N
$$


__The Gas.__ A simple model of a gas is the ideal gas. It's a gas at low density and high energy such that its atoms scatter elastically off each other and off the walls of the container they're in. As it turns out, many gases fall within this regime, so it's an incredibly useful model.

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


If the atoms switch places they'll have another, distinct, microstate such as


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


That's it for isolated systems, on to interactions. 

### Interacting Systems

Suppose that two thermodynamic systems interact by exchanging something with each other. "Something" could be energy, particles, volume, or any other macro-variable that's exchangeable. The question of this section is: do the systems equilibrate, and if so what's the equilibrium macrostate?

__Energy Exchange.__ To start, consider two systems having energies $$U_1$$ and $$U_2$$ that interact by exchanging energy. Throughout their interaction each system's energy fluctuates due to each one giving and gaining energy to the other randomly, but in a way which conserves the total $$U=U_1+U_2 = \text{const}$$. After the systems interact for a while, what are their energies? 

According to the uniformity assumption, the probability of observing a pair of energies is


$$
P(U_1,U_2) \propto \Omega(U_1, U_2) = \Omega_1(U_1) \Omega_2(U_2)
$$


So the more microstates associated with an energy macrostate, the more likely the system is to have that macrostate. Let's see how this works out for a pair of Einstein solids.

The joint multiplicity of two Einstein solids is


$$
\Omega(U_1, U_2) = \left( \frac{U_1e}{N_1} \right)^{N_1} \left( \frac{U_2e}{N_2} \right)^{N_2}
$$


This multiplicity function turns out to be shaped like a Gaussian that's peaked around the point where 


$$
\frac{N_1}{N_2} = \frac{U_1}{U_2}
$$


So energy is shared equally when the systems have the same number of particles, otherwise it's biased toward the system having more particles—remember these "particles" are quantum oscillators, and this result shows that the equilibrium energy per oscillator is constant.

How sharp is the Gaussian's peak? Fitting a Gaussian to $$\Omega$$, we find that it has a standard deviation of $$\sigma=U/\sqrt{N}$$, where $$N=N_1+N_2$$. This is the number of macrostates the joint system is expected to occupy as the two sub-systems exchange energy. Relative to the entire energy scale it's just $$1/\sqrt{N}$$, so for one mole only about $$10^{-9}$$ percent of macrostates actually get occupied, making the peak effectively the _only_ macrostate we expect to observe. In otherwords, eq. 18 is the answer to the question "after the systems interact for a while, what are their energies?".





* Do the same thing for ideal gas and paramagnet
* Volume exchange and particle exchange

* Conclusion: there's one equilibrium state. 
* For a general exchange, do differentiation and get the thermodynamic identity.
* Free energies
* Boltzmann distribution
* Partition functions
* Quantum





### Approximations

For large $$n$$


$$
n! \approx \sqrt{2\pi n} \left(\frac{n}{e}\right)^n
$$


For large $$n$$ and $$k$$


$$
\ln \binom{n}{k} \approx \frac{1}{2}\ln(\frac{n}{2\pi k(n-k)}) + n\ln n - k\ln k - (n-k)\ln (n-k)
$$



__Temperature & Energy.__ Temperature is defined as the willingness of a system to exchange energy with another system. Energy exchanged in this way is called _heat_. Any other form of energy transfer is called _work_. Heat and work describe energy _in transit_, so it doesn't make sense to say something like "the coffee cup has a lot of heat", but you can say "the coffee cup has a lot of energy".

