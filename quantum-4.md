$$\newcommand{\bra}[1]{\left<#1\right|}\newcommand{\ket}[1]{\left|#1\right>}\newcommand{\bk}[2]{\left<#1\middle|#2\right>}\newcommand{\bke}[3]{\left<#1\middle|#2\middle|#3\right>}$$

## Joint Systems & Entanglement

To describe quantum systems composed of several otherwise isolated systems, we use multiply-indexed basis vectors. For example, if a joint system consists of two objects, one having 3 possible measurement outcomes and another having 2, the joint system is defined in terms of six bases: $$\ket{00}$$, $$\ket{01}$$, $$\ket{02}$$, $$\ket{10}$$, $$\ket{11}$$, $$\ket{12}$$. The first symbol in the ket denotes the first object's contribution to the overall state and the second symbol denotes the second object's contribution. Together they describe a _single_ measurement possibility of the joint system.

As with isolated systems, joint systems are represented by linear combinations of basis vectors. For example, if a joint system has two subsystems (which is the number of subsystems we'll exclusively look at in this post), we get


$$
\ket{\psi}=\sum_{ij}a_{ij}\ket{ij}
$$


States are subject to the usual normalization constraint


$$
\sum_{ij} \lvert a_{ij} \rvert^2 = 1
$$


and coefficients have the usual probabilistic interperetation: $$\lvert a_{ij} \rvert^2$$ is the probability that a measurement of the first system returns state $$i$$ and a measurement the second system returns state $$j$$.

In terms of naming conventions, it's standard to call the first subsystem Alice and the second one Bob, and if there's a third it's called Charlie.

__Observables.__ How are observables represented for joint systems? The same way they are for isolated systems—with operators, but now each subsystem has its own set of operators which act independently on the corresponding part of the system.

For example, consider two spins. The most general state is


$$
a\ket{00} + b\ket{01} + c\ket{10} + d\ket{11}
$$


In terms of notation I'm using $$0$$ to represent spin-down and $$1$$ to represent spin-up. Also, I'm working in the $$z$$-basis, so what I called $$\ket{+z}$$ in the first set of notes I'm now calling $$\ket{1}$$. The reason for this change is that it's much easier to write $$\ket{11}$$ instead of $$\ket{+z+z}$$, etc.

Alice and Bob have their own separate operaters, corresponding to their observables. In particular, Alice has $$\sigma_x$$, $$\sigma_y$$, $$\sigma_z$$, and Bob has $$\tau_x$$, $$\tau_y$$, $$\tau_z$$. In terms of notation, $$\sigma$$ and $$\tau$$ both represent spin observables, but different symbols are needed to distinguish Alice's from Bob's. An alternative notation is $$\sigma_x^A$$ and $$\sigma_y^B$$, but I prefer writing it without superscripts.

So what do these operators do to states? Here are a few examples:


$$
\begin{align*}
\sigma_z \ket{\psi} &= -a\ket{00} - b\ket{01} + c\ket{10} + d\ket{11} \\
\tau_z \ket{\psi} &= -a\ket{00} + b\ket{01} - c\ket{10} + d\ket{11} \\
\sigma_x \ket{\psi} &= a\ket{10} + b\ket{11} + c\ket{00} + d\ket{01} \\
\end{align*}
$$


The pattern is that $$\sigma$$ acts only on Alice's part of each basis vector and $$\tau$$ acts only on Bob's part. The table below summarizes the action of each operator on each basis. 

|                            |  $$\ket{0}$$  | $$\ket{1}$$  |
| :------------------------: | :-----------: | :----------: |
| $$\sigma_x$$ or $$\tau_x$$ |  $$\ket{1}$$  | $$\ket{0}$$  |
| $$\sigma_y$$ or $$\tau_y$$ | $$-i\ket{1}$$ | $$i\ket{0}$$ |
| $$\sigma_z$$ or $$\tau_z$$ | $$-\ket{0}$$  | $$\ket{1}$$  |

To calculate the probability that Alice or Bob measure a certain outcome, we sum the probabilities over all the ways the outcome can be measured. For example, for Alice


$$
\begin{align*}
P(\sigma_z=-1) &= \sum_j \lvert \bk{0j}{\psi} \rvert^2 \\
&= \lvert \bk{00}{\psi} \rvert^2 + \lvert \bk{01}{\psi} \rvert^2 \\
&= \lvert a \rvert^2 + \lvert b \rvert^2 \\
P(\sigma_z=+1) &= \sum_j \lvert \bk{1j}{\psi} \rvert^2 \\
&= \lvert \bk{10}{\psi} \rvert^2 + \lvert \bk{11}{\psi} \rvert^2 \\
&= \lvert c \rvert^2 + \lvert d \rvert^2
\end{align*}
$$


For Bob


$$
\begin{align*}
P(\tau_z=-1) &= \sum_j \lvert \bk{j0}{\psi} \rvert^2 \\
&= \lvert \bk{00}{\psi} \rvert^2 + \lvert \bk{10}{\psi} \rvert^2 \\
&= \lvert a \rvert^2 + \lvert c \rvert^2 \\
P(\tau_z=+1) &= \sum_j \lvert \bk{j1}{\psi} \rvert^2 \\
&= \lvert \bk{01}{\psi} \rvert^2 + \lvert \bk{11}{\psi} \rvert^2 \\
&= \lvert b \rvert^2 + \lvert d \rvert^2
\end{align*}
$$


If for example Alice measures her spin to be $$-1$$ then the overall state collapses to


$$
\ket{\psi'} = \frac{a\ket{00} + b\ket{01}}{\sqrt{\lvert a \rvert^2 + \lvert b \rvert^2}}
$$


where the denominator is a normalization factor. Now, unless Alice tells Bob about her result, this new state _belongs only to Alice_. Bob's model of the system is still the original vector


$$
a\ket{00} + b\ket{01}+c\ket{10}+d\ket{11}
$$


and Bob's probability calculations are based on _this_ vector, while Alice's are based on $$\ket{\psi'}$$. It's important to note that this difference in knowledge between Alice and Bob is not due to Alice's measurement changing Bob's spin in any way, it's simply a matter of Alice knowing which of Bob's outcomes are still feasible given her knowledge of her system—information that Bob doesn't have access to at this point.

When Bob measures his half of the system, and Alice and Bob exchange measurement results, the state collapses to one of the basis vectors and the measurement of the joint system is complete.

__Entanglement.__ Do Alice and Bob always have to exchange measurement outcomes to know the complete state? Interestingly, the answer is no. For example, consider the state


$$
\frac{1}{\sqrt{2}} \left( \ket{10}-\ket{01} \right)
$$


In this state, if Alice measures $$1$$ she immediately knows Bob's state is $$0$$, and vice-versa. This is called _entanglement_, and it resembles the following classical scenario: Charlie has two cards, one marked $$0$$ and the other marked $$1$$. He shuffles the cards, gives one to Alice, the other to Bob. When Alice or Bob look at their card they immediately know what the other person has. 

Although this scenario seems the same as the quantum scenario, it's not. The reason is that in quantum mechanics states aren't determined until they're measured, while in classical mechanics they are. For example, in classical mechanics it makes sense to say "Alice's card was $$0$$ before she looked at it", while in quantum mechanics this statement makes no sense—her card (or spin, or whatever) only acquires its value when she measures it. Furthermore, because Alice's spin and Bob's spin are entangled, Alice's measurement _determines_ Bob's, as if Bob had measured his himself.

Here are the other three entangled states…


$$
\frac{1}{\sqrt{2}} \left( \ket{01}+\ket{10} \right) \\
\frac{1}{\sqrt{2}} \left( \ket{00}+\ket{11} \right) \\
\frac{1}{\sqrt{2}} \left( \ket{11}-\ket{00} \right)
$$


__Tensor Products.__ Going back to probabilities, suppose we want to calculate $$P(\sigma_y=+1)$$. If the system is non-joint we know how to do this. We just calculate


$$
\lvert \bk{+y}{\psi} \rvert^2
$$


where


$$
\ket{\psi} = a\ket{0} + b\ket{1} = \begin{pmatrix}  b \\ a  \end{pmatrix}
$$


and


$$
\ket{+y} = \frac{1}{\sqrt{2}}\left( i\ket{0} + \ket{1} \right) = \frac{1}{\sqrt{2}} \begin{pmatrix}  1 \\ i  \end{pmatrix}
$$


Taking this inner product is straightforward, but how do we do it when $$\ket{\psi}$$ is joint? When $$\ket{\psi}$$ is joint we would have to compute terms like $$\bk{+y}{01}$$ and $$\bk{+y}{11}$$, etc, but we can't do that because $$\ket{+y}$$ and, say, $$\ket{11}$$ live in two different vector spaces. We need to represent $$\ket{+y}$$ in the joint space to take the inner product, and to do that we need a mathematical thing called _tensor products_.

Tensor products, specifically Kronecker products, are a type of matrix multiplication. For two $$2\times2$$ matrices the tensor product is defined as


$$
\mathbf{A} \otimes \mathbf{B} = \begin{pmatrix}
a_{11}\mathbf{B} & a_{12}\mathbf{B} \\ 
a_{21}\mathbf{B} & a_{22}\mathbf{B} 
\end{pmatrix}
$$


which is a $$4\times4$$ matrix. For two $$2\times1$$ vectors the tensor product is


$$
\ket{\psi} \otimes \ket{\phi} = \begin{pmatrix}  \psi_1 \\ \psi_2  \end{pmatrix} \otimes \begin{pmatrix}  \phi_1 \\ \phi_2  \end{pmatrix} = \begin{pmatrix}  \psi_1\phi_1 \\ \psi_1\phi_2 \\ \psi_2\phi_1 \\ \psi_2\phi_2 \end{pmatrix}
$$


Here's a short-list of tensor product properties:

* The Kronecker product is a _type_ of tensor product. Tensor products are more general, but for the purpose of this discussion the Kronecker product does everything we need, so we simply refer to it as if it were _the_ tensor product.
* If the first matrix is $$m\times n$$ and the second is $$p\times q$$, the tensor product is $$mp \times nq$$.
* They don't commute in general.
* They're associative.
* They're distributive.
* Transpose and conjugate transpose distribute: $$(\mathbf{A} \otimes \mathbf{B})^\dagger = \mathbf{A}^\dagger \otimes \mathbf{B}^\dagger$$
* They have a so-called mixed product where $$(\mathbf{A} \otimes \mathbf{B})(\mathbf{C} \otimes \mathbf{D}) = (\mathbf{A}\mathbf{C}) \otimes (\mathbf{B}\mathbf{D})$$ 

So what does this have to do with quantum mechanics? The answer is that joint quantum states are really tensor product states. For example, what we've called $$\ket{01}$$ is really $$\ket{0} \otimes \ket{1}$$, what we've called $$\sigma$$ is really $$\sigma \otimes I$$, and $$\tau$$ is really $$I \otimes \tau$$. 

Looked at in terms of tensor products we see why Alice's operator acts only on her part of the system. For example,


$$
\begin{align*}
\sigma\ket{ab} &\rightarrow (\sigma \otimes I)(\ket{a} \otimes \ket{b}) \\
&= (\sigma \ket{a}) \otimes (I \ket{b}) \\
&= (\sigma \ket{a}) \otimes \ket{b}
\end{align*}
$$

The same is true for Bob. 

Tensor products also capture the experimental observation that Alice and Bob's measurements _are_ compatible. Without tensor products, Alice and Bob's operators don't commute:

$$
[\sigma_i,\sigma_j] = 2i\epsilon_{ijk}\sigma_k
$$


so it seems that Alice and Bob's measurements _aren't_ compatible, and they inherently disturb eachother's spin. But spin tensors _do_ commute:


$$
\begin{align*}
[\sigma,\tau] &\rightarrow (\sigma \otimes I)(I\otimes \tau)-(I\otimes \tau)(\sigma\otimes I) \\
&= \sigma I \otimes I\tau - I\sigma \otimes \tau I \\
&= \sigma \otimes\tau - \sigma\otimes \tau \\
&= 0
\end{align*}
$$


So Alice and Bob can in-fact take independent measurements.



