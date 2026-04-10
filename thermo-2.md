---
layout: default
---

# Notes on Thermodynamics

<center><img src="" style="zoom:100%;"></center>

Thermodynamics is a framework for modelling matter at scales where individual particles can be ignored and only their collective, bulk properties matter. At these scales, a system can be described by a small number of state variables, despite there being an enormous number of degrees of freedom at the microscopic level.

## When is Thermodynamics? 

As it's said, "*all models are wrong but some are useful*". Thermodynamics is no exception. It's only accurate, and therefore useful under certain conditions:

* The number of particles is large, typically $$N \gt 10^{10}$$.
* Macroscopic fluctuations are negligible. For example, in the previous post we saw that energy fluctuations scale as $$\Delta U/ \langle U \rangle \sim 1/\sqrt{N}  $$, which is sufficiently small for $$N \sim 10^{10}$$ .
* The system's energy spectrum is effectively continuous. This happens when $$kT \gg \delta E$$, where $$\delta E$$ is a typical microstate energy spacing.
* Microscopic events happen much faster than macroscopic ones. For example, particle collisions happening much faster than pressure or volume changes.
* The system is in equilibrium, or evolves slowly enough for it to appear so.

## States

When the conditions listed above are true, we can characterize a system using a small number of state variables:

- Pressure $$P$$
- Volume $$V$$
- Temperature $$T$$
- Internal energy $$U$$
- Entropy $$S$$

Although this looks like a 5-dimensional state space, in practice these variables are related to each other in a way that reduces the overall dimensionality. For example, an ideal gas with fixed $$N$$ has

* Equation of state: $$P(T,V) = \frac{kNT}{V}$$
* Energy relation: $$U(T) = \frac{d}{2}kNT$$
* Entropy relation: $$S(V,U) = Nk (\ln V + \frac{f}{2}\ln U) + \text{const}$$

or without constants:

*  $$P \propto T/V$$
*  $$U \propto T$$
*  $$S = a\ln V + b\ln U + c$$

Thus, an ideal gas's state is really only two dimensional. For example, to the full state all we need to know is $$(P,V)$$ or $$(S,U)$$ or $$(T,V)$$, etc. But note that not all pairs of variables work, for example $$(P,S)$$ doesn't determine $$U$$.

## Energy

The energy of a thermal system is defined by its **internal energy** $$U$$, which is simply the total kinetic and potential energy of its particles.

To calculate $$U$$ for a system, we could in principle sum all of the particle energies explicitly, but thermodynamics is about analyzing large systems using a small number of macroscopic variables, ignoring underlying particles, so we'd like to take a different approach. There's also a historical reason: when thermodynamics was developed, the microscopic structure of matter wasn't yet understood, so such a sum wasn't even an option. A macroscopic definition of $U$ was developed instead, and it's what we'll use here. 

The thermodynamic definition of $$U$$ comes from the **first law of thermodynamics** which describes energy flow and says that internal energy changes through just two mechanisms: heat $$Q$$ and work $$W$$
$$
\Delta U = Q + W
$$


### Work

Work is defined as energy transferred by a force acting through a displacement. "Displacement" usually refers to a change in the spatial coordinate of a particle, but in thermodynamics it's defined more generally as changing an **extensive variable**. An extensive variable is any quantity that defines the size or amount of matter in a system, such as volume, mass, etc. This contrasts with **intensive variables** such as temperature and pressure which do not change when volume, for example, is cut in half. 

There are many different types of work. For example, if a system contains charges in a potential $$\phi$$, we can "displace" charge by adding an amount $$dq$$ thereby doing work


$$
dW_{\text{electrical}} = \phi\ dq
$$


Similarly, if we displace a system's volume by $$dV$$ against a pressure $$P$$, the work done is


$$
dW_{\text{mechanical}} = -P\ dV
$$

In general, work takes the form of an extensive displacement times an intensive "force". Going forward, I'll just focus on mechanical work and refer to it simply as $$W$$.

Let's look at two common processes involving work: isothermal and adiabatic.

**Isothermal processes** are where temperature is held constant. In practice, this is acheived by placing the system in contact with a constant-temperature reservoir and changing the system so slowly that its temperature remains equal to the reservoir at all times.

How much does the system's internal energy change in such a process? As an example, an ideal gas has $$U = U(T)$$, so its internal energy actually doesn't change at all. So where does the added energy go? It's all dissipated to the environment as heat. To find out how much heat, we use the first law:


$$
\begin{align}
Q &= -W \\
&= \int P\ dV \\
&= NkT \int_{V_i}^{V_f} \frac{1}{V}\ dV \\
&= NkT \ln \frac{V_f}{V_i}
\end{align}
$$

**Adiabatic processes** are where no heat enters or leaves a system. In practice, this is acheived by thermally insulating a system from its environment. How does internal energy change in this case? From the first law,
$$
\Delta U = W
$$


To calculate $$W$$ we need an explicit formula for $$U$$. For ideal gases we have


$$
\begin{align}
dU &= dW \\
\rightarrow \frac{d}{2}Nk\ dT &= -P\ dV \\
\end{align}
$$


Inserting the ideal gas equation of state and integrating yields


$$
VT^{f/2} = \text{const}
$$


Now, given $$(T_i, V_i, V_f)$$ we can solve for $$T_f$$ and use it to calculate the change in internal energy as $$U(T_f) - U(T_i)$$. (Note that this last equation is equivalent to $$PV^{(f+2)/2} = \text{const}$$.)

### Heat

Heat is defined as energy transfer due to a temperature gradient between two systems. It happens spontaneously, with energy always flowing from the high temperature system to the low temperature one (unless work is supplied to make the process go in reverse, such as a refrigerator, which I'll discuss later).

In terms of terminology, systems don't "have" heat---heat is a mechanism of energy transfer, not a property of a substance. In common language we say objects are "hot" but really we mean they're at a higher temperature than something else and can therefore transfer energy to it via heat. "Hot" object don't physically contain something called heat.

The amount of heat transferred to a system depends on what it's made of, and this is captured by a quantity called **heat capacity**:


$$
C = \frac{\partial Q}{\partial T}
$$

Heat capacity is defined as the amount of heat needed to raise a system's temperature by 1K. Or as I like to think of it, the energy a system gains/loses when it equilibrates with a reservoir that's 1K hotter/cooler than it.

Heat capacity depends on the constraints of the process. Specifically, whether the process is under constant volume or constant pressure conditions. Under constant volume, no work is done, so

$$
\begin{align}
C_V &= \left( \frac{\partial Q}{\partial T} \right)_V \\
&= \left( \frac{\partial U}{\partial T} \right)_V \\
\end{align}
$$


Under constant pressure, volume changes, so work is done and therefore


$$
\begin{align}
C_P &= \left( \frac{\partial Q}{\partial T} \right)_P \\
&= \left( \frac{\partial (U -W)}{\partial T} \right)_P \\
&= \left( \frac{\partial U}{\partial T} \right)_P + P\left( \frac{\partial V}{\partial T} \right)_P \\
\end{align}
$$


For solids and liquids, volume doesn't change much with temperature, so the second term in $$C_P$$ can be ignored and $$C_V \approx C_P$$. For gases, volume changes significantly with temperature. As an example, for an ideal gas,


$$
U = \frac{d}{2}NkT
$$


so


$$
C_V = \frac{d}{2}Nk
$$


and 


$$
C_P = \frac{d}{2}Nk + Nk
$$


Here are some heat capacities per unit mass:

| Material | Specific Heat Capacity (J/(kg·K)) |
|---|---|
| Water (liquid) | 4,186 |
| Ice | 2,090 |
| Steam | 2,010 |
| Air | 1,005 |
| Iron / Steel | 450 |
| Gold | 129 |
| Lead | 128 |

Evidently it takes a lot of energy to raise the temperature of water.

The last thing I'll note about heat is that $$C$$ is defined for a given phase--solid, liquid or gas. If a phase transition occurs then heat energy goes into breaking chemical bonds while temperature stays constant.

## Path Dependence

l;k


## Heat Engines

A natural question to ask next is whether heat can be converted to work, and vice versa. Heat engines do exactly that — they transform the incoherent energy of microscopic particles into coherent macroscopic motion, like the lifting of a weight or the rotation of a drive shaft.

Heat engines have the following components:

* A working substance that absorbs heat and does work, usually a liquid or gas
* A hot reservoir at temperature $$T_H$$ that's the source of heat energy
* A cold reservoir at temperature $$T_C$$ that the engine dumps energy into in order to reset
* An engine body providing the physical mechanism for the transduction

In the examples that follow, the heat engine will be a sealed container of gas (the working substance) with a weighted piston on top. When the gas expands it does work against gravity and when it compresses it does $$PdV$$ work.

The purpose of an engine is to output work continuously, so engines operate in a (idealized) cycle starting and ending at the same point in state space before running again. The cycle has four stages:

1. Heating: the gas is in state $$(T_C, V_C)$$ and placed in contact with the hot reservoir
2. Power stroke: the gas absorbs heat, expanding and does work until it reaches $$(T_H, V_H)$$
3. Cooling: the gas is placed in contact with the cold reservoir
4. Compression: the gas dumps heat into the cold reservoir and compresses until it resets to $$(T_C, V_C)$$

There are many physical ways to implementat a heat engine, but amazingly they all have the same upper limit on their efficiency. To see this, start with conservation of energy


$$
Q_H = Q_C + W
$$


and define efficiency as


$$
\eta = \frac{W}{Q_H} = 1 - \frac{Q_C}{Q_H}
$$


**Example.**



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

For the rest of this discussion I'll only consider systems that change volume, i.e. those involving mechanical work, but the results are easy to generalize.

The fundamental thermodynamic relation assuming only mechanical work becomes


$$
dU = T\ dS - P\ dV
$$


---

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


{% include disqus.html %}