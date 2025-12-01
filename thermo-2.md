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

Reversibility is an important idealization in thermodynamics in much the same way that "frictionless" is an important idealization in mechanics: it removes all dissipative effects so we can understand an underlying phenomenon before accounting for real-world losses. 

A reversible process one which is quasistatic and frictionless, where quasistatic means the change is so slow that the system and environment are arbitrarily close to equilibrium at all times. Of course in the limit of true reversibility the process is so slow that it doesn't even happen, which is why reversibility is an idealization. As we'll see, if a system and its environment can be returned to their initial state without producing entropy, the process is reversible.

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

* Thermodynamics studies many particle systems at the bulk scale, where state is defined by P, V, T, U, S, N. I'll assume there's only one particle species, but generalizing to multiple species is straightforward.
* So the state of a thermodynamic system is a point in 6-d space, however these variables are often related by physical constraints such that only a subset of the space is accessible. For example, an ideal gas has 
  * Equation of state: PV = kNT
  * Energy relation: U = fNkT/2
  * Entropy relation: $$S = Nk \left[\ln\!\left(\frac{V}{N}\left(\frac{4\pi m}{3 h^{2}}\frac{U}{N}\right)^{3/2}\right)+\frac{5}{2}\right]$$
* So state is fully specified by three variables, for example P, V and N are typical choices. This freedom of choice sometimes makes this subject confusing because there are so many ways of doing the same thing.
* In thermodynamics the general relation between state variables is given by the thermodynamic identity
  * dU = TdS - PdV + udN
* We derived this in the previous post but basically it comes from defining U = U(S, V, N), taking the total differential and associating the partial derivatives with the state variables.
* The thermodynamic identity generalizes easily to multiple particle species, but for now I'll assume there's one and that it doesn't change, so
  * dU = TdS - PdV
* The thermodynamic identity is useful in that it specifies how a system's energy changes as it moves through state space.
* The first term is energy added through heat, which is defined as energy transferred as the result of a temperature gradient.
* The second term is energy added through mechanical work. The negative sign assures that energy is added to a system when its volume decreases.
* There are other types of work that can be done on a system, such as electromagnetic or elastic,
* For example, suppose we want to know how much a system's energy changes when 





\begin{align}
df = \grad f \cdot d\mathbf{r} \\
\Rightarrow \int_{\mathbf{r}_1}^{\mathbf{r}_2} df = \int_{\mathbf{r}_1}^{\mathbf{r}_2}\grad f \cdot d\mathbf{r}
\end{align}


{% include disqus.html %}