$$\newcommand{\bra}[1]{\left<#1\right|}\newcommand{\ket}[1]{\left|#1\right>}\newcommand{\bk}[2]{\left<#1\middle|#2\right>}\newcommand{\bke}[3]{\left<#1\middle|#2\middle|#3\right>}$$

## Composite Systems & Entanglement

To describe quantum systems composed of otherwise isolated systems, we use multiply-indexed basis vectors. For example, if a composite system consists of two objects, one having 3 possible measurement outcomes and another having 2, then the composite system is defined in terms of six basis vectors: $$\ket{00}$$, $$\ket{01}$$, $$\ket{02}$$, $$\ket{10}$$, $$\ket{11}$$, $$\ket{12}$$. The first symbol in the ket denotes the first object's contribution to the overall state and the second symbol denotes the second object's contribution. Together they describe a _single_ measurement possibility of the composite system.

As with isolated systems, composite states are linear combinations of basis vectors. For example, if a composite system has two subsystems (which is the number of subsystems we'll exclusively look at in this post), we get


$$
\ket{\psi}=\sum_{ij}a_{ij}\ket{ij}
$$


States are subject to the usual normalization constraint


$$
\sum_{ij} \lvert a_{ij} \rvert^2 = 1
$$


and coefficients have the usual probabilistic interperetation: $$\lvert a_{ij} \rvert^2$$ is the probability that a measurement of the first system returns state $$i$$ and a measurement the second system returns state $$j$$.

In terms of naming conventions, it's standard to call the first subsystem Alice and the second one Bob, and if there's a third it's called Charlie.

__Observables.__ How are observables represented for composite systems? The same way they are for isolated systems—with operators, but now each subsystem has its own set of operators which act independently on their part of the system.

For example, consider a sytem of two spins. The most general state is


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


The pattern is that $$\sigma$$ acts only on Alice's part of each basis vector and $$\tau$$ acts only on Bob's. The table below summarizes the action of each operator on each basis. 

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
P(\tau_z=-1) &= \sum_j \lvert \braket{j0}{\psi} \rvert^2 \\
&= \lvert \braket{00}{\psi} \rvert^2 + \lvert \braket{10}{\psi} \rvert^2 \\
&= \lvert a \rvert^2 + \lvert c \rvert^2 \\
P(\tau_z=+1) &= \sum_j \lvert \braket{j1}{\psi} \rvert^2 \\
&= \lvert \braket{01}{\psi} \rvert^2 + \lvert \braket{11}{\psi} \rvert^2 \\
&= \lvert b \rvert^2 + \lvert d \rvert^2
\end{align*}
$$


If for example Alice measures her spin to be $$-1$$ then the overall state collapses to


$$
\ket{\psi'} = \frac{a\ket{00} + b\ket{01}}{\sqrt{\lvert a \rvert^2 + \lvert b \rvert^2}}
$$


where the denominator is a normalization factor. Note that unless Alice tells Bob about her measurement result, this new state vector _belongs only to Alice_. Bob's model of the system is still the original vector


$$
a\ket{00} + b\ket{01}+c\ket{10}+d\ket{11}
$$

and Bob's probability calculations will be based on _this_ vector, while Alice's will be based on the updated vector $$\ket{\psi'}$$. It's important to note that this difference in knowledge between Alice and Bob is not due to Alice's measurement changing Bob's spin in any way, it's simply a matter of Alice knowing which of Bob's outcomes are still feasible given her knowledge of her system, information that Bob doesn't have access to.

When Bob measures his half of the system state collapses to one of the basis vectors and the measurement of the composite
