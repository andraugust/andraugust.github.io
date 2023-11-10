$$\newcommand{\bra}[1]{\left<#1\right|}\newcommand{\ket}[1]{\left|#1\right>}\newcommand{\bk}[2]{\left<#1\middle|#2\right>}\newcommand{\bke}[3]{\left<#1\middle|#2\middle|#3\right>}$$

## Composite Systems & Entanglement

__States.__ To describe a quantum system composed of several otherwise isolated systems, we use multiply-indexed state vectors. For example, if a composite system consists of two objects, one having 3 possible states and another having 2, then the composite system is spanned by $$3*2$$ basis vectors: $$\ket{00}$$, $$\ket{01}$$, $$\ket{02}$$, $$\ket{10}$$, $$\ket{11}$$, $$\ket{12}$$. Here, the first symbol in the ket denotes the first object's contribution to the overall state and the second symbol denotes the second object's contribution. Together, two sub-system states describe a _single_ state of their composite system. 

As with non-composite systems, a composite system's state is written as the linear combination of basis vectors. For example, if a composite system has two sub-systems (which is the number we'll exclusively look at), we get
$$
\ket{\psi}=\sum_{ij}a_{ij}\ket{ij}
$$
States are subject to the usual normalization constraint
$$
\sum_{ij}\abs{a_{ij}}^2 = 1
$$
and coefficients have the usual probabilistic interperetation that $$\abs{a_{ij}}^2$$ is the probability that a measurement of the first system returns state $$i$$ and a measurement the second system returns state $$j$$.

In terms of naming sub-systems, it's standard to call the first one Alice and the second one Bob, and if there's a third it's usually called Charlie.

__Measurements.__ How are measurements represented for composite systems? They're represented in the same way as they are for isolated systems—with operators. But now each sub-system has its own set of operators which act independently on the corresponding part of the sub-system.

For example, consider a sytem of two spins. It's most general state is
$$
a_{00}\ket{00} + a_{01}\ket{01} + a_{10}\ket{10} + a_{11}\ket{11}
$$
In terms of notation I'm using $$0$$ to represent spin-down and $$1$$ to represent spin-up. I'm also working in the $$z$$-basis, so what I was calling $$\ket{+z}$$ in the first set of notes I'm now calling $$\ket{1}$$. 

Alice and Bob have their own set of operaters, corresponding to the measurements they can make on their part of the system. In particular, Alice has $$\sigma_x$$, $$\sigma_y$$, $$\sigma_z$$, and Bob has $$\tau_x$$, $$\tau_y$$, $$\tau_z$$. In terms of notation, $$\sigma$$ and $$\tau$$ both "do" the same thing in the sense that they both measure spin, but they're different symbols to make the distinction between Alice's set and Bob's set. An alternative is to write things like $$\sigma_x^A$$ and $$\sigma_y^B$$, but I prefer it without superscripts.

So what happens when an operator is applied?