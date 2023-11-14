$$\newcommand{\bra}[1]{\left<#1\right|}\newcommand{\ket}[1]{\left|#1\right>}\newcommand{\bk}[2]{\left<#1\middle|#2\right>}\newcommand{\bke}[3]{\left<#1\middle|#2\middle|#3\right>}$$

## Composite Systems & Entanglement

To describe a quantum system composed of multiple otherwise isolated systems, we use multiply-indexed state vectors. For example, if a composite system consists of two objects, one having 3 possible states and another having 2, then the composite system is defined in terms of six basis vectors: $$\ket{00}$$, $$\ket{01}$$, $$\ket{02}$$, $$\ket{10}$$, $$\ket{11}$$, $$\ket{12}$$. The first symbol in the ket denotes the first object's contribution to the overall state and the second symbol denotes the second object's contribution. Together they describe a _single_ possible measurement outcome for the composite system.

As with isolated systems, composite states are linear combinations of basis vectors. For example, if a composite system has two subsystems (which is the number of subsystems we'll exclusively look at in this post), we get


$$
\ket{\psi}=\sum_{ij}a_{ij}\ket{ij}
$$


States are subject to the usual normalization constraint


$$
\sum_{ij} \lvert a_{ij} \rvert^2 = 1
$$


and coefficients have the usual probabilistic interperetation where $$\lvert a_{ij} \rvert^2$$ is the probability that a measurement of the first system returns state $$i$$ and a measurement the second system returns state $$j$$.

In terms of naming conventions, it's standard to call the first subsystem Alice and the second one Bob, and if there's a third it's called Charlie.

__Observables.__ How are observables represented for composite systems? The same way they are for isolated systems—with operators. But now each subsystem has its own set of operators which act independently on the corresponding part of the subsystem.

For example, consider a sytem of two spins. The most general state is


$$
a\ket{00} + b\ket{01} + c\ket{10} + d\ket{11}
$$


In terms of notation I'm using $$0$$ to represent spin-down and $$1$$ to represent spin-up. Also, I'm working in the $$z$$-basis, so what I called $$\ket{+z}$$ in the first set of notes I'm now calling $$\ket{1}$$. The reason for this change is that it's much easier to write $$\ket{11}$$ instead of $$\ket{+z+z}$$, etc.

Alice and Bob have their own separate operaters, corresponding to their separate observables. In particular, Alice has $$\sigma_x$$, $$\sigma_y$$, $$\sigma_z$$, and Bob has $$\tau_x$$, $$\tau_y$$, $$\tau_z$$. In terms of notation, $$\sigma$$ and $$\tau$$ both represent spin observables but different symbols are needed to distinguish Alice's observables from Bob's. An alternate notation is $$\sigma_x^A$$ and $$\sigma_y^B$$, but I prefer writing it without superscripts.

So what do these operators do to states? Here are a few examples:


$$
\begin{align*}
\sigma_z \ket{\psi} &= -a\ket{00} - b\ket{01} + c\ket{10} + d\ket{11} \\
\tau_z \ket{\psi} &= -a\ket{00} + b\ket{01} - c\ket{10} + d\ket{11} \\
\sigma_x \ket{\psi} &= a\ket{10} + b\ket{11} + c\ket{00} + d\ket{01} \\
\end{align*}
$$


The pattern is that $$\sigma$$ acts only on Alice's part of each basis vector and $$\tau$$ acts only on Bob's. The table below summarizes the action of each operator on each basis. 

|                            | $$\ket{0}$$   | $$\ket{1}$$  |
| -------------------------- | ------------- | ------------ |
| $$\sigma_x$$ or $$\tau_x$$ | $$\ket{1}$$   | $$\ket{0}$$  |
| $$\sigma_y$$ or $$\tau_y$$ | $$-i\ket{1}$$ | $$i\ket{0}$$ |
| $$\sigma_z$$ or $$\tau_z$$ | $$-\ket{0}$$  | $$\ket{1}$$  |

Strictly speaking, the row header for Alice should be $$\ket{0 \cdot}$$ and $$\ket{1 \cdot}$$, and for Bob it should be $$\ket{\cdot0}$$ and $$\ket{\cdot 1}$$, but I think the idea is clear as it's written.

To calculate the probability that Alice or Bob measure a certain outcome, we sum all the ways that the outcome can be measured. For example, the probability that Alice measures $$\sigma_z = +1$$ is
$$
\begin{align*}
P(\sigma_z=+1) &= \lvert \braket{10}{\psi} \rvert^2 + \lvert \braket{11}{\psi} \rvert^2 \\
&= \lvert c \rvert^2 + \lvert d \rvert^2 
\end{align*}
$$


