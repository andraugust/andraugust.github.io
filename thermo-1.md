---
layout: default
---

# Thermal Physics Part I: Statistical Mechanics

<center><img src="statmech/banner.png" style="zoom:100%;"></center>


- [Thermal Physics Part I: Statistical Mechanics](#thermal-physics-part-i:-statistical-mechanics)
  - [Introduction](#introduction)
  - [Pressure & The Kinetic Theory of Gases](#pressure--the-kinetic-theory-of-gases)
  - [Temperature](#temperature)
  - [The Multiplicity of a Gas](#the-multiplicity-of-a-gas)
  - [The Multiplicity of a Solid](#the-multiplicity-of-a-solid)
  - [The Stability of Equilibrium](#the-stability-of-equilibrium)
  - [The Energy of a Single Particle](#the-energy-of-a-single-particle)
  - [Molecules](#molecules)
  - [Exchanging More Than Energy](#exchanging-more-than-energy)
  - [Entropy and a Glimpse of Thermodynamics](#entropy-and-a-glimpse-of-thermodynamics)

## Introduction

If you zoom in closely on any object, you'll see nearly the same thing: countless molecules moving in rapid, random motion.

If the object is a solid, you'll see each molecule stay roughly in place but oscillate as if connected to its neighbors by springs. If the object is a liquid, such as water, you'll see the molecules closely packed but unbound, bouncing off one another and spinning. If the object is a gas it'll appear like the liquid, but with much more space between molecules.

To put some numbers to this picture: a human-scale sample of gas—a liter of air at standard temperature and pressure—contains about $$10^{23}$$ molecules. Each molecule moves at around $$500$$ m/s (about $$1000$$ mph) and collides with another molecule roughly $$10^{10}$$ times per second.

These numbers are so large that to model gases at the human scale, we must use statistics—there’s no way to track each particle individually. Now, it may seem like a compromise to use statistical models, since they provide only estimates, but in fact, the more particles there are in a system, the more deterministic the models become. “More deterministic” in the sense that the probability distributions become very sharply peaked.

**This post is about how macroscopic properties of many-particle systems emerge from the microscopic motion of individual molecules.** 

I’ll start with the emergence of pressure to demonstrate this concept, and then move on to temperature, which introduces the central theme that underlies everything else that follows: 

1. Every microstate (molecular-scale state) is equally likely at any given time
2. Macrostates (such as temperature and pressure) can correspond to many different microstates
3. The probability of a macrostate is therefore determined by counting the number of microstates that produce it (more microstates = more probable macrostate)
4. When there are large numbers of particles, the most probable macrostate is much, much more likely than all others, and is what we observe at equilibrium. 

## Pressure & The Kinetic Theory of Gases

The kinetic theory of gases was one of the first attempts to model gases as large collections of small moving objects. The theory proposes that:

* Gases contain lots of very small particles moving in constant motion
* The particles interact by colliding elastically with each other and the walls of their container
* Macroscopic properties like pressure emerge through the collective interaction of the particles, specifically through momentum transfer
* "Particle" is a general term for the microscopic constituents of bulk matter. Depending on the context a particle can be an atom, a molecule, a photon, or anything else that acts as a "unit of object"

Let's see if we can use these assumptions to connect microscopic particle motion with macroscopic pressure.

Pressure is given by


$$
P = F_x / \Delta A
$$


where $$F_x$$ is the force over an area $$\Delta A$$ perpendicular to a direction $$x$$. Force is related to momentum by $$F_x = \Delta p_x / \Delta t $$, where $$\Delta p_x$$ is the change in a particles $$x$$-momentum when it collides with a wall, and $$\Delta t$$ is the time over which one collision occurs. 

The next step is to calculate $$\Delta t$$ and $$\Delta A$$, and plug them in to get pressure. But collisions happen nearly instantaneously, so $$\Delta t \rightarrow 0 $$, and collision areas are nearly points, so $$\Delta A \rightarrow 0$$, suggesting that pressure isn't well defined. For one particle this is true, but for a continuous density of particles we can create a well defined formula for pressure.

Instead of a single particle, consider a density of particles $$n = N/V$$ having speed density distribution $$f(v_x)$$. The number of particles with speed $$v_x$$ hitting area $$\Delta A$$ over time $$\Delta t$$ is


$$
\frac{n}{2}\ \Delta t\ \Delta A\ f(v_x)\ v_x\ \text{d}v_x
$$


where the factor of one-half is used to only count particles moving toward the area $$\Delta A$$ (half are moving away).

When one particle collides with the wall it's momentum changes by $$2mv_x$$, so for all particles in the density the total momentum change is


$$
\begin{align}
\Delta p_x &= \frac{n}{2}\ 2m\ \Delta t\ \Delta A \int_0^\infty f(v_x) v_x^2\ \text{d}v_x \\
&= nm\ \Delta t\ \Delta A\ \langle v_x^2 \rangle
\end{align}
$$


Plugging this into the formula for pressure and using the isotropy condition


$$
\langle v_x^2 \rangle = \langle v_y^2 \rangle = \langle v_z^2 \rangle = \langle v^2 \rangle / 3
$$


gives the result


$$
P = \frac{1}{3} \frac{N}{V} m \langle v^2 \rangle
$$


This is the formula we're after, it connects microscopic particle motion to macroscopic pressure. Taking things a step further, we can associate $$m \langle v^2 \rangle$$ with twice the average kinetic energy of a particle and write 


$$
PV = 2U/3
$$


where $$U$$ is the total internal energy of the gas (not counting constant offsets like ground-states which don't change in the processes considered here), so now we can calculate a gas's energy by simply knowing its pressure and volume, which is pretty useful.

As mentioned earlier, particles don't have to be atoms. If they're photons, for example, we can derive a similar expression by removing mass from the equation:


$$
\langle m v^2 \rangle \rightarrow \langle \mathbf{p} \cdot \mathbf{v} \rangle = pc = E_{\text{photon}}
$$


So for a photon gas $$PV = U/3$$. 

## Temperature

Of all the quantities in thermodynamics, temperature is probably the most intuitive---we experience it constantly. But what is temperature objectively? We know that when two systems exchange energy for long enough they reach a point where their "temperature" is the same. So let's imagine what happens when two gases exchange energy, then see what we can derive about their equilibrium state.

Imagine two gas chambers with a wall between them. The wall allows energy to pass from one gas to the other through random molecular collisions while preventing any particles from moving between chambers. In otherwords, the gases only exchange energy. If the energy of each gas is $$U_1$$ and $$U_2$$, the total system energy is


$$
U = U_1 + U_2
$$

To figure out what $$U_1$$ and $$U_2$$ are at equilibrium, we need to introduce the concept of a _microstate_. A microstate is simply the gas's configuration. If the gas is modeled classically, its microstate is a point in phase space $$(\mathbf{x}_1, \mathbf{p}_1, \mathbf{x}_2, \mathbf{p}_2..., \mathbf{x}_N, \mathbf{p}_N)$$, where $$i=1 \ldots N$$ indexes particles. If the gas is modeled quantum mechanically, its microstate is a vector in Hilbert space $$\Psi(\mathbf{x}_1, \mathbf{x}_2, ... \mathbf{x}_N)$$ satisfying whatever Hamiltonian happens to the govern the dynamics.

With the concept of a microstate in hand, we can now write down the fundamental assumptions of statistical mechanics:

* Microstates evolve continually (the system isn't frozen---it moves through phase space)
* Given enough time, a system will explore all the microstates available to it, spending an equal amount of time in each
* If the microstate of a system is measured, each one has an equal probability of being observed

This last assumption is extremely useful. It allows us to write


$$
p(U_1,U_2) \propto \Omega(U_1, U_2) = \Omega_1(U_1) \Omega_2(U_2)
$$


where $$p(U_1,U_2)$$ is the probability that the total energy $$U$$ is divided such that the first gas has $$U_1$$ and the second gas contains has $$U_2$$. Meanwhile, $$\Omega$$ is the number of microstates corresponding to a particular energy. This function is called the _multiplicity_, and it's indexed for each system because in general it can depend on volume and population, which may differ between the systems.

Now, although the gases can divide their energy any way satisfying $$U_1 + U_2 = U$$, some divisions are more likely than others because they have more microstates associated with them. In fact, $$p$$ is very sharply peaked around one specific energy division which, not surprisingly, is _thermal equilibrium_. Let's find this division.

The multiplicity maximum is found through differentiation:


$$
\begin{align}
\frac{d\Omega}{dU_1} &= \Omega_2\frac{d\Omega_1}{dU_1} + \Omega_1\frac{d\Omega_2}{dU_2}\frac{dU_2}{dU_1} \\
&= \Omega_2\frac{d\Omega_1}{dU_1} - \Omega_1\frac{d\Omega_2}{dU_2} \\
&= 0
\end{align}
$$


which is the same as


$$
\frac{\partial \ln\Omega_1}{\partial U_1} = \frac{\partial \ln\Omega_2}{\partial U_2}
$$


I've switched to partial derivatives because in general $$\Omega$$ can depend on $$N$$ and $$V$$, but those quantities are held constant through the interaction. This equation defines the energy division where the joint system has the most microstates. As such, it's the most likely energy division, and therefore _defines_ thermal equilibrium. It follows that temperature should be defined as


$$
\frac{1}{kT} = \frac{\partial \ln\Omega}{\partial U}
$$


where $$k \approx 10^{-23} \ \text{J/K}$$ is the _Boltzmann constant_ that simply sets the scale for temperature in energy units. This is the objective definition of temperature we set out to derive. 

Let's use this formula to find the temperature of a gas.

## The Temperature of a Gas

To derive $$\Omega$$ for an $$N$$-atom gas, it's easiest to start with $$N=1$$ and then generalize. For one atom, the system's microstate is given by the atom's position and momentum $$(\mathbf{x},\mathbf{p})$$, where $$\mathbf{x}$$ is constrained within a volume $$V$$, and $$\mathbf{p}$$ is constrained by the gas's energy according to


$$
U = \frac{1}{2m}\lvert \mathbf{p} \rvert ^2
$$


Here I'm assuming the atom doesn't rotate or vibrate: all its energy is translational. If we were modeling molecules we would have to account for rotations and vibrations, which I'll do later on.

Since $$\mathbf{x}$$ and $$\mathbf{p}$$ are independent, the total multiplicity factors into


$$
\Omega = \Omega_\mathbf{x} \Omega_\mathbf{p}
$$


Classically, a single particle can occupy continuous positions and momenta as long as the energy and volume constraints are satisfied. But this would imply that multiplicity is infinite. Quantum mechanically, however, there's a limit to the simultaneous "resolution" of $$\mathbf{x}$$ and $$\mathbf{p}$$. In particular, they're limited to have $$\Delta x_i \Delta p_i = \hbar/2$$, where $$i$$ indexes the three spatial dimensions. So if we imagine phase space as being chopped into a grid of $$\Delta x$$s and $$\Delta p$$s at this limit, then microstates become countable and finite (even though there may be _a lot_ of them).

With this quantization, the number of position states is


$$
\Omega_x = \frac{V}{\Delta x_1 \Delta x_2 \Delta x_3}
$$


and the number of momentum states is


$$
\Omega_p = \frac{S_d(r)}{\Delta p_1 \Delta p_2 \Delta p_3}
$$


Where $$S_d(r)$$ is the surface area of a sphere of radius $$r$$ and dimension $$d$$. Why the surface area of a sphere? It's because the energy-momentum relation is the equation of a sphere and the momenta satisfying the energy constraint lie on its surface.

For $$N > 1$$ the approach is the same, but now position-space volume is $$V^N$$ and momentum-space dimensionality is $$d=3N$$. Also, we have to account for the fact that atoms are indistinguishable. To see why, consider a _distinguishable_ three-atom gas. One of its microstate is


$$
((\mathbf{x}_1,\mathbf{p}_1),(\mathbf{x}_2,\mathbf{p}_2),(\mathbf{x}_3,\mathbf{p}_3))
$$


If the atoms switch places they'll have another, distinct, microstate such as


$$
((\mathbf{x}_3,\mathbf{p}_3),(\mathbf{x}_1,\mathbf{p}_1),(\mathbf{x}_2,\mathbf{p}_2))
$$


In this case there are two states to count, but if the particles are indistinguishable then there are no subscripts on the individual states and the first overall state is the same as the second. The way we're calculating $$\Omega$$, however, doesn't account for such _permutation redundancy_, that is unless $$\Omega$$ is divided by $$N!$$ to "un-count" the redundant states. So the correct multiplicity for indistinguishable particles is $$\Omega_x \Omega_p/N!$$.

The result is


$$
\Omega = \frac{V^N}{N!}\frac{2\pi^{3N/2}}{h^{3N}\ \Gamma (\frac{3N}{2})} \left(\sqrt{2mU}\right) ^{3N-1}
$$


In the limit of large $$N$$ this simplifies to


$$
\Omega = f(N) V^N U^{3N/2}
$$


where


$$
f(N) = \frac{(2\pi m)^{3N/2}}{h^{3N}N!\ \Gamma (3N/2)}
$$


Now we can get the gas's temperature by take the partial derivative of $$\ln \Omega$$ with respect to energy. The result is


$$
kT = \frac{PV}{N} = \frac{2}{3}\frac{U}{N}
$$


The first equality is the so-called _ideal gas law_, and the second equality says that temperature is proportional to the average energy per particle, which is an intuitive connection between temperature and energy.

## The Temperature of a Solid

To find the temperature of a solid, we can use a simple solid model called the *Einstein solid*. In the model, atoms are connected via springs into a cubic lattice. The springs are assumed to be identical, so their frequency parameters $$\omega$$ are all the same, and they're treated quantum mechanically so their energy is an integer multiple of $$\hbar \omega$$, which we'll take to be the energy units.

Since atoms are arranged in a cubic lattice, there are three oscillators per atom. We'll let $$N$$ refer to the number of oscillators instead of the number of atoms because the oscillators are what "have" the energy. The total energy $$U$$ of the solid (relative to the ground state) is just the total number of energy units in all the oscillators.

The microstate of an Einstein solid is a list of each oscillator's energy. For example, if $$U=5$$ and $$N=3$$, some allowed microstates are $$(2,0,3)$$ and $$(1,1,3)$$, etc. This leads to the multiplicity function


$$
\Omega = \begin{pmatrix} U+N-1 \\ U \end{pmatrix} \approx \frac{(U+N)^{U+N}}{U^U {N}^{N}}
$$


where the approximation is for large $$N$$ and $$U$$. Calculating $$\partial \ln\Omega / {\partial U}$$ gives


$$
kT = \frac{1}{\ln(1+\frac{N}{U})}
$$


In the high-energy limit when $$U \gg N$$ this simplifies to


$$
kT \approx \frac{U}{N}
$$


So at high energy the temperature is again proportional to the average energy per particle.

## The Stability of Equilibrium

Earlier I said that the joint multiplicity of two systems is sharply peaked around one energy division, which we called thermal equilibrium. The reason it's called _equilibrium_ is because the number of microstates around this particular division is so large that the system effectively spends all of its time there. Now that we have the gas's multiplicity function let's verify this.

To simplify, assume that the two interacting gases have the same population and volume, so the joint multiplicity is

$$
\Omega(u) = f(N)^2V^{2N}(u\ (U-u))^{3N/2}
$$


In terms of notation I'm calling system $$1$$'s energy $$u$$ instead of $$U_1$$ just to clarify the fact that it's an independent variable. Taking the derivative of $$\Omega$$ with respect to $$u$$ and setting it equal to zero gives the equilibrium point at $$u = U/2$$, which is an equal division of energy. This is an intuitive result because the gases have the same volume and population. Less intuitive is how sharply peaked the multiplicity function is around this division, and that's key to understanding why the system is stable there, so let's figure that out next.

Taking the Taylor series of $$\Omega$$ around the point $$u = U/2$$ gives


$$
\Omega(u) \sim \exp \left( -\frac{6N}{U^2} \left(u-\frac{U}{2} \right)^2 \right)
$$


Apparently, near equilibrium, the multiplicity function is Gaussian with mean $$U/2$$ and variance like $$U/\sqrt{N}$$. 

As a mathematical aside, I'll note that polynomial approximations like Taylor series are only accurate when the function being approximated changes fairly slowly (like a polynomial) around the point of interest. Multiplicities tend to change very quickly, so it's best to approximate their logarithm and then exponentiate to get the final result. For example, if a function $$f(x)$$ changes quickly near $$x_0$$, its best to use


$$
\ln f(x) \approx \ln f(x_0) + \frac{f'(x_0)}{f(x_0)}(x-x_0) - \frac{1}{2}\frac{f''(x_0)}{f(x_0)^2}(x-x_0)^2 + \ldots
$$


and then take the exponent of the series to recover the approximation for $$f(x)$$.

OK back to the physics... because $$u$$ can have any value from $$0$$ to $$U$$, the width of $$\Omega$$ relative to the energy scale is $$1/\sqrt{N}$$. This means that if there are $$10^{23}$$ particles in the system, only about $$10^{-10}\%$$ of possible energy divisions have a reasonable likelihood of occurring, and those divisions are all centered around $$U/2$$. In other words, thermal equilibrium is very, very stable.

## The Energy of a Single Particle

In the section on temperature I described two systems exchanging energy and treated the systems like they operated on similar energy scales. But often times one system is so much larger than the other that the energy it gains or loses is negligible compared to the smaller system.

For example, if the smaller system is a single atom in a gas and the larger system is the rest of the gas, the single atom will exchange energy with the gas through random collisions, but the energy change of the gas is approximately zero relative to its total energy. Let's see if we can derive the energy distribution of a single atom (or whatever the small system may be) in this context.

The approach here is the same as in the temperature derivation: two systems have multiplicities $$\Omega_1(u)$$ and $$\Omega_2(U-u)$$, they exchange energy, and the probability of measuring the small system with energy $$u$$ is $$p(u) \propto \Omega_1(u)\Omega_2 (U-u)$$. I'm calling the small system $$1$$ and the big system $$2$$.

A natural starting point is to do a Taylor series on $$\Omega_2$$ under the assumption $$u \ll U$$. This assumption is valid but, as mentioned earlier, Taylor series aren't accurate for multiplicities, so the series is applied to the logarithm of $$\Omega$$:


$$
\begin{align}
\ln \Omega_2(U-u) &\approx \ln \Omega_2(U) - u\frac{1}{\Omega_2}\frac{d\Omega_2}{du} \\
&= \ln \Omega_2(U) - \frac{u}{kT_2}
\end{align}
$$


and so


$$
p(u) \propto \Omega_1(u)\ \Omega_2 (U)\ e^{-u/kT_2}
$$


The factor $$\Omega_2 (U)$$ is a constant that can be absorbed into the proportionality, and it's generally understood that $$T_2$$ is the temperature of the larger system (sometimes called the _heat bath_ or _thermal reservoir_), so the subscript is dropped. The result is


$$
p(u) = \frac{1}{Z} \Omega(u)\ e^{-u/kT}
$$


where $$Z$$ is a normalizing constant called the _partition function_. It's given by


$$
Z = \int_0^\infty \Omega(u)\ e^{-u/kT}\ \text{d}u
$$


In cases where $$u$$ has discrete values the integral becomes a sum.

$$p(u)$$ is the energy distribution of the small system (sometimes just one particle), $$\Omega(u)$$ is the so-called _density of states_ which counts the degeneracy of $$u$$, and $$\exp(-u/kT)$$ is the so-called _Boltzmann factor_ which implies that high energy states are less likely. Let's apply this formula to one atom in a gas.

An atom's energy degeneracy comes from the fact that it has many momentum states with the same energy: $$p_x^2+p_y^2+p_z^2 = 2mu$$. This equation defines the surface of a sphere having radius $$R = \sqrt{2mu}$$, so the volume of states centered at a given energy is $$A\ dR$$, where $$A$$ is the surface area of the sphere. In terms of energy this means


$$
\Omega(u) = A\ dR \propto \sqrt{u}
$$


therefore


$$
p(u) \propto \sqrt{u} e^{-u/kT}
$$


and with the normalization constant:


$$
p(u) = \frac{2}{(kT)^{3/2}\sqrt{\pi}} \sqrt{u} e^{-u/kT}
$$


The average energy is


$$
\langle u \rangle = \int_0^\infty u\ p(u)\ \text{d}u = \frac{3}{2}kT
$$


This is the exact same result as in the temperature derivation but with $$\langle u \rangle$$ in place of $$U/N$$. 

This derivation is based on the classical model of an atom's energy. Is it consistent with the quantum model? In the quantum model the atom's energy is


$$
u(n_x, n_y, n_z) = n_x^2 + n_y^2 + n_z^2
$$

where each $$n$$ is a positive integer starting at $$1$$ and the energy units are $$h^2/8mV^{2/3}$$. Degeneracy comes from the fact that different integer combinations can produce the same energy. For example, $$u(2, 1, 1) = u(1,2,1) = u(1,1,2) = 6$$, so $$\Omega(6)=3$$. Similarly $$\Omega(7)=0$$, $$\Omega(12) = 1$$, etc. 

The quantum multiplicity is not smooth like the classical one, but the difference between consecutive energy levels is only about one energy unit (sometimes two or three, depending on the level), so if 

$$
kT \gg \frac{h^2}{8 m V^{2/3}}
$$


then the quantized levels will appear continuous. For a hydrogen atom in a $$1\ \text{m}^3$$ container at room temperature, $$kT_\text{room} \approx 0.026\ \text{eV}$$, while $$h^2/8mV^{2/3} \approx 10^{-23}\ \text{eV}$$, so the atom definitely behaves classically.

The next example is an oscillator, like the ones in the Einstein solid. Quantum oscillators have energy levels given by $$u_n = n + 1/2$$, where $$n$$ is a positive integer starting at zero and the energy is in units of $$\hbar \omega$$. Each energy level has a unique value of $$n$$ associated with it, so $$\Omega = 1$$. Plugging this into the energy probability formula yields


$$
p(n) = (1-e^{-1/kT})e^{-n/kT}
$$


The average energy is


$$
\langle u \rangle = \sum_{n=1}^\infty n\ p(n) = \frac{1}{1-e^{-1/kT}}
$$


In the high-temperature limit this becomes $$kT+1/2$$, which, aside from the ground-state offset, is the same result we obtained previously for the Einstein solid.

At this point $$1/kT$$ has appeared frequently enough to get its own label:


$$
\beta \equiv 1/kT
$$


With this definition there's a nice trick for calculating $$\langle u \rangle$$ in terms of $$Z$$ and $$\beta$$. The trick is


$$
\langle u \rangle = - \frac{1}{Z}\frac{\partial Z}{\partial \beta}
$$


## Molecules

We now have the tools we need to model simple molecules. In the context of statistical mechanics the main difference between molecules and atoms is that molecules have more places to "put" their energy: they can rotate, oscillate and translation, while atoms can only translate. For example, if we model a diatomic molecule classically as two point masses connected by a spring, its energy is


$$
u = \sum_{x,y,z}\frac{p_i^2}{2m} + \sum_{i=1}^3 \frac{L_i^2}{2I_i} + \frac{1}{2}\mu \dot r^2 + \frac{1}{2}\mu \omega^2 (r - r_0)^2
$$


where

* $$L_i$$ are the three principal angular momenta, and $$I_i$$ are the corresponding interial moments
* $$\mu$$ is the reduced mass of the two atoms, and $$\omega$$ is the spring oscillation parameter
* $$r$$ is the separation between the two atoms, and $$r_0$$ is their resting (non-vibrating) separation

This is a complicated formula compared to that of a single atom, so counting the number of degenerate energies is difficult: we would need to find the surface area of a $$d$$-dimensional spheroid, which unfortunately doesn't have a general formula like a $$d$$-dimensional sphere does. Luckily though, we don't need to know the exact surface area of the spheroide to calculate $$\langle u \rangle$$. The reason is that the surface area of a spheroid is given by $$G\rho^{d-1}$$, where $$G$$ is a constant related to geometry and $$\rho$$ is the spheroid's radius parameter.

Looking at the formula for energy, $$\sqrt{u}$$ plays the role of $$\rho$$, and $$d$$ is the number of quadratic terms on the right side of the equation. As for the geometry constant $$G$$, we don't have to worry about it because it ends up canceling.

Starting with


$$
Z = \int_0^\infty \Omega(u)\ e^{-\beta u}\ \text{d}u
$$


We have 


$$
\begin{align}
\Omega(u)\ \text{d}u &= (\text{Surface Area}) *d(\text{Radius}) \\
&= u^{(d-1)/2} u^{-1/2} \text{d}u\\
&= u^{(d-2)/2} \text{d}u
\end{align}
$$


The partition function becomes


$$
\begin{align}
Z &= \int_0^\infty u^{(d-2)/2} e^{-\beta u} du \\
&= \Gamma(d/2)\ \beta^{-d/2}
\end{align}
$$


Plugging this into the formula at the end of the previous section gives the result:


$$
\langle u \rangle = \frac{d}{2}kT
$$


Interestingly, this says that on average energy gets distributed evenly to each of the particle's quadratic "degrees of freedom". Despite each of these degrees having unique characteristics like inertial moments and reduced mass they each get the same $$kT/2$$ worth of energy on average. 

This result is called the _equipartition theorem_, and it gives insight into the observation that different substances can require different amounts of energy to change their temperature by the same amount. For example, to raise the temperature of monatomic helium gas by $$1\text{K}$$, you have to add $$3k/2$$ units of energy per particle, whereas $$\text{O}_2$$ gas requires more---$$5k/2$$ units of energy per particle. This is because monatomic helium has three degrees of freedom, while diatomic $$\text{O}_2$$ has three translational plus two rotational degrees of freedom. The diatomic gas has more ways to store energy, a property called _heat capacity_.

In this example, for the $$\text{O}_2$$ molecule, I didn't count the third rotational degree of freedom or the two spring degrees of freedom. The reason is that the third rotation axis is co-linear with the atomic bond, and due to quantum mechanics this means it doesn't store energy. Meanwhile, the spring degrees of freedom weren't counted because at room temperature nearly all molecules are "frozen" in the ground-state: the gap between oscillation energies for $$\text{O}_2$$ is about $$0.2\ \text{eV}$$, while room temperature thermal energy is much lower, $$kT_\text{room} \approx 0.026\ \text{eV}$$, so the number of molecules in the first excited-state relative to the number in the ground-state is


$$
\frac{N_1}{N_0} = e^{-(u_1-u_0)/kT_\text{room}} \approx 10^{-4}
$$


This same line of reasoning can be used to understand why I haven't considered electronic energy levels in any of these calculations: the energy gap between the ground-state and first excited state of the hydrogen electron, for example, is about $$10\ \text{eV}$$, which is far beyond what room temperature thermal energy is likely to provide.

## Exchanging More Than Energy

So far, nearly the entire discussion has focused on systems exchanging energy. What happens when they exchange other things, like volume and particles?

Like energy, other quantities equilibrate when they maximize multiplicity. For a general set of variables, the joint multiplicity is


$$
\Omega = \Omega_1(X_1, Y_1, ...,Z_1)\ \Omega_2(X_2, Y_2, ..., Z_2)
$$


with the constraint that each pair of variables is conserved: $$\xi_1 + \xi_2 = \text{const}$$. Maximizing $$\Omega$$ gives an equilibrium condition for each variable:


$$
\frac{\partial \ln \Omega_1}{\partial \xi_1} = \frac{\partial \ln \Omega_2}{\partial \xi_2}
$$


When dealing with energy, dimensionality analysis identified temperature as inversely proportional to these derivatives. Can we do something similar for volume and population?

For volume, the equilibrium condition is


$$
\frac{\partial \ln \Omega}{\partial V}
$$


We know that the equilibrating quantity for volume is pressure, but the units of this derivative are inverse-volume, so we expect


$$
P = c\frac{\partial \ln \Omega}{\partial V}
$$


where $$c$$ has units of energy. What is $$c$$? If we look at the ideal gas, it has $$\Omega \propto V^N$$, so $$\partial \ln \Omega / \partial V = N/V$$. But the ideal gas law says $$N/V = P/kT$$, therefore


$$
P = kT\frac{\partial \ln \Omega}{\partial V}
$$


which has the correct units and turns out to be the correct equilibrium condition for volume exchange.

For population, the equilibrium condition is


$$
\frac{\partial \ln \Omega}{\partial N}
$$


Turning again to dimensional analysis and the known multiplicity of an ideal gas, the population equilibrium turns out to be


$$
\mu = -kT\frac{\partial \ln \Omega}{\partial N}
$$


where $$\mu$$ is the so-called _chemical potential_. The negative sign is a convention used to make particles prefer systems with lower chemical potential.

## Entropy and a Glimpse of Thermodynamics

Now is finally the time to step into the thermodynamic realm and define a major link between thermodynamics and statistical mechanics, _entropy_:


$$
S = k \ln \Omega
$$


It's mathematical properties are straightforward but important:

* $$S$$ is monotonic, so maximizing $$\Omega$$ implies maximizing $$S$$, and vice versa. This means that $$\Omega$$ and $$S$$ share equilibria.
* $$S \ge 0$$ because $$\Omega \ge 1$$.
* The entropy of a joint system is the sum of its subsystems: $$S_{\text{total}} = \sum_i S_i$$

Entropy is special for many reasons, but here it's important because it ties together all the results from the previous section:


$$
\begin{align}
dS &= \frac{\partial S}{\partial U}\ dU + \frac{\partial S}{\partial V}\ dV + \frac{\partial S}{\partial N} \ dN \\
&= \frac{1}{T}\ dU + \frac{P}{T}\ dV + \frac{\mu}{T}\ dN
\end{align}
$$


Rearranging for energy:


$$
dU = T\ dS - P\ dV +\mu\ dN
$$


This is the so-called _thermodynamic identity_. It demonstrates how the change in a system's energy can be decomposed into contributions from heat, mechanical work and chemical work. With no direct reference to $$\Omega$$, this formula is firmly in the domain of thermodynamics where processes are framed in terms of macrostates like $$T$$ and $$P$$ rather than the underlying microstates which give rise to them. 

In a future set of notes I'll talk about thermodynamics more thoroughly. Stay tuned...



{% include disqus.html %}