---
layout: default
---

# Quantum Mechanics Part 1: Systems, States and Principles

<center><img src="quantum/dalle-square-840.jpg" style="object-fit:contain;"></center>

$$\newcommand{\bra}[1]{\left<#1\right|}\newcommand{\ket}[1]{\left|#1\right>}\newcommand{\bk}[2]{\left<#1\middle|#2\right>}\newcommand{\bke}[3]{\left<#1\middle|#2\middle|#3\right>}$$

## 1. Systems and Experiments

One way to start understanding quantum mechanics is by comparing it to classical mechanics, and this is how Susskind and Friedman's book begins—with a comparison between a classical spin experiment and its quantum analog.

The experiment is to measure the spin of a particle using an apparatus that can be oriented arbitrarily in space. The goal is to develop a model which captures the relationship between the spin of the particle, the orientation of the apparatus and the measurement it returns. 

For the classical system, suppose we orient the apparatus in the $$+z$$ direction, measure the spin, and find it to be $$+1$$. Next, we orient the apparatus in the $$-z$$ direction, measure the spin, and find it to be $$-1$$. Next, orient in the $$+x$$ direction and measure $$0$$. After more configurations and measurements we find that spin can be modeled as a unit vector $$\hat{\sigma}$$ oriented in 3-space relative to the apparatus direction $$\hat{a}$$, and the measurement is $$\hat{a} \cdot \hat{\sigma}$$. Note that we've assumed spin to be unaffected by all measurements—spin is a physical state existing independent of the apparatus and any measurement we take leaves it unchanged. As we'll see, this is not the case in QM.

Now let's do the same experiment on quantum spin. Measuring $$\pm z$$ we get the same results, but when we measure $$x$$ we don't get $$0$$ like in the classical experiment, instead we get $$+1$$. Starting the experiment over and taking the same measurements to verify results, we now find that $$x$$ has spin $$-1$$. If we restart the experiment several times we get $$+1$$s and $$-1$$s in seemingly random order, with no $$0$$s and no other numbers in between. After taking more measurements a pattern emerges: the quantum result is the same as the classical result but only on average. In other words $$\left< \sigma \right> = \hat{a} \cdot \hat{\sigma}$$.

So between CM and QM the notion of determinism changes, as does the notion of measureable states: classical spin is real-valued between $$-1$$ and $$+1$$, but quantum spin is binary. Also, classical states are unchanged by measurements. For example, measuring along $$z$$ and then $$x$$ and then $$z$$ returns the original measurement of $$z$$—measuring $$x$$ doesn't affect the outcome of measuring $$z$$. In quantum mechanics this isn't always true. The intermediate measurement of  $$x$$ changes the system such that re-measuring $$z$$ may not return the original measurement. To develop intuition for why this is, it's helpful to remember that quantum systems are so small that any measurement energetically strong enough to be useful is necessarily strong enough to change the system in a significant way, whereas classically the energy used to measure a system has negligible impact on the system itself.

## 2. Quantum States

Quantum states are modeled as vectors in a space called Hilbert space. In Hilbert space vectors can be real or complex and have finite or infinite dimensionality. An example of an infinite-dimensional vector is a continuous-valued function.

Notationally, vectors in Hilbert space are drawn as kets $$\ket{A}$$ and have complex conjugates—called bras—drawn backward $$\ket{A}^{*} = \bra{A}$$. Vectors have inner products $$\bk{A}{B}^{*} = \bk{B}{A}$$, orthogonalities $$\bk{A}{B} = 0$$, and unit-normalization $$\bk{A}{A} = 1$$. The familiar vector properties of commutativity, associativity, distributivity and closedness all hold. 

A general quantum states is simply denoted as $$\ket{A}$$, but it's often useful to represent them explicitly in terms of components:


$$
\ket{A} = \sum_i a_i \ket{i}
$$


where $$\ket{i}$$ are orthonormal basis vectors and $$a_i$$ are complex components. Note that this way of representing $$\ket{A}$$ requires selecting a specific basis, and the values $$a_i$$ in general change from one basis to another.

__Spin States.__ How is quantum spin represented in this formalism? Let $$\ket{+z}$$ and $$\ket{-z}$$ be orthonormal bases for the $$z$$ measurement such that an arbitrary state prior to measurement is


$$
\ket{A} = a_+ \ket{+z} + a_- \ket{-z}
$$


Defining $$\ket{+z}$$ and $$\ket{-z}$$ as orthonormal is important because it encodes the fact that they are distinct: measuring $$z$$ returns $$\ket{+z}$$ or $$\ket{-z}$$ but never both.

The values of $$a_+$$ and $$a_-$$ when squared and normalized represent measurement probabilities—this is a principle of QM. In other words, $$a_+^{*}a_+$$ is the probability of measuring $$\sigma_z = +1$$ and configuring the system to $$\ket{+z}$$, while $$a_-^{*} a_-$$ is the probability of measuring $$\sigma_z = -1$$ and configuring the system to $$\ket{-z}$$. As probabilities, they normalize:


$$
\sum_i a_i^*a_i = \bk{A}{A} = 1
$$


Because $$a_i = \bk{i}{A}$$, the probability of preparing $$\ket{i}$$ can be expressed as


$$
p_i = \lvert\bk{i}{A}\rvert^2 = \bk{A}{i}\bk{i}{A}
$$


So, components are related to measurement probabilities, what are they for $$+$$ and $$-$$? It depends on how the system is prepared prior to measurement. If a $$y$$ state is prepared then the components will have certain values and if a $$x$$ state is prepared then they may have different values. 

To actually find values for components we have to pick a basis and write components down in terms of them. $$\ket{+z}$$ and $$\ket{-z}$$ are orthogonal, so they can be used as bases.

Starting with the $$\ket{+x}$$ measurement, the 50% measurement outcome from the spin experiment is captured by defining it as


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

It's important to point out that states in QM have a very different interpretation compared to states in classical mechanics. In CM, states and measurements are the same thing: measuring the state $$(q,p)$$ returns the measurement $$(q,p)$$. In QM measuring the state $$\ket{+z}$$ does not return the measurement $$\ket{+z}$$, instead it returns a number, namely $$+1$$.

As a final comment on states, note that multiplying them by a phase factor $$e^{i\theta}$$, where $$\theta$$ is real, does nothing to change outcome probabilities.

## 3. Principles

The principles of QM are formulated around the idea of measureables, i.e., the outcomes of experiments. They state that:

* Measureables (such as spin) are represented by Hermitian operators, which are defined as having the property $$\mathbf{H^\dagger} = \mathbf{H}$$.
* Quantum states (such as $$\ket{+z}$$ and $$\ket{-z}$$) are eigenvectors of these operators.
* Measurement outcomes (such as $$\pm1$$) are eigenvalues of these operators.
* When an eigenvalue is measured the system is said to be _prepared_ in the corresponding eigenstate.
* Distinguishable states are represented by orthogonal vectors.
* If a system is in state $$\ket{A}$$ the probability of measuring $$\lambda$$ is $$p(\lambda)=  \lvert\bk{\lambda}{A}\rvert^2$$.

Why Hermitian operators? Hermitian operators have a few desirable mathematical properties:

* They're linear, which is appropriate because states are vectors in a linear vector space. 
* Their eigenvalues are always real, meaning that measurements always return real numbers.
* Unique eigenvalues have orthogonal eigenvectors, which means there's an unambiguously distinct state associated with each unique measurement outcome (for a given operator).
* Their eigenvectors form a complete set, meaning that any vector the operator can generate can be written as a linear combination of its eigenvectors.

Hermitian operators implicitly define eigenvectors and eigenvalues such that they "package up" or encode the information about observables. The principles, meanwhile, describe how eigenquantities are used to calculate measurement probabilities once they're calculated from an operator, or, conversely, how to construct an operator if its eigenquantities are known.

__Spin Operators.__ How are spin operators constructed from their eigenvalues and eigenvectors? The answer is by using the matrix identity $$\mathbf{X} = \mathbf{P}\mathbf{\Lambda}\mathbf{P}^{-1}$$, where $$\mathbf{P}$$'s columns are the eigenvectors of $$\mathbf{X}$$ and $$\mathbf{\Lambda}$$ is diagonal with eigenvalues of $$\mathbf{X}$$. 

Spin operators are $$2\times2$$ matrices called $$\mathbf{\sigma}_x$$, $$\sigma_y$$, and $$\sigma_z$$. For example, $$\sigma_y$$ is


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


What can we do with these? So far we've only measured spin along $$x$$, $$y$$, and $$z$$. These operators allow us to make measurements in any direction. This is done by taking the dot product of the Pauli matrices with the measurement-direction vector $$\hat{n}$$.

For example, measuring along $$\hat{n}=(1/\sqrt{2},1/\sqrt{2},0)$$, the operator is


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


These eigenvectors can be used to calculate measurement probabilities. For example, if the spin starts in $$\ket{+z}$$ the measurement probabilities are


$$
P(+1) = \lvert \bk{+n}{+z} \rvert^2  = 1/2 \\
P(-1) = \lvert \bk{-n}{+z} \rvert^2  = 1/2
$$

The two probabilities are equal because the measurement is taken at 45 degrees.

__Sequential Measurement.__ What happens after a measurement is made? The answer is that the particle "collapses to", or becomes "prepared in", one of the eigenstates of the operater being measured. 

For example, consider a particle with initial spin state (in the $$z$$ basis)


$$
\ket{A} = \begin{pmatrix} a \\ b \end{pmatrix}
$$


If $$\sigma_x$$ is measured then the outcome probabilities prior to measurement are


$$
\begin{align*}
P(\sigma_x = +1) &= \lvert\bk{+x}{A}\rvert^2  = \frac{1}{2}(1+a^*b+ab^*) \\
P(\sigma_x = -1) &= 1 - P(+1) = \frac{1}{2}(1-a^*b-ab^*)
\end{align*}
$$


Immediately after measuring the state collapses to either $$\ket{+x}$$ or $$\ket{-x}$$. If $$\sigma_x$$ is measured again it's guaranteed to return the same state. On the other hand, if a different spin is measured, then the outcome probabilities are all $$1/2$$, as per the definition of each state. For example, if the first measurement returned $$\sigma_x = +1$$ and we measure $$\sigma_z$$, then the outcome probabilities are


$$
P(\sigma_z = +1) = \lvert\bk{+z}{+x}\rvert^2 = 1/2 \\
P(\sigma_z = -1) = \lvert\bk{-z}{+x}\rvert^2 = 1/2
$$


## 4. Last

States, operators, and principals wrap up the first part of QM. They lay the foundation over which more  interesting systems can be modeling, such as particles, forces, dynamics, and entanglement, all of which will be covered in the posts to follow. To be continued…



{% include disqus.html %}