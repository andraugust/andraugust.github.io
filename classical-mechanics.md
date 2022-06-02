---
layout: default
---

# TLDR: Classical Mechanics

<center><img src="classical-mechanics/banner.png" style="zoom:80%;"></center>

The first book in the Theoretical Minimum series is on classical mechanics. It starts with a discussion of states and dynamics and then derives the Lagrangian and Hamiltonian formulations. Along the way it connects symmetries to conservation laws and Liouville's theorem to determinism. In this post I summarize the book and capture the pieces I found most interesting.

### Lecture 1: The Nature of Classical Physics

Classical mechanics is about identifying and characterizing the motion of objects for which quantum effects are ignorable. The main subfields of CM are Newtonian motion, classical electromagnetism, and general relativity. This book covers Newtonian motion and a little bit of classical electromagnetism.

Dynamics in CM are defined in terms of states and their transitions. For closed systems, all states within a trajectory have a unique predecessor state and a unique successor state. In other words, dynamics are deterministic and information is conserved. Once a state (such as an initial condition) and all forces acting on the system are defined, the entire future and past of the system are determined. Leonard calls this the _Minus First Law_, due to the priority it should take in how fundamental it is to physics. 

CM systems are deterministic. But many are chaotic. So if initial states and forces can't be known with sufficiently high precision, then _in practice_ is it fair to say they're deterministic?

### Lecture 2: Motion

This lecture is about basic ODEs and their solutions.

### Lecture 3: Dynamics

This lecture covers Newton's formulation of motion and gives an intro to PDEs. Newton's formulation defines motion for a single particle as the solution to the second order ODE $$F=m\ddot{x}$$. This equation is generally solved by inputing $x(0)$, $\dot{x}(0)$, and $F$, and then integrating forward in time. Note that the initial condition time of $0$ is arbitrary, it could have been any number, and sometimes it's called $t_0$ to make this point more explicit.

### Lecture 4: Systems of More Than One Particle

For a system consisting of a single particle, we define the state at time $t$ as the vector $(x(t),\dot{x}(t))$. This vector, along with the dynamics law (encoded by $F = m\ddot{x}$), tells us everything we need to know about the system's evolution; this vector defines the particle's _state_.

For a system of more than one partice, the approach is the same, but now we have an $x$ and an $\dot{x}$ for each particle. For a system of $N$ particles moving in 3-space, the state vector has $6N$ entries, and we can think of the system as following a single trajectory through $6N$ dimensional state-space, while each individual particle follows a trajectory through $6$ dimensional space. 

As an alternative to expressing a system's state in terms of $x$s and $\dot{x}$s, we can express it in terms of $x$s and $p$s. The reason we can do this is because the dynamics equation $F=m\ddot{x}$ is equivalent to $F=\dot{p}$, which formulates a particle's trajectory as $(x(t),p(t))$ with initial conditions $x(0)$ and $p(0)=\dot{x}(0)/m$. This space, where one axis is $x$ and the other axis is $p$ is called _phase_ space. The reason we would want to use phase-space instead of state-space is because sometimes objects don't have mass (e.g. photons) and phase space allows us to avoid defining dynamics explicitly in terms of mass. Also, the Lagrangian and Hamiltonian formulations deal directly with momentum, so it's more natural to work with momentum instead of velocity as a state-defining coordinate.

### Lecture 5: Energy

A fundamental principal asserts that all fundamental forces derive from a scalar function called _potential energy_: $F(x) = -\nabla V(x)$, and that the sum of potential and kinetic energy $T = mv^2/2$ are conserved. Note that in general $F$ is a vector field and so is $x$, but I'm going to leave them unbolded for now. 

To verify that energy is conserved, compute $\dot{E}$:
$$
\begin{align}
\dot{E} &= \dot{T} + \dot{V} \\
&= m\dot{x}\ddot{x} + \frac{\partial V}{\partial x}\dot{x} \\
&= m\dot{x}\ddot{x} - F\dot{x} \\
&= m\dot{x}\ddot{x} - m\ddot{x}\dot{x} \\
&= 0
\end{align}
$$

Note that there exist so-called _non-conservative_ forces for which this is not true. For example, friction and air resistance are non-conservative forces. These forces however are not fundamental forces like gravity or electromagnetism and therefore fall outside the domain of application of this rule. Furthermore, when analyzing friction and drag we usually only model the object which is being slowed down and not the individual air molecules which produce the drag, so the system isn't closed. I like to think of non-conservative forces as "convenience" or "phenomenological" forces because they allow us to ignore the complex dynamics of unimportant objects (e.g. the air or ground) while still capturing the dynamics of the things we care about (e.g., a ball moving through the air or rolling across the ground).

### Lecture 6: The Principle of Least Action

The principle of least action states that of all the trajectories a particle can conceivably take, the one it _does_ take is the one that minimizes the integral
$$
A = \int_{t_0}^{t_1} L(x,\dot{x}) \, dt
$$
where $L = T - V$  is the _Lagrangian_, and $A$ is the _action_. Although this is usually called the principal of _least_ action, technically we are solving for the action extrema, which may be a maximum. The extrema trajectory satisfies the Euler-Lagrange equation:
$$
\frac{d}{dt}\frac{\partial L}{\partial \dot{x}} = \frac{\partial L}{\partial x}
$$
Plugging in $L = m\dot{x}^2/2 - V(x)$ results in Newton's equation $m\ddot{x} = -\partial V/\partial x$. For systems with more than one degree of freedom there is a separate Euler-Lagrange equation for each degree of freedom.

If the least-action formulation is equivalent to Newton's equation, then why should we care about it? Leonard lists a few reasons:

- Entire theories, such as electrodynamics, Einstein's gravity, and the standard model of elementary particles are described by a Lagrangian.
- It makes coordinate transformations more convenient, such as if we wanted to move between a stationary and rotating coordinate system.
- It conveniently allows us to incorporate constraints on trajectories by using _generalized coordinates_.

Generalized coordinates are what I'm going to use going forward. They allow us to go beyond cartesian coordinates and define coordinates however we want as long as they uniquely specify a system's state. For example, if we were modeling a double pendulum we could use the first pendulum's angle relative to the vertical and the second pendulum's angle relative to the first pendulum's, instead of the x-y positions of each. 

The convenience of generalized coordinates is furthered by the fact that they seamlessly integrate constraints into motion. For example, if a particle is constrained to move on a manifold, then by choosing generalized coordinates on the manifold we automatically get a dynamics equation written in terms of those coordinates.

In terms of notation, we use $q$ and $\dot{q}$ for generalized position and velocity. The Euler-Lagrange equation becomes
$$
\frac{d}{dt}\frac{\partial L}{\partial \dot{q}} = \frac{\partial L}{\partial q}
$$
Each generalized coordinate has an associated generalized momentum called its _conjugate momentum_. To figure out what it is, note that 
$$
\frac{\partial L}{\partial \dot{q}} = m\dot{q} = p
$$
And so we define $\partial L/\partial \dot{q}$ as the generalized momentum conjugate. 

Why did we go through this trouble to compute the momentumm which we already knew? Well because sometimes momentum isn't this obvious, and in those cases this formula is practical. For example, consider motion in polar coordinates where
$$
L = m(\dot{r}^2 + r^2\dot{\theta}^2) \,/\, 2
$$
The radial and angular momenta are straightforward to calculate:
$$
p_r = \frac{\partial L}{\partial \dot{r}} = m\dot{r} \\
p_\theta = \frac{\partial L}{\partial \dot{\theta}} = mr^2\dot{\theta}
$$
Note that the right-hand side $\partial L/\partial \dot{\theta} = 0$ and therefore $\dot{p}_\theta=0$, angular momentum is conserved. 

### Lecture 7: Symmetries and Conservation Laws

lkj

### Lecture 8: Hamiltonian Mechanics

lkj

### Lecture 9: The Phase Space Fluid

lk

### Lecture 10: Poisson Brackets

lk





{% include disqus.html %}

