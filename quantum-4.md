$$\newcommand{\bra}[1]{\left<#1\right|}\newcommand{\ket}[1]{\left|#1\right>}\newcommand{\bk}[2]{\left<#1\middle|#2\right>}\newcommand{\bke}[3]{\left<#1\middle|#2\middle|#3\right>}$$

## Composite Systems & Entanglement

__States.__ To describe a quantum system composed of several otherwise isolated systems, we use multiply-indexed state vectors. For example, if a composite system consists of two objects, one having 3 possible states and another having 2, then the composite system is spanned by $$3*2$$ basis vectors: $$\ket{00}$$, $$\ket{01}$$, $$\ket{02}$$, $$\ket{10}$$, $$\ket{11}$$, $$\ket{12}$$. Here, the first symbol in the ket denotes the first object's contribution to the overall state and the second symbol denotes the second object's contribution. Together, they describe a _single_ state of the composite system. 

As with non-composite systems, states are linear combinations of basis vectors. For example, if a composite system has two subsystems (which is the number of subsystems we'll exclusively look at), we get
$$
\ket{\psi}=\sum_{ij}a_{ij}\ket{ij}
$$
States are subject to the usual normalization constraint
$$
\sum_{ij}\abs{a_{ij}}^2 = 1
$$
and coefficients have the usual probabilistic interperetation that $$\abs{a_{ij}}^2$$ is the probability that a measurement of the first system returns state $$i$$ and a measurement the second system returns state $$j$$.

In terms of naming subsystems, it's standard to call the first one Alice and the second one Bob, and if there's a third it's usually called Charlie.

__Observables.__ How are observables represented for composite systems? They're represented in the same way as for isolated systems—with operators. But now each subsystem has its own set of operators which act independently on the corresponding part of the subsystem.

For example, consider a sytem of two spins. The most general state is
$$
\ket{\psi} = a\ket{00} + b\ket{01} + c\ket{10} + d\ket{11}
$$
In terms of notation I'm using $$0$$ to represent spin-down and $$1$$ to represent spin-up. Also, I'm working in the $$z$$-basis, so what I was calling $$\ket{+z}$$ in the first set of notes I'm now calling $$\ket{1}$$. The reason for this change is that it's much cleaner to write $$\ket{11}$$ instead of $$\ket{+z+z}$$, etc.

Alice and Bob have their own separate operaters, corresponding to the measurements they make on their part of the system. In particular, Alice has $$\sigma_x$$, $$\sigma_y$$, $$\sigma_z$$, and Bob has $$\tau_x$$, $$\tau_y$$, $$\tau_z$$. In terms of notation, $$\sigma$$ and $$\tau$$ both represent spin observables, but different symbols are used to distinguish Alice's observable from Bob's. An alternative is to write $$\sigma_x^A$$ and $$\sigma_y^B$$, but I prefer no superscripts.

So what do these operators do to states? Here are a few examples:
$$
\begin{align*}
\sigma_z \ket{\psi} &= -a\ket{00} - b\ket{01} + c\ket{10} + d\ket{11} \\
\tau_z \ket{\psi} &= -a\ket{00} + b\ket{01} - c\ket{10} + d\ket{11} \\
\sigma_x \ket{\psi} &= a\ket{10} + b\ket{11} + c\ket{00} + d\ket{01} \\
\end{align*}
$$
The pattern is that $$\sigma$$ acts according to what's in the first entry of the basis vector, and $$\tau$$ acts according to what's in the second entry. The table below summarizes the action of $$\sigma$$ on each basis

| x            | $$\ket{0}$$ | $$\ket{1}$$ |
| ------------ | ----------- | ----------- |
| $$\sigma_x$$ | $$\ket{1}$$ | 2           |
| $$\sigma_y$$ | 2           | 2           |
| $$\sigma_z$$ | 2           | 2           |

