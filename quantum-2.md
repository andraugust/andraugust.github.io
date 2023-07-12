---
layout: default
---

# Quantum Mechanics Part 2: Particles and Dynamics

<center><img src="" style="zoom:80%;"></center>

$$\newcommand{\bra}[1]{\left<#1\right|}\newcommand{\ket}[1]{\left|#1\right>}\newcommand{\bk}[2]{\left<#1\middle|#2\right>}\newcommand{\bke}[3]{\left<#1\middle|#2\middle|#3\right>}$$

## 1. Time and Change

In CM states are real numbers that change under the influence of forces. In QM states are vectors in  Hilbert space—how do they change?

__Time Evolution Operator.__ To answer this, start by modeling state dynamics generically as
$$
\ket{\psi(t)}=\mathbf{U}(t) \ket{\psi(0)}
$$
where $$\mathbf{U}$$ is called the time evolution operator—it maps states across time. One thing we want $$\mathbf{U}$$ to do is conserve the relationship between states over time. In other words, $$\braket{\psi(t)}{\phi(t)} = \braket{\psi(0)}{\phi(0)}$$, which is the same as saying
$$
\bra{\psi(0)}\mathbf{U}(t)^{\dagger}\mathbf{U}(t)\ket{\phi(0)} = \braket{\psi(0)}{\phi(0)}
$$
Implying that $$\mathbf{U}^{\dagger}\mathbf{U} = I$$. This property is called unitarity.

Next, lets see what infinitesimal change looks like for $$\mathbf{U}$$. To first order,
$$
\mathbf{U}(\epsilon) = I - \epsilon i \mathbf{H}
$$
Where $$\epsilon$$ is an infinitesimal time interval, $$\mathbf{H}$$ is a constant operator, and $$-i$$ is added with hindsight for how the results turn out and correspond to experiments. What does this operator do to $$\ket{\psi}$$?
$$
\begin{align*}
\ket{\psi(\epsilon)} &= \mathbf{U}(\epsilon) \ket{\psi(0)} \\
\ket{\psi(\epsilon)} &= (I - \epsilon i \mathbf{H}) \ket{\psi(0)} \\
\frac{\ket{\psi(\epsilon)} - \ket{\psi(0)}}{\epsilon} &= -i\mathbf{H} \ket{\psi(0)} \\
\end{align*}
$$
As $$\epsilon \rightarrow 0$$,
$$
\frac{\partial \ket{\psi}}{\partial t} = -\frac{i}{\hbar}\mathbf{H}\ket{\psi}
$$
where $$\hbar$$ is added so the units are correct. It's value is about $$10^{-34} kg \space m^2/s$$. This PDE is called the generalized Schrodinger equation.

Before moving on, we can learn about $$\mathbf{H}$$ by asking what, if anything, the unitary constraint on $$\mathbf{U}$$ implies about it:
$$
\begin{align*}
\mathbf{U}(\epsilon)^\dagger \mathbf{U}(\epsilon) &= (I - \epsilon i \mathbf{H})^\dagger (I - \epsilon i \mathbf{H}) \\
&= (I + \epsilon i \mathbf{H}^\dagger) (I - \epsilon i \mathbf{H}) \\
&= I - \epsilon i \mathbf{H} + \epsilon i \mathbf{H}^\dagger = I \\
\end{align*}
$$
So $$\mathbf{U}$$ being unitary implies $$\mathbf{H}$$ is Hermitian and therefore can represent an observable, which, as we'll see is the Hamiltonian in QM.

In CM the Hamiltonian represents the total energy of a system and relates to its dynamics through Poisson brackets:
$$
\dot{L}=\{L,H\}
$$
Where $$L$$ is any quantity defined over phase space $$L(q,p)$$. A similar relation exists in QM for expected values:
$$
\frac{d}{dt}\left<\mathbf{L}\right> = -\frac{i}{\hbar}\left<\left[\mathbf{L},\mathbf{H}\right]\right>
$$
Where $$\left[\mathbf{L},\mathbf{H}\right] = \mathbf{L}\mathbf{H} - \mathbf{H}\mathbf{L}$$ is called the commutator. From it we see that if a quantity commutes with $$\mathbf{H}$$ then it is conserved (in expectation), and more generally any function of a quantity that commutes with $$\mathbf{H}$$ is conserved (in expectation).

Note that in QM expected values don't change due to measurement outcomes changing, those are fixed for a given operator (for example $$\pm 1$$ for spin), instead, they change because the associated measurement _probabilities_ change, and to calculate how those change we have to solve the generalized Schrodinger equation.

__Solving the GSE.__ Solving the generalized Schrodinger equation is easiest in the energy basis where $$\mathbf{H}$$ is diagonal and a general state vector can be written as
$$
\ket{\psi(t)} = \sum_i a_i(t) \ket{E_i}
$$
where $$\ket{E_i}$$ is an energy eigenvector satisfying $$\mathbf{H}\ket{E_i} = E_i\ket{E_i}$$. Inserting into the GSE gives
$$
\begin{align*}
\sum_i \dot{a}_i(t) \ket{E_i} &= -\frac{i}{\hbar} \mathbf{H} \sum_i a_i(t) \ket{E_i} \\
&= -\frac{i}{\hbar} \sum_i E_i a_i(t) \ket{E_i}\\
\end{align*}
$$
Which is a simple first-order ODE for each component. The solution is
$$
a_i(t) = a_i(0) e^{-iE_it/\hbar}
$$
Compared to the general form of an oscillator $$\exp(-i \omega t)$$ we see that $$E/\hbar$$ plays the role of frequency in QM.

This solution assumes we're working in the energy basis. What if we're given a state vector in a different basis and want to compute dynamics? The solution is to do a change of basis. Given a general state vector $$\ket{\Psi}$$ in a non-energy basis (such as the $$\ket{u}$$ and $$\ket{d}$$ basis), factor the Hamiltonian according to $$\mathbf{H} = \mathbf{P}\mathbf{\Lambda}\mathbf{P}^{\dagger}$$, then the state in the energy basis is $$\mathbf{P}^{\dagger}\ket{\Psi}$$.  In terms of components $$a_i = \braket{E_i}{\Psi}$$, where $$a_i$$ is the $$i$$th component of $$\ket{\Psi}$$ in the energy basis. This is all summarized by the formula
$$
\ket{\Psi(t)} = \sum_i \braket{E_i}{\Psi(0)} e^{-iE_it/\hbar} \ket{E_i}
$$


## 2. Particle States

So far the states we've looked at have all been discrete—they're represented by a finite sum over basis vectors. In this section we're going to model particles, which have continuous states for position and momentum. How are continuous states modeled? The answer is in the same way that discrete states are modeled: by the principles of QM. The trick is to observe that nothing in the principles requires states to be discrete, the principles only define conditions and physical interpretations about _vectors_, which can be anything, continuous or discrete, as long as they satisfy the mathematical axioms of vectors (they commute, have an inverse, etc). Complex functions, as it turns out, are vectors, and they are what we'll use to model particles.

In terms of notation, a continuous vector is associated with a _wave function_ $$\psi(x)$$ which takes a complex input and returns a complex output. Wave functions are defined with respect to a particular basis just as discrete vectors are, and their form can change from one basis to the next, just as discrete vectors can. The bra-ket notation is as useful for wave-functions as it is for discrete vectors. The discrete representation
$$
\ket{A} = \sum_i a_i \ket{i}
$$
becomes
$$
\ket{\psi} = \int \psi(x) \ket{x} \,dx
$$
for continuous vectors, where $$x$$ labels eigenvalues and $$\ket{x}$$ is the basis associated with the eigenvalue $$x$$. In this analogy, $$\psi(x)$$ is like a continuous set of coefficients.

__Operators on Functions.__ Operators on functions are similar to operators on discrete vectors: they need to be linear and Hermitian. They're linear when they distribute over the sum of functions and when constants factor out of the operator. In other words
$$
\mathbf{L}(a\psi(x)+b\phi(x)) = a\mathbf{L}\psi(x) + b\mathbf{L}\phi(x)
$$
Examples of linear operators include multiplication by $$x$$ and differentiation by $$d/dx$$.

Hermiticity is a bit more involved. It occurs when
$$
\bke{\psi}{\mathbf{L}}{\phi} = \bke{\phi}{\mathbf{L}}{\psi}^{*}
$$
Where
$$
\bke{\psi}{\mathbf{L}}{\phi} = \int \psi^*(x)\mathbf{L} \phi(x) \,dx
$$
For $$\mathbf{L}=x$$ this is
$$
\bke{\psi}{x}{\phi} = \int \psi^*(x) x \phi(x) \,dx = \left( \int \psi(x) x \phi^*(x) \,dx \right)^* = \bke{\phi}{x}{\psi}^*
$$
Therefore the operator $$x$$ is Hermitian. Note that $$\dagger$$ from discrete operators gets replaced by $$*$$ for functions because there are no transposes for functions. Applying the same test to $$d/dx$$ we find that it's not Hermitian, but if we multiply by $$i$$ it is.

__Eigenfunctions of Position.__ How are eigenvalues and eigenfunctions computed for continuous operators? For position the operator is $$x$$ and its eigenvalues are denoted by $$x_0$$. The eigenequation is
$$
x\psi(x) = x_0 \psi(x)
$$
or
$$
(x-x_0)\psi(x) = 0
$$
If $$x \ne x_0$$ then this requires $$\psi(x) = 0$$, and when $$x = x_0$$ then $$\psi(x)$$ can be anything, but because $$\psi$$ is a probability amplitude, it must integrate to $$1$$, so the eigenfunction is
$$
\psi(x) = \delta(x-x_0)
$$
This states the obvious fact that if a particle is measured at $$x_0$$ then it's only at $$x_0$$. It's important to note that $$\delta$$ is not a function, it's a distribution, and as such belongs inside an integral as
$$
\begin{align*}
\ket{\psi} &= \int \psi(x) \ket{x} \,dx \\
&= \int \delta(x-x_0) \ket{x} dx \\
&= \ket{x_0}
\end{align*}
$$
__Eigenfunctions of Momentum.__ What are the eigenfunctions of momentum? For momentum the set-up and solution are the same, but now $$\bar\psi$$ is used to denote the wave function in momentum space:
$$
p\bar\psi(p) = p_0\bar\psi(p) \\
\rarr\bar\psi(p) = \delta(p-p_0)
$$
The $$\delta$$ function solution here and for position are not especially insightful, but when we look at momentum in the $$x$$ basis things are more interesting. In the $$x$$ basis the momentum operator changes from $$p$$ to $$-i\hbar d/dx$$, so the eigenequation is
$$
-i\hbar \frac{d}{dx}\psi(x) = p \psi(x)
$$
The solution is
$$
\psi(x) = Ae^{ipx/\hbar}
$$
Note that because this is a wavefunction in the $$x$$-basis it's considered a function of $$x$$ and not $$p$$. The $$p$$ appears because each value of momentum has a different wavefunction, so $$p$$ acts more like a parameter or index.

The constant $$A$$ is determined by normalization:
$$
\bk{\psi}{\psi} = \int_{-\infty}^{\infty} \psi(x)^*\psi(x) \,dx = 1
$$
But this gives
$$
|A|^2\int_{-\infty}^{\infty} \,dx = 1
$$
Which is undefined. This reflects the fact that when particles are unconstrained in space the planewave solution $$\exp(ipx/\hbar)$$ is physically unrealistic. In practice, particles are either constrained in space such that the integration limits are finite, or, if they are un-constrained in space, they're acted on by a potential such that they form a localized wave-packet and the integral converges.

__Changing Basis.__ Generally speaking, an abstract state vector $$\ket{\Psi}$$ can be represented in any basis. For example, in the $$x$$ basis $$\psi(x) = \bk{x}{\Psi}$$, in the momentum basis $$\bar\psi(p) = \bk{p}{\Psi}$$, etc. Because these different representations ultimately correspond to the same thing, namely $$\ket{\Psi}$$, there must be a way to transform between them. How do we transform between the $$x$$ and $$p$$ basis? The trick is to use the identity operator:
$$
I = \int \ket{x}\bra{x} \cdot \,dx
$$
Where "$$\cdot$$" is a placeholder for the vector which the operator acts on. Inserting this into the momentum-space representation gives
$$
\begin{align*}
\bar\psi(p) &= \bk{p}{\Psi} \\
&= \bke{p}{I}{\Psi} \\
&= \int \bk{p}{x}\bk{x}{\Psi}\,dx \\
\end{align*}
$$
But
$$
\begin{align*}
\braket{p}{x} &= \int A e^{-ipx'/\hbar} \delta(x'-x) \,dx' \\
&= Ae^{-ipx/\hbar}
\end{align*}
$$
And $$\braket{x}{\Psi} = \psi(x)$$, so
$$
\bar\psi(p) = A\int e^{-ipx/\hbar} \psi(x) \, dx
$$
Which is the formula for computing a momentum-space wave function given its position-space complement. The derivation of the inverse operation is similar. The result is
$$
\psi(x) = A \int e^{ipx/\hbar} \bar\psi(p) \,dp
$$
So position and momentum wave-functions are Fourier transforms of each other.

__Position-Momentum Uncertainty.__ Going back to the discussion of commutators, we found that two observables are simultaneously knowable iff their operators commute. Do the operators for $$x$$ and $$p$$ commute? The answer is no. Given $$\mathbf{X}=x$$ and $$\mathbf{P}=-i\hbar d/dx $$ the commutator is
$$
[\mathbf{X}, \mathbf{P}] = i\hbar
$$
Which means that position and momentum aren't simultaneously knowable—measuring one destroys information about the other, and vice versa. How unknowable are they together? Defining unknowability in terms of the standard deviation $$\Delta$$ of an operator we find from the general uncertainty principle that
$$
\Delta \mathbf{X} \Delta \mathbf{P} \ge \frac{\hbar}{2}
$$
The lower limit on simultaneous uncertainty is reached when either $$\psi$$ or $$\bar \psi$$ are Gaussian function.

## 3. Particle Dynamics

The previous section looked at 





{% include disqus.html %}
