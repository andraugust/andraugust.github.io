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

Thermodynamics is a framework for modelling the macroscopic properties of matter. It's a coarse-grained approach that allows us to describe systems in terms of a small number of observables, despite there being an enormous number of degrees of freedom at the microscopic level.

## When is Thermodynamics?

As the saying goes, "*all models are wrong but some are useful*". Thermodynamics is no exception, it's only accurate under the following conditions:

* The number of particles is large, typically $$N \gt 10^{10}$$.
* Macroscopic fluctuations are negligible. For example, in the previous post we saw that energy fluctuations scale as $$\Delta U/ \langle U \rangle \sim 1/\sqrt{N}  $$, which is sufficiently small for $$N \sim 10^{10}$$ .
* The system's energy spectrum is effectively continuous. This happens when $$kT \gg \delta E$$, where $$\delta E$$ is a typical microstate energy spacing.
* Microscopic events happen much faster than macroscopic ones. For example, particle collisions happening much faster than pressure or volume changes.
* The system is in equilibrium, or evolves slowly enough for it to appear so.

## States

When the conditions listed above are true, we can characterize the system using a small number of state variables:

- Pressure $$P$$
- Volume $$V$$
- Temperature $$T$$
- Internal energy $$U$$
- Entropy $$S$$

Although this looks like a 5-dimensional state space, in practice these variables are related to each other in a way that reduces the overall dimensionality. For example, an ideal gas with fixed $$N$$ has

* Equation of state: $$P(T,V) = \frac{kNT}{V}$$
* Energy relation: $$U(T) = \frac{f}{2}kNT$$
* Entropy relation: $$S(V,U) = Nk (\ln V + \frac{f}{2}\ln U) + \text{const}$$

or without constants:

*  $$P \propto T/V$$
*  $$U \propto T$$
*  $$S = a\ln V + b\ln U + c$$

Thus, an ideal gas's state is really only two dimensional. For example, to the full state all we need to know is $$(P,V)$$ or $$(S,U)$$ or $$(T,V)$$, etc. But note that not all pairs of variables work, for example $$(P,S)$$ doesn't determine $$U$$.

## Energy

The energy of a thermal system is defined by its **internal energy** $$U$$, which is simply the total kinetic and potential energy of each of its particles.

To calculate $$U$$ we could theoretically sum each particle's energy, but thermodynamics is all about analyzing large systems using a small number of macroscopic variables, ignoring underlying microstates. Besides, when thermodynamics was developed no one actually knew what matter was made of, so such a sum wasn't an option, but the thermodynamic definition of $$U$$ still existed, and that's what we use here. In particular, the first law of thermodynamics describes energy flow and says that internal energy changes through just two mechanisms: heat $$Q$$ and work $$W$$

$$
\Delta U = Q + W
$$

### Work

Work is defined as energy transferred by a force acting through a displacement. "Displacement" usually refers to a change in the spatial coordinate of a particle, but in thermodynamics it's defined more generally as changing an **extensive variable**. An extensive variable is any quantity that defines the size or amount of matter in a system, such as volume, mass, etc.. This is in contrast to **intensive variables** such as temperature and pressure which do not change when a system's volume, for example, is cut in half. 

There are many different types of work. For example, if a system contains charges in a potential $$\phi$$, we can "displace" charge by adding an amount $$dq$$. The work done in this case is

$$
dW_{\text{electrical}} = \phi\ dq
$$


Similarly, if we displace a system's volume $$V$$ against a pressure $$P$$ then the work done is


$$
dW_{\text{mechanical}} = -P\ dV
$$


The negative sign is used to make decreases in volume increase internal energy. Going forward, I'll focus on mechanical work and refer to it simply as $$W$$.

Let's look at two common processes involving work: isothermal and adiabatic.

Isothermal processes are those where temperature is held constant. In practice, this is acheived by placing the system in contact with a constant-temperature reservoir and changing the system so slowly that its temperature remains equal to the reservoir throughout.

How much does the system's internal energy change in such a process? As an example, an ideal gas has $$U = U(T)$$, so isothermally its internal energy doesn't change. Then where does the work energy go? It's all dissipated to the environment as heat. To find out how much heat, we use the first law:


$$
\begin{align}
Q &= -W \\
&= \int P\ dV \\
&= NkT \int_{V_i}^{V_f} \frac{1}{V}\ dV \\
&= NkT \ln \frac{V_f}{V_i}
\end{align}
$$


The other type of process is called adiabatic. It's where no heat enters or leaves the system. In practice, this is acheived by thermally insulating the system from its environment. How does internal energy change in this case? From the first law,


$$
\Delta U = W
$$


We can't calculate $$W$$ like for the isotherm because $$T$$ isn't constant. Instead, we have to use an explicit formula for $$U$$. For an ideal gas we have


$$
\begin{align}
dU &= dW \\
\rightarrow \frac{f}{2}Nk\ dT &= -P\ dV \\
\end{align}
$$


Inserting the ideal gas equation of state and integrating yields


$$
VT^{f/2} = \text{const}
$$


which can be written


$$
PV^{(f+2)/2} = \text{const}
$$


Now, given $$(T_i, V_i, V_f)$$ we can solve for $$T_f$$ and use it to calculate the change in internal energy as $$U(T_f) - U(T_i)$$.

### Heat

Compared to work, heat is much more passive. It's defined as energy transferred due to a temperature gradient between a system and its environment. Note that systems don't "have" heat---heat is a mechanism of energy transfer, not a property of a substance. In common language we say objects "are hot" but really we mean to say they're at a higher temperature and will transfer energy via heat if we touch them. "Hot" object don't physically contain something called heat.



## Path Dependence

l;k


## Cycles

lkj

## Potentials











\begin{align}
df = \grad f \cdot d\mathbf{r} \\
\Rightarrow \int_{\mathbf{r}_1}^{\mathbf{r}_2} df = \int_{\mathbf{r}_1}^{\mathbf{r}_2}\grad f \cdot d\mathbf{r}
\end{align}



* Equation of state: $$P(T,V) = \frac{kNT}{V}$$
* Energy relation: $$U(T) = \frac{f}{2}kNT$$
* Entropy relation: $$S(V,U) = Nk \lparen \ln V + \frac{f}{2}\ln U \rparen + \text{const}$$



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


{% include disqus.html %}