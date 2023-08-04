---
layout: default
---

# Quantum Mechanics Part 3: Applications

<center><img src="" style="zoom:80%;"></center>

$$\newcommand{\bra}[1]{\left<#1\right|}\newcommand{\ket}[1]{\left|#1\right>}\newcommand{\bk}[2]{\left<#1\middle|#2\right>}\newcommand{\bke}[3]{\left<#1\middle|#2\middle|#3\right>}$$

## 1. Free Particle

A particle is said to be "free" when no forces act on it. In the absence of forces there are no potentials and the Hamiltonian is


$$
\mathbf{H} = \frac{\mathbf{P}^2}{2m} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}
$$


Plugging this into the GSE gives the free particle PDE:


$$
\frac{\partial \psi(x,t)}{\partial t} = \frac{i\hbar}{2m} \frac{\partial^2 \psi(x,t)}{\partial x^2}
$$


This has the form of a diffusion equation but with a complex diffusion coefficient. We'll see that the complex nature of the coefficient causes solutions to be waves. 

To solve it we use the solution derived earlier for discrete vectors:


$$
\ket{\Psi(t)} = \sum_i \bk{E_i}{\Psi(0)} e^{-iE_it/\hbar} \ket{E_i}
$$


Converting this to continuous space gives


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

At this point it's reasonable to ask why there are any dynamics at all, given there aren't any forces. The reason is that the wavefunction is a sum of plane waves $$\exp i(kx-\omega t)$$ weighted by the amount of each such "phase wave" in the initial state $$\bar \psi(p,0)$$. Each wave moves at a different speed, called its phase velocity, and this causes the shape of the wavefunction to change over time. If instead the phase waves all moved at the same speed then the initial wavefunction would be preserved and there wouldn't be any dynamics beyond motion at constant velocity.

The speed of each phase wave is


$$
v(k) = \omega/k = E/p = p/2m =\hbar k/2m
$$


Where $$k=p/\hbar$$ and $$\omega=p^2/2m\hbar = \hbar k^2/2m =E/\hbar$$. So waves with smaller wavelength move faster—they have more energy.

Note that $$k$$ and $$\omega$$ are not independent quantities. They have a dispersion relation


$$
\omega (k) = \frac{\hbar k^2}{2m}
$$


__The Gaussian Wavepacket.__ A Gaussian wavepacket is a wavefunction having Gaussian, or Normal, density $$\psi^*\psi \sim N$$. Distributions like this are interesting because they're localized in space, in contrast to planewaves. Consider the following wavepacket in momentum-space:


$$
\bar\psi(p,0) = \frac{1}{(2\pi \sigma_p^2)^{1/4}} \exp (-\frac{(p-p_0)^2}{4\sigma_p^2})
$$

This wavepacket, when squared, is a Gaussian centered around $$p_0$$ with spread $$\sigma_p$$. In position-space this wavefunction is


$$
\psi(x,0) = \left( \frac{4 \sigma_p^2 \hbar^2}{2\pi} \right)^{1/4} \exp(-\sigma_p^2 x^2 /\hbar^2) \exp(ip_0x/\hbar)
$$


Which is a Gaussian multiplied by a wave factor. By inspection, position-space uncertainty is related to momentum-space uncertainty by $$\sigma_x \sigma_p = \hbar/2$$, which is exactly the lower limit of the Heisenberg uncertainty relation.

Plugging $$\psi(x,0)$$ into the SE we find that it's _not_ a solution, which shouldn't come as a surprise—we already showed that solutions are planewaves of the form $$A \exp i(kx-\omega t)$$. So technically wave-packets don't describe single particles, _but_ we can add several planewaves together such that their superposition _approximates_ a wavepacket, and the sum of planewaves _is_ a solution to the SE, so in this sense wavepackets are physically realistic.

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


So the wavepacket moves to the right with "group velocity" $$p_0/m$$, just like a classical particle. It's interesting to note that group velocity is different from phase velocity. The dispersion of the phase waves causes the wavepacket to spread as it travels. The spread increases like $$\sqrt{1+t^2}$$, so the particle becomes less localized with time and the product $$\sigma_x\sigma_p$$ increases above the uncertainty lower limit.



## 2. Harmonic Oscillator






{% include disqus.html %}
