---
layout: default
---

# Notes on Thermodynamics

<center><img src="" style="zoom:100%;"></center>

## Path Dependence

"Doing" thermodynamics generally means calculating how the temperature, pressure, volume or energy of systems change when they interact with eachother. For example, if a gas is heated, what happens to its volume? Or if a liquid evaporates, how much heat does it have to absorb?

To answer questions like these, it's sometimes enough to know only the initial and final state of the system, like its initial and final temperature. Other times, however, it's necessary to know the _path_ the system follows through state space from its initial state to its final state. For example, consider the amount of work done on an ideal gas:

$$
W = -\int P\ dV
$$

Imagine the gas transitions from state $$(P_1, V_1)$$ to state $$(P_2, V_2)$$ via the paths shown in the diagram. We have 
$$
\begin{align}
W_A = P_1\ (V_2 - V_1) \\
W_B = P_2\ (V_2 - V_1)
\end{align}
$$
the two works are different, which demonstrates that work is path _dependent_.

As an example of path _independence_, consider the internal energy of an ideal gas. The internal energy is given by $$U \propto T$$, so the change in internal energy during _any_ process only depends on initial and final states, namely temperature.

Can we determine if a quantity is path dependent without explicitly computing it for different paths and comparing? Yes---using a mathematical thing called exact differentials. The differential expression
$$
F(x,y)\ dx + G(x,y)\ dy
$$
is called an exact differential if there exists a function $$f(x,y)$$ such that
$$
F = \frac{\partial f}{\partial x} \ \text{ and }\  G = \frac{\partial f}{\partial y}
$$
For example, the expression $$y\ dx + x\ dy$$ is an exact differential because it's the total differential of $$f = xy$$. It turns out that exact differentials are path independent, so we can calculate the total change in $$df$$ using just the endpoints:
$$
\int_{\mathbf{r}_1}^{\mathbf{r}_2} df = f(\mathbf{r}_2) - f(\mathbf{r}_1)
$$
On the other hand $$y\ dx$$, for example, is an _inexact_ differential because there's no function $$f$$ such that $$df = y\ dx$$. Note that I've written these differentials in terms of two variables $$x$$ and $$y$$, but in general they can depend on any number of scalar variables.

Thus, in thermodynamics, if a quantity is an exact differnetial then we can compute it by simply looking at end points, otherwise we have to be more careful and consider exactly how the change occurs. Exact differentials will be denoted by $$df$$, while inexact differentials will be denoted by $$\delta f$$ to remind us that path matters.

## Reversibility

Reversibility is an important idealization in thermodynamics in much the same way that "frictionless" is an important idealization in mechanics: it removes all dissipative effects so we can understand the underlying phenomenon before accounting for real-world losses. 

Reversible processes are quasistatic and frictionless, where quasistatic means that change is so slow the system and environment are arbitrarily close to equilibrium at all times. Of course in the limit of true reversibility the process is so slow that it doesn't happen, which is what makes this an idealization. As we'll see, if a system and environment can be returned to their initial state without producing entropy then the process is reversible.

## Energy

There are a few mechanisms through which thermodynamic systems can gain or lose energy. From the previous post on statistical thermodynamics, the general change in internal energy of a system (assuming constant particle number) is given by

$$
dU = T\ dS - P\ dV
$$

The first term, $$T\ dS$$, is the heat transfer into the system. Heat is defined as energy transferred due to a temperature gradient. It's important to note that substances don't "have" heat, they only absorb or dissipate it, which is why heat is sometimes described as thermal energy in _transit_. Heat is a mechanism of energy transfer and not a property of a substance. Heat is an inexact differential:

$$
\delta Q = T\ dS
$$

The second term, $$-P\ dV$$, is the mechanical work done _on_ the system (hence the negative sign), and it too is an inexact differential:
$$
\delta W = -P\ dV
$$
Note that the sum of these two inexact differentials is an exact one.

## Heat Capacity

The amount of heat needed to raise a substance's temperature varies from one substance to another. To quantify this variability we use _heat capacity_, defined as
$$
C = \frac{\delta Q}{dT}
$$
This is a strange looking derivative because it mixes $$\delta$$s with $$d$$s. To actually make the calculation we need to specify $$how$$ heat is added. If heat is added at constant volume we have
$$
C_V \equiv \left( \frac{\partial Q}{\partial T} \right)_V
$$
and if heat is added at constant pressure we have
$$
C_P \equiv \left( \frac{\partial Q}{\partial T} \right)_P
$$


---

Thermodynamics is a framework for describing the macroscopic properties of bulk matter. It's a coarse-grained model which allows us to focus an a small number of macroscopic observables.

## The Domain of Validity

As the saying goes, *all models are wrong, but some are useful*. Thermodynamics is no different. It has a domain of validity and that domain is characterized by the following conditions:

* The number of particles in the system is large, typically $$N \gt 10^{10}$$.
* Macroscopic fluctuations are negligible. For example, in a previous post we found that at equilibrium the relative energy fluctuations scale as $$\Delta U/ \langle U \rangle \sim 1/\sqrt{N}  $$, which is sufficiently small for $$N \sim 10^{10}$$ . 
* The system's energy spectrum is effectively continuous. This happens when $$kT \gg \delta E$$, where $$\delta E$$ is a typical microstate energy spacing.
* Microscopic events happen much faster than macroscopic events, such as when particle collisions happening much faster than pressure or volume changes.
* The system is in equilibrium, or evolves slowly enough for it to appear so.

## State

When the conditions listed above are true, we can characterize the system with a small number of state variables:

- Particle number $$N$$
- Pressure $$P$$
- Volume $$V$$
- Temperature $$T$$
- Internal energy $$U$$
- Entropy $$S$$

From this, it seems that thermodynamic state-space is 6 dimensional. In practice, however, these states are related to each other in ways that reduce the overall dimensionality. For example, an ideal gas with fixed $$N$$ has

* Equation of state: $$P(T,V) = \frac{kNT}{V}$$
* Energy relation: $$U(T) = \frac{f}{2}kNT$$
* Entropy relation: $$S(V,U) = Nk \lparen \ln V + \frac{f}{2}\ln U \rparen + \text{const}$$

or without so many constants:

* $$P \propto T/V$$
* $$U \propto T$$
* $$S = a\ln V + b\ln U + c$$

Thus, an ideal gas's state is actually two dimensional. For example, we can fully specify all state variables if we know $$(P,V)$$ or $$(S,U)$$ or $$(T,V)$$, etc. But note that not all pairs of variables work, for example $$(P,S)$$ doesn't determine $$U$$.

## Energy

The energy of a thermodynamic system is captured by the fundamental thermodynamic relation:

$$
dU = T\ dS + \sum_i X_i\ dY_i
$$

Here, $$X_i$$ is a generalized force and $$Y_i$$ is the corresponding generalized displacement, together they account for a type of __work__. Here are a few examples of force-displacement pairs:

| Type of work    | Generalized Force $$X_i$$ | Generalized Displacement $$Y_i$$ |
| --------------- | ------------------------- | -------------------------------- |
| Mechanical      | $$-P$$                    | $$V$$                            |
| Surface tension | $$\gamma$$                | $$A$$                            |
| Electrical      | $$\Phi$$                  | $$Q$$                            |
| Chemical        | $$\mu$$                   | $$N$$                            |

For the rest of this discussion I'll only consider systems that change volume, i.e. those involving mechanical work, but the results are easy to generalize.

The fundamental thermodynamic relation assuming only mechanical work becomes

$$
dU = T\ dS - P\ dV
$$

The first term, $$T\ dS$$, is the heat transfer into a system. **Heat** is defined as energy transfer due to a temperature gradient. It's important to note that substances don't "have" heat, they only absorb or dissipate it, which is why heat is sometimes called thermal energy in _transit_: it's a mechanism of energy transfer, not a property of a substance.

## State Change











\begin{align}
df = \grad f \cdot d\mathbf{r} \\
\Rightarrow \int_{\mathbf{r}_1}^{\mathbf{r}_2} df = \int_{\mathbf{r}_1}^{\mathbf{r}_2}\grad f \cdot d\mathbf{r}
\end{align}



* Equation of state: $$P(T,V) = \frac{kNT}{V}$$
* Energy relation: $$U(T) = \frac{f}{2}kNT$$
* Entropy relation: $$S(V,U) = Nk \lparen \ln V + \frac{f}{2}\ln U \rparen + \text{const}$$





{% include disqus.html %}