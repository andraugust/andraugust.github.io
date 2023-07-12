---
layout: default
---

# Notes on Quantum Mechanics

<center><img src="" style="zoom:80%;"></center>

$$\newcommand{\bra}[1]{\left<#1\right|}\newcommand{\ket}[1]{\left|#1\right>}\newcommand{\bk}[2]{\left<#1\middle|#2\right>}\newcommand{\bke}[3]{\left<#1\middle|#2\middle|#3\right>}$$

## 1. Systems and Experiments

One way to start learning about quantum mechanics is by comparing it to classical mechanics, and this is how the book begins—with a comparison between a classical spin experiment and its quantum analog.

The experiment is to measure spin using an apparatus that can be oriented arbitrarily in space. For the classical system, suppose we do the following: orient the apparatus in the $$+z$$ direction, measure the spin, and find it to be $$+1$$. Now, we orient the apparatus in the $$-z$$ direction, measure the spin, and find it to be $$-1$$. Now, orient in the $$+x$$ direction we measure $$0$$. After more configurations and measurements we find that spin can accurately be modeled as a unit vector $$\hat{\sigma}$$ oriented in 3-space relative to the apparatus direction $$\hat{a}$$, and the measurement we get is $$\hat{a} \cdot \hat{\sigma}$$.

Now lets do the same experiment on a quantum spin. Measuring $$\pm z$$ we get the same results, but when we measure $$x$$ we don't get $$0$$, instead we get $$+1$$. Let's measure again. Now we get $$-1$$. Measuring again and again we get $$+1$$s and $$-1$$s in seemingly random order, with no $$0$$s and no other numbers in between. After taking more measurements a pattern emerges: the quantum result is the same as the classical result but only on average. In other words $$\left< \sigma \right> = \hat{a} \cdot \hat{\sigma}$$.

So between classical and quantum mechanics the notion of determinism changes, as does the notion of measureable states: classical spin is real-valued between $$-1$$ and $$+1$$, but quantum spin is binary. Also, classical states are unchanged by measurements. For example, measuring along $$z$$ and then $$x$$ and then $$z$$ returns the original measurement of $$z$$—measuring $$x$$ doesn't affect the outcome of measuring $$z$$. In quantum mechanics this isn't always true. The intermediate measurement of  $$x$$ changes the system such that re-measuring $$z$$ may not return the original value. To develop intuition for why this is, it's helpful to remember that quantum systems are so fragile that any measurement that's energetically strong enough to be useful is necessarily strong enough to change the system significantly, whereas classically the energy used to measure a system has negligible impact on the system itself.

## 2. Quantum States

Quantum states are modeled as vectors in a space called Hilbert space. In Hilbert space vectors can be real or complex and have finite or infinite dimensionality. An example of an infinite-dimensional vector is a continuous-valued function. 

Notationally, vectors in Hilbert space are drawn as kets $$\ket{A}$$ and have complex conjugates—called bras—drawn backward $$\ket{A}^{*} = \bra{A}$$. Vectors have inner products $$\bk{A}{B}^{*} = \bk{B}{A}$$, orthogonalities $$\bk{A}{B} = 0$$, and unit-normalization $$\bk{A}{A} = 1$$. The familiar vector properties of commutativity, associativity, distributivity and closedness all hold. 

In general, quantum states are denoted simply as $$\ket{A}$$, but it's often useful to represent them explicitly in terms of components:


$$
\ket{A} = \sum_i a_i \ket{i}
$$


where $$\ket{i}$$ are orthonormal basis vectors and $$a_i$$ are complex components. Note that this way of representing $$\ket{A}$$ requires selecting a specific basis and the values $$a_i$$ in general change from one basis to another.

__Example.__ How is quantum spin represented in this formalism? Let $$\ket{+z}$$ and $$\ket{-z}$$ be orthonormal bases for the $$z$$ measurement such that an arbitrary state prior to measurement is


$$
\ket{A} = a_+ \ket{+z} + a_- \ket{-z}
$$


Defining $$\ket{+z}$$ and $$\ket{-z}$$ as orthonormal is important because it encodes the fact that they are distinct states: measuring $$z$$ returns $$\ket{+z}$$ or $$\ket{-z}$$ and never both.

The values of $$a_+$$ and $$a_-$$ when squared and normalized represent measurement probabilities—this is a principle of QM. In other words, $$a_+^{*}a_+$$ is the probability of measuring $$\sigma_z = +1$$ and configuring the system to $$\ket{+z}$$, while $$a_-^{*} a_-$$ is the probability of measuring $$\sigma_z = -1$$ and configuring the system to $$\ket{-z}$$. As probabilities, they normalized:

$$
\sum_i a_i^*a_i = \bk{A}{A} = 1
$$


Because $$a_i = \bk{i}{A}$$, the probability of preparing $$\ket{i}$$ can be expressed as


$$
p_i = \bk{A}{i}\bk{i}{A}
$$


So, components are related to measurement probabilities. What are they for $$+$$ and $$-$$? It depends on how the system is prepared prior to measurement. If a $$y$$ state is prepared then the components will have certain values and if a $$x$$ state is prepared then they may have different values. 

To actually find values for components at this point then, we have to pick a basis and write components down in terms of them. $$\ket{+z}$$ and $$\ket{-z}$$ are orthogonal, so lets use them as bases.

Starting with the $$\ket{+x}$$ measurement, the 50% measurement outcome from the spin experiment is captured by writting it as


$$
\ket{+x} = \frac{1}{\sqrt{2}} \ket{+z} + \frac{1}{\sqrt{2}} \ket{-z}
$$


Next, for $$\ket{-x}$$, it may seem like the same coefficients will work because they also capture the 50% measurement outcomes, but that would violate the orthogonality condition $$\bk{+x}{-x} = 0$$. To satisfy orthogonality the solution is


$$
\ket{-x} = \frac{1}{\sqrt{2}} \ket{+z} - \frac{1}{\sqrt{2}} \ket{-z}
$$


Similar logic applies for the $$y$$ measurement and the states $$\ket{+y}$$ and $$\ket{-y}$$. This time, however, we have to consider the fact that the 50% measurement outcome is true when the system is prepared in a $$z$$ state _or_ an $$x$$ state. The results are


$$
\ket{+y} = \frac{1}{\sqrt{2}} \ket{+z} + \frac{i}{\sqrt{2}} \ket{-z}
$$


$$
\ket{-y} = \frac{1}{\sqrt{2}} \ket{+z} - \frac{i}{\sqrt{2}} \ket{-z}
$$

It's important to point out that states in QM have a very different interperetation compared to states in classical mechanics. In CM, states and measurements are the same thing: measuring the state $$(q,p)$$ returns the measurement $$(q,p)$$. In QM measuring the state $$\ket{+z}$$ does not return the measurement $$\ket{+z}$$, instead it returns a number, namely $$+1$$.

As a final comment on states, note that multiplying them by a phase factor $$e^{i\theta}$$, where $$\theta$$ is real, does nothing to change outcome probabilities.

## 3. Principles

The principles of QM are formulated around the idea of measureables, i.e., the outcomes of experiments. They state that:

* Measureables (such as spin) are represented by Hermitian operators, which are defined as having the property $$\mathbf{H^\dagger} = \mathbf{H}$$.
* Quantum states (such as $$\ket{u}$$ and $$\ket{d}$$) are eigenvectors of these operators.
* The measureable quantities themselves (such as $$\pm1$$) are the eigenvalues.
* When an eigenvalue is measured the system is said to be _prepared_ in the corresponding eigenstate.
* Distinguishable states are represented by orthogonal vectors.
* If a system is in state $$\ket{A}$$ the probability of measuring $$\lambda$$ is $$p(\lambda)=\bk{A}{\lambda}\bk{\lambda}{A}$$.

Why Hermitian operators? Because Hermitian operators have a few desireable mathematical properties:

* They're linear, which is appropriate because states are vectors in a linear vector space. 
* Their eigenvalues are always real, meaning that measurements always return real numbers (no one has ever measured a complex-valued length or spin or velocity etc).
* Unique eigenvalues have orthogonal eigenvectors, which means there's an unambiguously distinct state associated with each unique measurement outcome.
* Their eigenvectors form a complete set, meaning that any vector the operator can generate can be written as a linear combination of the eigenvectors.

Because Hermitian operators implicitly define eigenvectors and eigenvalues, they "package up", or encode the information about observables. The principles, meanwhile, describe how eigenquantities can be used to calculate measurement probabilities once they're calculated from an operator, or, conversely, how to construct an operator if its eigenquantities are known.

__Example.__ How are spin operators constructed from their eigenvalues and eigenvectors? By using the matrix identity $$\mathbf{X} = \mathbf{P}\mathbf{\Lambda}\mathbf{P}^{-1}$$, where $$\mathbf{P}$$'s columns are the eigenvectors of $$\mathbf{X}$$ and $$\mathbf{\Lambda}$$ is diagonal with the eigenvalues of $$\mathbf{X}$$. Spin operators are $$2\times2$$ matrices called $$\sigma_x$$, $$\sigma_y$$, and $$\sigma_z$$. For example, $$\sigma_y$$ is


$$
\begin{align*}
\sigma_y &= \frac{1}{2}\begin{pmatrix}
									1 & 1 \\
									i & -i \\
						\end{pmatrix}
						\begin{pmatrix}
									1 & 0 \\
									0 & -1 \\
						\end{pmatrix}
						\begin{pmatrix}
									1 & -i \\
									1 & i \\
						\end{pmatrix} \\
&= \begin{pmatrix}
									0 & -i \\
									i & 0 \\
								\end{pmatrix}
\end{align*}
$$


The rest of the results are the so-called Pauli matrices:


$$
\begin{align*}
		\sigma_x &= \begin{pmatrix}
									0 & 1 \\
									1 & 0 \\
								\end{pmatrix} \\
		\sigma_y &= \begin{pmatrix}
									0 & -i \\
									i & 0 \\
								\end{pmatrix} \\
		\sigma_z &= \begin{pmatrix}
									1 & 0 \\
									0 & -1 \\
								\end{pmatrix} \\
\end{align*}
$$


What can we do with these? So far we've only measured spin along $$x$$, $$y$$, and $$z$$, which are arbitrary reference frames. The operators allow measurement in any direction. This is accomplished by taking the dot product of the Pauli matrices with the direction unit vector $$\hat{n}$$.

For example, measuring along $$\hat{n}=(\frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}},0)$$, the operator is


$$
\frac{1}{\sqrt{2}} 
\begin{pmatrix}
0 & 1-i \\
1+i & 0 \\
\end{pmatrix}
$$


Which has eigenvalues  $$\pm 1$$ and eigenvectors


$$
\begin{align*}
	\ket{+n} &= \frac{1}{2}\begin{pmatrix} 1-i \\ \sqrt{2} \end{pmatrix} \\
	\ket{-n} &= \frac{1}{2}\begin{pmatrix} -1+i \\ \sqrt{2} \end{pmatrix} \\
\end{align*}
$$


These eigenvectors allow measurement probabilities to be calculated. For example, if the spin starts in $$\ket{+z}$$ the measurement probabilities are


$$
P(+1) = \lvert \bk{+n}{+z} \rvert^2  = \frac{1}{2} \\
P(-1) = \lvert \bk{-n}{+z} \rvert^2  = \frac{1}{2}
$$

The two probabilities are equal because the measurement is taken at 45 degrees.

## 4. Time and Change

In CM states are real numbers that change under the influence of forces. In QM states are vectors in  Hilbert space—how do they change?

__Time Evolution Operator.__ To answer this, start by modeling state dynamics generically as
$$
\ket{\psi(t)}=\mathbf{U}(t) \ket{\psi(0)}
$$
where $$\mathbf{U}$$ is called the time evolution operator—it maps states across time. One thing we want $$\mathbf{U}$$ to do is conserve the relationship between states over time. In otherwords, $$\braket{\psi(t)}{\phi(t)} = \braket{\psi(0)}{\phi(0)}$$, which is the same as saying
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


## 5. Particle States

So far the states we've looked at have all been discrete—they're represented by a finite sum over basis vectors. In this section we're going to model particles, which have continuous states for position and momentum. How are continuous states modeled? The answer is in the same way that discrete states are modeled: by the principles of QM. The trick is to observe that nothing in the principles requires states to be discrete, the principles only define conditions and physical interperetations about _vectors_, which can be anything, continuous or discrete, as long as they satisfy the mathematical axioms of vectors (they commute, have an inverse, etc). Complex functions, as it turns out, are vectors, and they are what we'll use to model particles.

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
__Eigenfunctions of Momentum.__ What are the eigenfunctions of momentum? For momentum the set-up and solution are the same, but now $$\bar\psi$$ is used to denote the wave funtion in momentum space:
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
where $$A$$ is determined by the normalization constraint
$$
\bk{\psi}{\psi} = \int_{-\infty}^{\infty} \psi(x)^*\psi(x) \,dx = 1
$$
But this gives
$$
|A|^2\int_{-\infty}^{\infty} \,dx = 1
$$
Which is undefined. This reflects the fact that when particles are unconstrained in space the planewave solution $$\exp(ipx/\hbar)$$ is physically unrealistic. In practice, particles are either constrained in space such that the integration limits are finite, or, if they are un-constrained in space, they're acted on by a potential such that they form a localized wave-packet.

__Changing Basis.__ Generally speaking, an abstract state vector $$\ket{\Psi}$$ can be represented in any basis. For example, in the $$x$$ basis $$\psi(x) = \bk{x}{\Psi}$$, in the momentum basis $$\bar\psi(p) = \bk{p}{\Psi}$$, etc. Because these different representations ultimately correspond to the same thing, namely $$\ket{\Psi}$$, there must be a way to transform between them. How do we transform between the $$x$$ and $$p$$ basis? The trick is to use the identity operator:
$$
I = \int \ket{x}\bra{x} \cdot \,dx
$$
Where $$\cdot$$ is a placeholder for the vector which the operator acts on. Inserting this into the momentum-space representation gives
$$
\begin{align*}
\bar\psi(p) &= \bk{p}{\Psi} \\
&= \bke{p}{I}{\Psi} \\
&= \int \bk{p}{x}\bk{x}{\Psi}\,dx \\
&= \frac{1}{\sqrt{2\pi}} \int e^{-ipx/\hbar} \psi(x) \,dx
\end{align*}
$$
Which is the formula for computing a momentum-space wave function given its position-space complement. The derivation of the inverse operation is similar. The result is
$$
\psi(x) = \frac{1}{\sqrt{2\pi}} \int e^{ipx/\hbar} \bar\psi(p) \,dp
$$
So position and momentum wave-functions are Fourier transforms of eachother.

__Position-Momentum Uncertainty.__ Going back to the discussion of commutators, we found that two observables are simultaneously knowable iff their operators commute. Do the operators for $$x$$ and $$p$$ commute? The answer is no. Given $$\mathbf{X}=x$$ and $$\mathbf{P}=-i\hbar d/dx $$ the commutator is
$$
[\mathbf{X}, \mathbf{P}] = i\hbar
$$
Which means that position and momentum aren't simultaneously knowable—measuring one destroys information about the other, and vice versa. How unknowable are they together? Defining unknowability in terms of the standard deviation $$\Delta$$ of an operator we find from the general uncertainty principal that
$$
\Delta \mathbf{X} \Delta \mathbf{P} \ge \frac{\hbar}{2}
$$
The lower limit on simultaneous uncertainty is reached when either $$\psi$$ or $$\bar \psi$$ are Gaussian function.















{% include disqus.html %}
