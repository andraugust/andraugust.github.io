---
layout: default
---

# Quantum Mechanics Part 3: Examples

<center><img src="" style="zoom:80%;"></center>

$$\newcommand{\bra}[1]{\left<#1\right|}\newcommand{\ket}[1]{\left|#1\right>}\newcommand{\bk}[2]{\left<#1\middle|#2\right>}\newcommand{\bke}[3]{\left<#1\middle|#2\middle|#3\right>}$$

## 1. The Free Particle

Conceivably the simples particle to model is one with no forces acting on it. This is the so-called _free particle_. Without forces there is no potential, so the Hamiltonian is


$$
\mathbf{H} = \frac{\mathbf{P}^2}{2m} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}
$$


Plugging this into the GSE gives


$$
i\hbar\frac{\partial \psi(x,t)}{\partial t} = -\frac{\hbar^2}{2m} \frac{\partial^2 \psi(x,t)}{\partial x^2}
$$


This has the form of a diffusion equation with a complex coefficient, which, as we'll show, gives rise to wave-like solutions that spread out over time. 

To solve the PDE we use separation of variables. The result can be written several ways:


$$
\begin{align*}
\psi(x,t) &= \left(Ae^{ix\sqrt{2mE}/\hbar} + Be^{-ix\sqrt{2mE}/\hbar}\right) e^{-iEt/\hbar} \\
&= Ae^{i\left(k x - \omega t\right)} + Be^{-i\left(k x - \omega t\right)} \\
&= \left(A\cos\left(kx\right) + B\sin\left(kx\right)\right) e^{-i\omega t}
\end{align*}
$$


where $$A$$ and $$B$$ are constants chosen to fit the initial and/or boundary conditions of a specific configuration, and $$k = \sqrt{2mE}/\hbar$$ and $$\omega = E/\hbar$$. 

By inspection, the solution consists of two identical planewaves moving in opposite directions. The waves' phase velocity is


$$
v = \omega/k = E/p = p/2m =\hbar k/2m
$$


And their dispersion relation is


$$
\omega (k) = \frac{\hbar k^2}{2m}
$$


In terms of normalization, the free particle wavefunction only normalizes when a particle is _bounded_. For example if a particle is _un_-bounded such that it can exist freely in $$(-\infty,\infty)$$ or $$(0,\infty)$$ etc, then there's no way to set $$A$$ and $$B$$ such that $$\int\psi^*\psi = 1$$. Thus, physical free particles have to be bounded.

__Particle in a box.__ An example of a bounded free particle is the so-called particle in a box. Consider the potential


$$
V(0\le x \le L) = 0 \\
V(x < 0) = V(x>L) = \infty
$$


This is a "potential well" bounding the particle between $$0$$ and $$L$$. The boundary conditions imply that $$\psi(0)=\psi(L)=0$$, which, together with the normalization constraint yields the solution


$$
\begin{align*}
\psi_n(x,t) &= \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right) e^{-iE_nt/\hbar} \\
E_n &= \frac{\hbar^2 \pi^2}{2mL^2}n^2
\end{align*}


$$
Where $$n\in \{0,1,2,...\}$$. The first few wavefunctions are shown below on the left (at $$t=0$$) with their probability densities on the right. Interestingly, the boundary conditions force solutions to be countable, having a discrete _spectrum_ of energies.

<center><img src="quantum/particle_in_box.png" style="object-fit:contain;"></center>

Because the Schrodinger equation is linear, any linear combination of the $$\psi_n$$ is also a solution, so the general solution to the particle in a box is


$$
\sum_n a_n (0) \psi_n
$$


where $$a_n(0)$$ is the "amount" of $$\psi_n$$ in the initial condition, and is subject to the constraint


$$
\sum_n a_n^*(0)a_n(0) = 1
$$


__Stationary states.__ Eigenfunctions of the Schrodinger equation are sometimes called _stationary states_. "Stationary" because their PDFs are time-independent. For example, if $$\psi(x)$$ is an eigenfunction, then the wavefunction at time $$t$$ is


$$
\psi(x)e^{-iEt/\hbar}
$$


which depends on time, but the PDF $$\psi^*\psi$$ doesn't. Note that the _sum_ of stationary states _isn't_ stationary. For example, if $$\psi_1$$ and $$\psi_2$$ are stationary and normalized individually, then the sum


$$
a\psi_1(x) e^{i\omega_1t} + b\psi_2(x) e^{i\omega_2t}
$$


has PDF


$$
\left| a\psi_1 \right|^2 + \left| b\psi_2 \right|^2 + a^*b\psi_1^*\psi_2\cos((\omega_1-\omega_2)t) + ab^*\psi_1\psi_2^*\sin((\omega_1-\omega_2)t)
$$


which _is_ time-dependent. This time-dependency causes the PDF to oscillate with a beat.

Keep in mind that if the energy of the combined system is measured, it always returns just one of the energy eigenvalues $$E_1$$ or $$E_2$$ (corresponding to $$\omega_1$$ and $$\omega_2$$). After measurement, the wavefunction collapses and the PDF becomes stationary.

__The Gaussian Wavepacket.__  The _Gaussian wavepacket_ is a common wavefunction used to model a free particle. It's wavefunction has a Gaussian shape, so the density is Normal $$\psi^*\psi \sim N$$. This makes it ideal for modeling localized particles. 

Consider the following initial wavepacket in momentum-space:


$$
\bar\psi(p,0) = \frac{1}{(2\pi \sigma_p^2)^{1/4}} \exp (-\frac{(p-p_0)^2}{4\sigma_p^2})
$$


When squared, this wavepacket is a Gaussian centered around $$p_0$$ with spread $$\sigma_p$$. In position space the corresponding wavefunction is


$$
\psi(x,0) = \left( \frac{4 \sigma_p^2 \hbar^2}{2\pi} \right)^{1/4} \exp(-\sigma_p^2 x^2 /\hbar^2) \exp(ip_0x/\hbar)
$$


Which is a Gaussian function multiplied by a wave factor. By inspection, position space uncertainty is related to momentum space uncertainty by $$\sigma_x \sigma_p = \hbar/2$$, which is exactly the lower limit of the Heisenberg uncertainty relation.

Plugging $$\psi(x,0)$$ into the SE we find that it's _not_ a solution, but this shouldn't come as a surprise—we already showed that solutions are planewaves of the form $$A \exp i(kx-\omega t)$$. So technically wavepackets don't describe single particles, _but_ we can add several planewaves together such that their superposition _approximates_ a wavepacket, and the sum of planewaves _is_ a solution to the SE, so in this sense wavepackets are realistic.

Plugging $$\bar \psi(p,0)$$ into the GSE solution and taking the integral gives


$$
\psi(x,t) = \frac{(2\pi\sigma_x^2)^{-1/4}}{\left(1+i\frac{\hbar}{2m\sigma_x^2}\right)^{1/2}}\exp \frac{-x^2+\frac{i}{\hbar}(4\sigma_x p_0 x + 2\sigma_x^2p_0^2t)}{4\sigma_x^2(1+i\frac{\hbar}{2m\sigma_x^2}t)}
$$


This is a complicated looking wavefunction, but its density is a simple Gaussian:


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


So the center of the wavepacket moves with "group velocity" $$p_0/m$$ just like a classical particle, and the dispersion of the phase waves causes the packet to spread over time. The spread increases like $$\sqrt{1+t^2}$$, so the particle becomes less localized and the product $$\sigma_x\sigma_p$$ rises above the Heisenberg lower limit.

What happens when a Gaussian wavepacket is measured? If its energy is measured to be, say, $$E_0$$ then the wavefunction collapses to the eigenfunction corresponding to that energy, namely $$\exp(ix\sqrt{2mE_0}/\hbar)$$. But recall that this eigenfunction isn't normalizable, so this wavepacket model comes with a warning regarding its realism. 

## 2. Harmonic Oscillator

The quantum harmonic oscillator is modeled like the classical harmonic oscillator—with a quadratic potential. The Hamiltonian is


$$
\mathbf{H} = \frac{\mathbf{P}^2}{2m} + \frac{1}{2}m\omega^2\mathbf{X}^2 = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + \frac{1}{2}m\omega^2x^2
$$


where $$\omega$$ is the oscillator's frequency parameter. Plugging this into the GSE gives


$$
i\frac{\partial \psi}{\partial t} = -\frac{\hbar}{2m} \frac{\partial^2 \psi}{\partial x^2} + \frac{m \omega^2}{2\hbar}x^2\psi
$$


This PDE can be simplified by recalling that the solution is the sum of energy eigenvectors multiplied by the time-dependant factor $$\exp(-iE_it/\hbar)$$. So the first step is to find the eigenvectors and eigenvalues of 


$$
\mathbf{H}\psi_E = E\psi_E
$$


where $$\psi_E$$ is an energy eigenvector corresponding to the energy eigenvalue $$E$$. The ODE this produces is


$$
-\frac{\hbar^2}{2m}\frac{d^2 \psi_E}{d x^2} + \frac{1}{2} m \omega^2 x^2 \psi_E = E\psi_E
$$


It turns out that this equation has solutions for every value of $$E$$, including complex $$E$$, but only a small few of them normalize, the rest diverge and therefore don't represent physical states. The ones that converge _do_ represent physical states, and it's these states we're looking for.

Deriving the normalizable states requires a lot of math that isn't especially relevant to the physics, so I'll just present the results: for each $$0 \le n$$ the $$n$$th energy eigenvalue is


$$
E_n = \left( n + \frac{1}{2} \right)\hbar\omega
$$


and the corresponding wavefunction is


$$
\psi_n(x) = \sqrt{\frac{a}{2^n n! \sqrt{\pi}}} H_n(ax) e^{-a^2x^2/2}
$$


where $$a = \sqrt{\omega m / \hbar}$$ and $$H_n$$ are _Hermite polynomials_. The probability densities of the first few energies are shown below along with the potential energy function. Any harmonic oscillator wavefunction can be written as a sum of these eigenfunctions, weighted by a coefficient that can be interpereted as "the amount" of each energy level in the initial condition. 

<center><img src="quantum/harmonic_oscillator_probabilities.png" style="object-fit:contain;"></center>


There are a few interesting things to notice…

* The minimum energy is not zero—it's $$\hbar \omega /2$$. So for an oscillator to even exist in the first place some energy is involved. This can be understood in terms of the uncertainty principle: suppose we try to make the energy zero by closely localizing the particle to $$x=0$$ where the potential energy is zero. In this case the momentum will be very spread out, and momentum has energy associated with it. On the other hand if we try to set the particle at rest so it has no momentum then the position will be spread out, in particular it will be spread out away from $$x=0$$ and therefore have potential energy. So either way the oscillator has _some_ energy.
* Hermite polynomials are orthogonal. They better be—they're eigenvectors!
* The probability density is non-zero outside the potential energy curve, so the particle can be found _beyond_ the classical region.
* There are points in the classical region where the density is zero, so the particle will _never_ be measured there even though classically it can be.
* In the limit of large $$n$$ the quantum density approaches the classical density.



## 3. Particle in a Box

The _particle in a box_ models a particle constrained within a volume. As always the solution approach is to write a Hamiltonian and then find it's eigenfunctions and eigenvalues. This time, however, the potential isn't continuous—it's piecewise. Specifically, it's zero inside the box and infinity outside. The infinite potential outside the box models the walls that the particle isn't allowed to cross.

Already we know the wavefunction is zero outside the box, and inside it's that of a free particle. But what about the walls? At the walls the wavefunction has to be continuous, and outside the box the wavefunction is $$0$$, therefore $$\psi(0) = \psi(L) = 0$$. This constraint enables the wavefunction to normalize, unlike the free particle.

Inside the box the solution is 
$$
\psi(x) = e^{ix\sqrt{2mE}/\hbar}
$$




, which normalizes to



## 4. Tunnelling



## 5. Hydrogen atom



## References

* Gaussian wavepacket integrals: [1](https://ocw.mit.edu/courses/6-974-fundamentals-of-photonics-quantum-electronics-spring-2006/235adf962a3ef4772b2f494261e00d4b_chapter4.pdf), [2](https://here.isnew.info/inverse-fourier-transform-of-the-gaussian-function.html)





{% include disqus.html %}
