---
layout: default
---

# Quantum Mechanics Part 2: Particles and Dynamics

<center><img src="quantum/banner-2.png" style="object-fit:contain;"></center>

$$\newcommand{\bra}[1]{\left<#1\right|}\newcommand{\ket}[1]{\left|#1\right>}\newcommand{\bk}[2]{\left<#1\middle|#2\right>}\newcommand{\bke}[3]{\left<#1\middle|#2\middle|#3\right>}$$

## 1. Time and Change

In classical mechanics states are represented by points in phase space and they change under the influence of forces. In quantum mechanics states are complex vectors in Hilbert space. How and what causes them to change?

__Time Evolution Operator.__ Dynamics for vectors can generically be modeled as


$$
\ket{\Psi(t_2)}=\mathbf{U}(t_2,t_1) \ket{\Psi(t_1)}
$$

where $$\mathbf{U}$$ is the "time evolution operator", it maps states from one point in time to another. Usually we'll set $$t_1=0$$ and $$t_2=t$$ and simply write $$\mathbf{U}(t,0) \rightarrow \mathbf{U}(t)$$. 

One thing we want $$\mathbf{U}$$ to do is conserve inner products. In otherwords for arbitrary $$t$$ we want $$\bk{\Psi(t)}{\Phi(t)} = \bk{\Psi(0)}{\Phi(0)}$$ or

$$
\bra{\Psi(0)}\mathbf{U}(t)^{\dagger}\mathbf{U}(t)\ket{\Phi(0)} = \bk{\Psi(0)}{\Phi(0)}
$$


Which implies $$\mathbf{U}^{\dagger}\mathbf{U} = I$$, so $$\mathbf{U}$$ is unitary .

Any finite evolution can be buit up by composing several intermediate evolutions. For example


$$
\mathbf{U}(t_3,t_0) = \mathbf{U}(t_3,t_2)\mathbf{U}(t_2,t_1)\mathbf{U}(t_1,t_0)
$$


In general we'll assume $$\mathbf{U}$$ doesn't explicitly depend on time, so $$\mathbf{U}(t_2,t_1)=\mathbf{U}(t_2-t_1)$$. Thus, if we have an infinitesimal operator we can create whatever dynamics we like by applying it repeatedly. In the limit, the infinitesimal operator is

$$
\mathbf{U}(\epsilon) = I - \epsilon i \mathbf{H}
$$


Where $$\epsilon$$ is an infinitesimal time interval, $$\mathbf{H}$$ is a constant operator, and $$-i$$ is added so that results fit experiment. What does this operator do to $$\ket{\Psi}$$?


$$
\begin{align*}
\ket{\Psi(\epsilon)} &= \mathbf{U}(\epsilon) \ket{\Psi(0)} \\
\ket{\Psi(\epsilon)} &= (I - \epsilon i \mathbf{H}) \ket{\Psi(0)} \\
\frac{\ket{\Psi(\epsilon)} - \ket{\Psi(0)}}{\epsilon} &= -i\mathbf{H} \ket{\Psi(0)} \\
\end{align*}
$$


As $$\epsilon \rightarrow 0$$,


$$
\frac{\partial \ket{\Psi}}{\partial t} = -\frac{i}{\hbar}\mathbf{H}\ket{\Psi}
$$


where $$\hbar$$ is added so units are correct, it's value is about $$10^{-34} kg \space m^2/s$$. This PDE is called the generalized Schrodinger equation.

Before moving on, we can learn a bit about $$\mathbf{H}$$ by asking what, if anything, the unitary constraint on $$\mathbf{U}$$ implies about it:


$$
\begin{align*}
\mathbf{U}(\epsilon)^\dagger \mathbf{U}(\epsilon) &= (I - \epsilon i \mathbf{H})^\dagger (I - \epsilon i \mathbf{H}) \\
&= (I + \epsilon i \mathbf{H}^\dagger) (I - \epsilon i \mathbf{H}) \\
&= I - \epsilon i \mathbf{H} + \epsilon i \mathbf{H}^\dagger = I \\
\end{align*}
$$


So $$\mathbf{U}$$ being unitary implies $$\mathbf{H}$$ is Hermitian and therefore represents an observable, which, as we'll show, is the QM Hamiltonian.

In CM, Hamiltonians represent the total energy of a system and relate to its dynamics through the Poisson bracket:


$$
\dot{L}=\{L,H\}
$$


Where $$L$$ is any quantity defined on phase space $$L(q,p)$$. A similar relation exists in QM, but for expected values:


$$
\frac{d}{dt}\left<\mathbf{L}\right> = -\frac{i}{\hbar}\left<\left[\mathbf{L},\mathbf{H}\right]\right>
$$


$$\left[\mathbf{L},\mathbf{H}\right] = \mathbf{L}\mathbf{H} - \mathbf{H}\mathbf{L}$$ is called the commutator. From it we see that if a quantity commutes with $$\mathbf{H}$$ then it is conserved (in expectation), and more generally any function of a quantity that commutes with $$\mathbf{H}$$ is conserved (in expectation). This is like in CM where if the PB is $$0$$ then $$L$$ is conserved.

Note that in QM expected values don't change due to measurement outcomes changing, those are fixed for a given operator (for example $$\pm 1$$ for spin), instead, expected values change because measurement _probabilities_ change, and to calculate how measurement probabilities change we have to solve the generalized Schrodinger equation.

__Solving the SE.__ Solving the SE is easiest in the energy basis where $$\mathbf{H}$$ is diagonal and a state vector is


$$
\ket{\Psi(t)} = \sum_i a_i(t) \ket{E_i}
$$


$$\ket{E_i}$$ is an energy eigenvector satisfying $$\mathbf{H}\ket{E_i} = E_i\ket{E_i}$$. Inserting this into the SE gives


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

This solution assumes we're working in the energy basis. What if we're given a state vector in a different basis and want to compute dynamics? The solution is to do a change of basis. Given a general state vector $$\ket{\Psi}$$ in a non-energy basis (such as the spin basis $$\ket{+z}$$, $$\ket{-z}$$), factor the Hamiltonian according to $$\mathbf{H} = \mathbf{P}\mathbf{\Lambda}\mathbf{P}^{\dagger}$$, then the state in the energy basis is $$\mathbf{P}^{\dagger}\ket{\Psi}$$.  In terms of components $$a_i = \bk{E_i}{\Psi}$$, where $$a_i$$ is the $$i$$th component of $$\ket{\Psi}$$ in the energy basis. This is all summarized by the general solution to the SE:


$$
\ket{\Psi(t)} = \sum_i \bk{E_i}{\Psi(0)} e^{-iE_it/\hbar} \ket{E_i}
$$

## 2. Particle States

So far the states we've looked at have all been discrete—they're represented by a finite sum over basis vectors. In this section we're going to model particles, which have continuous states for position and momentum. How are continuous states modeled? The answer is in the same way that discrete states are modeled: by using the principles of QM. The trick is to see that nothing in the principles requires states to be discrete—the principles only define conditions and physical interpretations related to _vectors_, and vectors can be anything, continuous or discrete, as long as they satisfy the mathematical axioms of vectors (they commute, have an inverse, etc). Complex functions, as it turns out, are vectors, and they're what we'll use to model particles.

__Continuous States.__ In terms of notation, a continuous state vector is associated with a _wave function_ $$\psi(x)$$ which takes a complex input and returns a complex output. Wave functions are defined with respect to a particular basis just as discrete vectors are, and their form can change from one basis to the next, just as discrete vectors can. The bra-ket notation is useful for wave-functions like it is for discrete vectors. The discrete representation


$$
\ket{A} = \sum_i a_i \ket{i}
$$


becomes


$$
\ket{\Psi} = \int \psi(x) \ket{x} \,dx
$$


where $$x$$ labels eigenvalues and $$\ket{x}$$ is the associated eigenvector. In this analogy, $$\psi(x)$$ is like a continuous set of coefficients. Another way to think of wave functions is in terms of them being a state vector's projection onto a basis. For example, in the $$x$$ basis the wave function is


$$
\psi(x) = \bk{x}{\Psi}
$$


__Continuous Operators.__ Operators on continuous vectors are similar to operators on discrete vectors: they need to be linear and Hermitian. They're linear when they distribute over the sum of functions with constants factoring out. In other words,


$$
\mathbf{L}(a\psi(x)+b\phi(x)) = a\mathbf{L}\psi(x) + b\mathbf{L}\phi(x)
$$


Examples of linear operators include multiplication by $$x$$ and differentiation by $$d/dx$$.

Hermiticity is a bit trickier. It occurs when


$$
\bke{\psi}{\mathbf{L}}{\phi} = \bke{\phi}{\mathbf{L}}{\psi}^{*}
$$


Where


$$
\bke{\psi}{\mathbf{L}}{\phi} = \int \psi^*(x)\mathbf{L} \phi(x) \,dx
$$


For example, if $$\mathbf{L}=x$$ this is


$$
\begin{align*}
\bke{\psi}{x}{\phi} &= \int \psi^*(x) x \phi(x) \,dx \\
&= \left( \int \psi(x) x \phi^*(x) \,dx \right)^* \\
&= \bke{\phi}{x}{\psi}^*
\end{align*}
$$


Therefore the operator $$x$$ is Hermitian. Note that $$\dagger$$ from discrete operators gets replaced by $$*$$ for functions because there are no transposes for functions. Applying the same test to $$d/dx$$ we find that it's not Hermitian, but if we multiply by $$i$$ it is.

__Eigenfunctions of Position.__ How are eigenvalues and eigenvectors computed for continuous operators? For position the operator is $$x$$ and its eigenvalues are denoted by $$x_0$$. The eigenequation is


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
\ket{\Psi} &= \int \psi(x) \ket{x} \,dx \\
&= \int \delta(x-x_0) \ket{x} dx \\
&= \ket{x_0}
\end{align*}
$$


__Eigenfunctions of Momentum.__ What are the eigenfunctions of momentum? For momentum the set-up and solution are the same, but now $$\bar\psi$$ is used to denote a wave function in momentum space:


$$
p\bar\psi(p) = p_0\bar\psi(p) \\
\rightarrow \bar\psi(p) = \delta(p-p_0)
$$


The $$\delta$$ function solution here and for position are not especially insightful, but when we look at momentum in the $$x$$ basis things are more interesting. In the $$x$$ basis, from experimental insight, the momentum operator changes from $$p$$ to $$-i\hbar \, d/dx$$. The eigenequation is


$$
-i\hbar \frac{d}{dx}\psi(x) = p \psi(x)
$$


The solution is


$$
\psi(x) = Ae^{ipx/\hbar}
$$


Note that because this is a wavefunction in the $$x$$-basis it's considered a function of $$x$$ and not $$p$$. The $$p$$ appears because each value of momentum has a different wavefunction associated with it, so $$p$$ acts more like a parameter or index.

The constant $$A$$ is determined by normalization:


$$
\bk{\psi}{\psi} = \int_{-\infty}^{\infty} \psi(x)^*\psi(x) \,dx = 1
$$


But this gives


$$
|A|^2\int_{-\infty}^{\infty} \,dx = 1
$$


Which is undefined. This reflects the fact that when particles are unconstrained in space the planewave solution $$\exp(ipx/\hbar)$$ is physically unrealistic. In practice, particles are either constrained in space such that the integration limits are finite, or, if they are un-constrained in space, they're acted on by a potential such that they're localized and the integral converges.

__Changing Basis.__ Generally speaking, a state vector $$\ket{\Psi}$$ can be represented in any basis. For example, in the $$x$$ basis $$\psi(x) = \bk{x}{\Psi}$$, in the momentum basis $$\bar\psi(p) = \bk{p}{\Psi}$$, etc. Because these representations ultimately correspond to the same thing, namely $$\ket{\Psi}$$, there must be a way to transform between them. How do we transform between the $$x$$ and $$p$$ basis? The trick is to use the identity operator:


$$
I = \int \ket{x}\bra{x} \cdot \,dx
$$


Where "$$\cdot$$" is a placeholder for the vector which the operator acts on. Inserting this into the momentum-representation gives


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
\bk{p}{x} &= \int A e^{-ipx'/\hbar} \delta(x'-x) \,dx' \\
&= Ae^{-ipx/\hbar}
\end{align*}
$$


And $$\bk{x}{\Psi} = \psi(x)$$, so


$$
\bar\psi(p) = A\int e^{-ipx/\hbar} \psi(x) \, dx
$$


Which is the formula for converting a momentum-space wave function into its position-space complement. The derivation of the inverse operation is similar. The result is


$$
\psi(x) = A \int e^{ipx/\hbar} \bar\psi(p) \,dp
$$


So position and momentum space are related by the Fourier. This leads to the interpretation that momentum space is the spatial frequency domain of position space, where spatial frequency is given by $$k=p/\hbar$$.

__Changing Basis: Operators.__ How do operators change basis? In the same way as when they're matrices—using $$\mathbf{L' = \mathbf{U} \mathbf{L} \mathbf{U}^{-1}}$$, where $$\mathbf{L}$$ is the operator of interest, $$\mathbf{L}'$$ is the transformed operator, and $$\mathbf{U}$$ is a unitary change-of-basis operator. Because $$\mathbf{U}$$ is unitary and we're working with continuous operators we can set $$\mathbf{U}^{-1} = \mathbf{U}^*$$.

How does this work for position and momentum? The relevant change-of-basis transformation is the Fourier transform $$\mathbf{F}$$. Is it unitary? Yes because $$\mathbf{F}^*\mathbf{F}\psi(x) = \psi(x)$$. Let's use it to derive the position operator in momentum space, call it $$\mathbf{\bar X}$$.


$$
\begin{align*}
\mathbf{\bar X} \bar\psi(p) &= \mathbf{F}\mathbf{X}\mathbf{F}^* \bar \psi(p) \\
&= \mathbf{F} \mathbf{X} \psi(x) \\
&= \mathbf{F} x \psi(x) \\
&= i\hbar \frac{d}{dp} \bar \psi(p)
\end{align*}
$$


Where the last step comes from a Fourier transform identity. So the position operator in momentum-space has the same form as the momentum operator in position space, namely $$i\hbar d/dp$$.

Another way to determine or verify an operator in a new basis is through the use of commutators. The reason is that commutators are _basis independent_. For example, $$[\mathbf{X}, \mathbf{P}] = [\mathbf{\bar X}, \mathbf{\bar P}] = i\hbar$$. This method may require some guessing and checking, whereas the unitary method is an explicit calculation.

As a practical note, when working with operators it's helpful to supply them with a test function to act on, otherwise it isn't necessarily clear how they behave or simplify.

__Position-Momentum Uncertainty.__ Going back to the discussion of commutators, we found that two observables are simultaneously knowable iff their operators commute. Do the operators for $$x$$ and $$p$$ commute? The answer is no. Given $$\mathbf{X}=x$$ and $$\mathbf{P}=-i\hbar d/dx $$ the commutator is


$$
[\mathbf{X}, \mathbf{P}] = i\hbar
$$


Which means position and momentum aren't simultaneously knowable—measuring one destroys information about the other, and vice versa. How unknowable are they together? Defining unknowability in terms of the standard deviation $$\sigma$$ of an operator we find (from the general uncertainty principle) that


$$
\sigma_x \sigma_p \ge \frac{\hbar}{2}
$$


The lower limit on simultaneous uncertainty is reached when either $$\psi$$ or $$\bar \psi$$ are Gaussian function, as is shown later in the section on wavepackets.

## 3. Particle Dynamics

In the first section we derived the general Schrodinger equation and solved it for the dynamics of discrete-state systems. In the second section we defined wavefunctions and showed how to represent particles in terms of them. The rest of this post combines those two sections to model the dynamics of particles, starting with the free particle and then moving on to potentials and oscillators.

__Free Particle.__ A particle is said to be "free" when no forces act on it. In the absence of forces there are no potentials, so the Hamiltonian is
$$
\mathbf{H} = \frac{\mathbf{P}^2}{2m} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}
$$


Plugging this into the GSE gives the PDE governing free particle dynamics:


$$
\frac{\partial \psi(x,t)}{\partial t} = \frac{i\hbar}{2m} \frac{\partial^2 \psi(x,t)}{\partial x^2}
$$


This PDE has the form of a diffusion equation but with complex diffusion coefficient. To solve it we use the solution derived earlier for discrete vectors:


$$
\ket{\Psi(t)} = \sum_i \bk{E_i}{\Psi(0)} e^{-iE_it/\hbar} \ket{E_i}
$$


Converting to continuous space gives


$$
\psi(x,t) = \int \left( \int \psi_E^*(x) \psi(x,0) \,dx \right) e^{-iEt/\hbar} \psi_E(x) \, dE
$$


Where $$\psi_E(x)$$ is an energy eigenfunction in the $$x$$-basis. To find $$\psi_E$$ we solve the eigenvalue equation


$$
\begin{align*}
\mathbf{H}\psi_E(x) &= E\psi_E(x) \\
\rightarrow -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} \psi_E(x) &= E \psi_E(x)
\end{align*}
$$


The general solution is


$$
\psi_E(x) = Ae^{ix\sqrt{2mE}/\hbar}
$$


Or, in terms of momentum,


$$
\psi_p(x) = Ae^{ipx/\hbar}
$$


Plugging this into the general solution and writing everything in terms of $$p$$ instead of $$E$$ gives


$$
\begin{align*}
\psi(x,t) &= \int \left( \mathbf{F}\psi(x,0) \right) \, e^{-iEt/\hbar} \, e^{ipx/\hbar} \, dp \\
&= \int \bar\psi(p,0) \exp(i \left( \frac{p}{\hbar}x-\frac{p^2}{2m\hbar}t \right)) dp
\end{align*}
$$


This is the general solution to the SE for a free particle. 

At this point it's reasonable to ask why there are any dynamics at all given there are no forces. The reason is that the wavefunction is a sum of plane waves $$\exp i(kx-\omega t)$$ weighted by the amount of each wave in the initial state $$\bar \psi(p,0)$$. Each wave moves at a different speed, called its phase velocity, and this causes the shape of the wavefunction to change over time. If instead the phase waves all moved at the same speed then the initial wavefunction shape would be preserved.

The speed of each phase wave is given by


$$
v(k) = \omega/k = E/p = p/2m =\hbar k/2m
$$


Where $$k=p/\hbar$$ and $$\omega=p^2/2m\hbar = \hbar k^2/2m =E/\hbar$$. So waves with smaller wavelength move faster—they have more energy.

Note that $$k$$ and $$\omega$$ are not independent quantities, but instead have a dispersion relation


$$
\omega (k) = \frac{\hbar k^2}{2m}
$$


__The Gaussian Wavepacket.__ A Gaussian wavepacket is a wave function having Gaussian, or Normal, density $$\psi^*\psi \sim N$$. Such distributions are interesting because unlike planewaves they're localized in space. Consider the following wavepacket in momentum-space:


$$
\bar\psi(p,0) = \frac{1}{(2\pi \sigma_p^2)^{1/4}} \exp (-\frac{(p-p_0)^2}{4\sigma_p^2})
$$

This wavepacket, when squared, is a Gaussian centered around $$p_0$$ with spread $$\sigma_p$$. In position-space it's wavefunction is


$$
\psi(x,0) = \left( \frac{4 \sigma_p^2 \hbar^2}{2\pi} \right)^{1/4} \exp(-\sigma_p^2 x^2 /\hbar^2) \exp(ip_0x/\hbar)
$$


Which is also Gaussian, but multiplied by a wave factor. By inspection, the position-space uncertainty is related to the momentum-space uncertainty by $$\sigma_x \sigma_p = \hbar/2$$, which is exactly the lower limit from the Heisenberg uncertainty relation.

Plugging $$\psi(x,0)$$ into the SE we find that it's _not_ a solution. This shouldn't come as a surprise—we already showed that solutions are planewaves of the form $$A \exp i(kx-\omega t)$$. So technically wave-packets don't describe single particles, _but_ we can add several planewaves together such that their superposition _approximates_ a wavepacket, and the sum of planewaves _is_ a solution to the SE, so in this sense wavepackets are physically realistic.

Plugging $$\bar \psi(p,0)$$ into the general SE solution and taking the integral gives


$$
\psi(x,t) = \frac{(2\pi\sigma_x^2)^{-1/4}}{\left(1+i\frac{\hbar}{2m\sigma_x^2}\right)^{1/2}}\exp \frac{-x^2+\frac{i}{\hbar}(4\sigma_x p_0 x + 2\sigma_x^2p_0^2t)}{4\sigma_x^2(1+i\frac{\hbar}{2m\sigma_x^2}t)}
$$


This wavefunction is complicated, but its density is a simple Gaussian:


$$
\lvert \psi(x,t) \rvert^2 = \frac{1}{\sqrt{2\pi\sigma_x^2(t)}} \exp -\frac{\left( x-\mu(t) \right)^2}{2\sigma^2_x(t)}
$$


Where


$$
\begin{align*}
\mu(t) &= \frac{p_0}{m}t \\
\sigma_x(t) &= \sigma_x \sqrt{1+\left(\frac{\hbar}{2m\sigma_x^2}t\right)^2}
\end{align*}
$$


So the wavepacket moves to the right with "group velocity" $$p_0/m$$, just like a classical particle. It's interesting to note that group velocity is different from phase velocity. The dispersion of the phase waves causes the wavepacket to spread as it travels. The spread increases like $$\sqrt{1+t^2}$$, so the particle becomes less localized with time.

__The Classical Connection.__ Is the wavepacket result $$v_g = p_0/m$$ true more generally? In QM the classical notion of velocity corresponds to 


$$
v = \frac{d}{dt} \left< \mathbf{X} \right>
$$


Where the time-derivative is determined by


$$
\frac{d}{dt}\left<\mathbf{X}\right> = -\frac{i}{\hbar}\left<\left[\mathbf{X},\mathbf{H}\right]\right>
$$

For a free-particle this simplifies to $$\left< \mathbf{P} \right> = mv$$, so the result does in fact generalize beyond wavepackets.

What about non-free particles? In CM when there's a potential the dynamics are
$$
\frac{dp}{dt} = -\frac{dV}{dx}
$$
In QM the left side becomes
$$
\frac{d}{dt}\left<\mathbf{P}\right> = -\frac{i}{\hbar}\left<[\mathbf{P},\mathbf{H}]\right>
$$
The Hamiltonian is
$$
\mathbf{H} = \frac{1}{2m}\mathbf{P}^2 + \mathbf{V}(x)
$$
Which leads to
$$
\frac{d}{dt}\left<\mathbf{P}\right> = -\left<\frac{d\mathbf{V}}{dx}\right>
$$
So the quantum result is similar to the classical result, but it's important to note that on the right side the expectation is taken over the entire derivative, which in general is different from taking it over $$x$$ first and then differentiating. In otherwords,
$$
\left<\frac{d\mathbf{V}}{dx}\right> \neq \frac{d\mathbf{V}(\left<x\right>)}{d\left<x\right>}
$$












## References

* Gaussian wavepacket integrals: [1](https://ocw.mit.edu/courses/6-974-fundamentals-of-photonics-quantum-electronics-spring-2006/235adf962a3ef4772b2f494261e00d4b_chapter4.pdf), [2](https://here.isnew.info/inverse-fourier-transform-of-the-gaussian-function.html)
* 

{% include disqus.html %}
