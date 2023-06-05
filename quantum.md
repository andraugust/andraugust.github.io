---
layout: default
---

# Notes on Quantum Mechanics

<center><img src="" style="zoom:80%;"></center>
$$\newcommand{\bra}[1]{\left<#1\right|}\newcommand{\ket}[1]{\left|#1\right>}\newcommand{\braket}[2]{\left<#1\middle|#2\right>}\newcommand{\bke}[3]{\left<#1\middle|#2\middle|#3\right>}$$

### 1. Systems and Experiments

One way to start learning about quantum mechanics is by comparing it to classical mechanics, and this is how the book begins, with a comparison between a classical spin experiment and its quantum analog.

The experiment is to measure spin using an apparatus that can be oriented arbitrarily in space. In the classical system suppose we do the following: orient the apparatus in the $$+z$$ direction, measure the spin, and find it to be $$+1$$. Now we orient the apparatus in the $$-z$$ direction, measure the spin and find it to be $$-1$$. How about orienting the apparatus in the $$+x$$ direction? In this case we measure $$0$$. After a few more configurations and measurements we find that spin can be modeled effectively as a unit vector $$\hat{\sigma}$$ oriented in 3-space relative to the apparatus direction $$\hat{a}$$ and the measurement we get is $$\hat{a} \cdot \hat{\sigma}$$.

Now lets do the same experiment on a quantum spin. Measuring $$\pm z$$ we get the same results, but when we measure $$x$$ we don't get $$0$$. Instead we get $$+1$$, different from the classical spin. Let's measure again. Now we get $$-1$$. Measuring again and again we get $$+1$$s and $$-1$$s in seemingly random order, with no $$0$$s and nothing in between. After taking more measurements a pattern emerges. The quantum result is the same as the classical result but only on average. In other words $$\left< \sigma \right> = \hat{a} \cdot \hat{\sigma}$$.

So between classical and quantum mechanics the notion of determinism changes, as does the notion of measureable states (classical spin measurements are real-values between $$-1$$ and $$+1$$ but quantum spin is binary). What's more, classical states are unchanged by measurements. For example, measuring along $$z$$ and then $$x$$ and then $$z$$ returns the original measurement of $$z$$: measuring $$x$$ doesn't affect the outcome of measuring $$z$$. In quantum mechanics this isn't always true. The intermediate measurement of  $$x$$ changes the system such that re-measuring $$z$$ may not return the original value. To gain intuition for why this is, it's helpful to remember that quantum systems are so fragile that any measurement energetically strong enough to be useful is necessarily strong enough to change the system in a significant, whereas classically the energy used for measurement has negligible impact on the system itself.

### 2. Quantum States

Quantum states are modeled as vectors in a space called Hilbert space. In Hilbert space vectors can be real or complex and infinite dimensional. Vectors are drawn as kets $$\ket{A}$$ and they have complex conjugates, called bras, drawn backward $$\ket{A}^{*} = \bra{A}$$. Vectors have inner products $$\braket{A|B}^{*} = \braket{B|A}$$, orthogonalities $$\braket{A|B} = 0$$, and unit-normalization $$\braket{A|A} = 1$$. The familiar vector proprties of commutativity, associativity, distributivity and closedness.

In general, quantum states are simply denoted by $$\ket{A}$$, but it's often useful to represent them concretely in terms of components:

$$
\ket{A} = \sum_i \alpha_i \ket{i}
$$

where $$\ket{i}$$ are orthonormal basis vectors and $$\alpha_i$$ are complex components. Note that this way of representing $$\ket{A}$$ requires the selection of a particular basis and the values $$\alpha_i$$ will in general change from basis to basis.

As an example, let's represent quantum spin in this formalism. Let $$\ket{u}$$ and $$\ket{d}$$ be orthonormal bases for the $$z$$ measurement such that an arbitrary state prior to measurement is represented as

$$
\ket{A} = \alpha_u \ket{u} + \alpha_d \ket{d}
$$

Defining $$\ket{u}$$ and $$\ket{d}$$ as orthogonal is important because it encodes the fact that they are distinct states: measuring $$z$$ returns $$\ket{u}$$ or $$\ket{d}$$, never both.

The values of $$\alpha_u$$ and $$\alpha_d$$, when squared and normalized, represent measurement probabilities. In other words, $$\alpha_u^*\alpha_u$$ is the probability of measuring $$\sigma_z = +1$$ and preparing $$\ket{u}$$, while $$\alpha_d^*\alpha_d$$ is the probability of measuring $$\sigma_z = -1$$ and preparing $$\ket{d}$$. These are probabilities, so they need to be normalized:
$$
\sum_i \alpha_i^*\alpha_i = \braket{A|A} = 1
$$

Because $$\alpha_i = \braket{i|A}$$, we can express the probability of preparing $$\ket{i}$$ as
$$
p_i = \braket{A|i}\braket{i|A}
$$

So, components are related to measurement probabilities. What are they for $$u$$ and $$d$$? It depends on how the system is prepared prior to measurement. If it's prepared in $$\ket{l}$$ the components with have certain values, if it's prepared in $$\ket{r}$$ they may have different values. Same goes for the other bases and how they're prepared prior to measurement. 

To make progress at this point then, and actually find values for components, we have to pick a basis and write components in terms of them. Let's use $$\ket{u}$$ and $$\ket{d}$$.

Start with the $$x$$ measurement. To capture the 50% measurement outcome from the spin experiment, we simply set 
$$
\ket{r} = \frac{1}{\sqrt{2}} \ket{u} + \frac{1}{\sqrt{2}} \ket{d}
$$

Next, for $$\ket{l}$$, it may seem like we can use the same coefficients because it also has 50% measurement outcomes, but this doesn't satisfy orthogonality $$\braket{r|l} = 0$$. To satisfy orthogonality the solution is
$$
\ket{l} = \frac{1}{\sqrt{2}} \ket{u} - \frac{1}{\sqrt{2}} \ket{d}
$$

Similar logic applies for the $$y$$ measurement and the states $$\ket{i}$$ and $$\ket{o}$$. This time, however, we have to consider the fact that the 50% measurement outcome is true both when the system is prepared in a $$z$$ state _or_ an $$x$$ state. The results are
$$
\ket{i} = \frac{1}{\sqrt{2}} \ket{u} + \frac{i}{\sqrt{2}} \ket{d}
$$

$$
\ket{o} = \frac{1}{\sqrt{2}} \ket{u} - \frac{i}{\sqrt{2}} \ket{d}
$$



### 3. Principles of Quantum Mechanics

The principles of quantum mechanics are formulated around the idea of measureables, that is to say, the outcomes of experiments. They state that:

* Measureables, such as spin, are represented by Hermitian operators.
* Quantum states, such as $$\ket{u}$$ or $$\ket{d}$$, are the eigenvectors these operators.
* The measureable quantities themselves, such as $$\pm1$$ for spin, are the eigenvalues.
* When a particular eigenvalue is measured, the system is said to be _prepared_ in the corresponding eigenstate.
* Distinguishable states are represented by orthogonal vectors.
* If a system is in state $$\ket{A}$$, the probability of measuring $$\lambda$$ is $$\braket{A|\lambda}\braket{\lambda|A}$$.

Why are the operators Hermitian? Because Hermitian operators have certain desireable properties:

* They're linear.
* Their eigenvalues are always real, meaning that measurements made in real life return real numbers.
* Unique eigenvalues have orthogonal eigenvectors.
* Their eigenvectors form a complete set, meaning that any vector the operator can generate can be written as a linear combination of the eigenvectors.

Because Hermitian operators implicitly define eigenvectors and eigenvalues we can think of them as "packaging up", or encoding information about observables. The principles, meanwhile, give us a sense for how to use eigenquantities once they've been calculated from such an operator, or, conversely, how to construct an operator if the eigenquantities are known.

As an example, let's construct the spin operators from what we know about its eigenquantities. These operators are $$2\times2$$ matrices we'll call $$\sigma_x$$, $$\sigma_y$$, and $$\sigma_z$$. For $$\sigma_z$$ we know the eigenvalues are $$\pm1$$ and the eigenvectors are $$\ket{u}$$ and $$\ket{d}$$. This means that
$$
\sigma_z \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}
$$

$$
\sigma_z \begin{pmatrix} 0 \\ 1 \end{pmatrix} = -\begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

Similarly, for $$\sigma_x$$,
$$
\sigma_x \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$

$$
\sigma_x \begin{pmatrix} 1 \\ -1 \end{pmatrix} = -\begin{pmatrix} 1 \\ -1 \end{pmatrix}
$$

And similar for $$\sigma_y$$. Solving for the components of each matrix we get the so-called Pauli matrices that represent quantum spin:
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

So far we've only measured spin along $$x$$, $$y$$, and $$z$$, but the results above enable us to measure spin in any direction $$\hat{n}$$. This is done by taking the dot product of the Pauli matrices with $$\hat{n}$$. The resulting operator describes measurements in any direction. 

For example, measuring in the direction $$\hat{n}=(\frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}},0)$$, the operator is

$$
\frac{1}{\sqrt{2}} 
\begin{pmatrix}
0 & 1-i \\
1+i & 0 \\
\end{pmatrix}
$$
The eigenvalues are still $$\pm 1$$ but the eigenvectors are now
$$
\begin{align*}
	\ket{+1} &= \frac{1}{2}\begin{pmatrix} 1-i \\ \sqrt{2} \end{pmatrix} \\
	\ket{-1} &= \frac{1}{2}\begin{pmatrix} -1+i \\ \sqrt{2} \end{pmatrix} \\
\end{align*}
$$
What are the measurement probabilities if the spin starts in $$\ket{u}$$?
$$
P(+1) = \lvert \braket{+1|u} \rvert^2  = \frac{1}{2}
$$
The result is the same for $$P(-1)$$, which isn't surprising given the measurement is at 45deg.

{% include disqus.html %}
