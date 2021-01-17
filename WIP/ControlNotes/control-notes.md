---
layout: default
---

# Notes on Optimal Control

Optimal control usually begins with the analysis of continuous-time linear dynamical systems. These systems are represented by a state vector $$\textbf{x}(t) \in R^n$$ having dynamics defined by an $$n \times n$$ transition matrix $$\textbf{A}$$:

$$\dot{\textbf{x}}(t) = \textbf{Ax}(t)$$

The solution of which is

$$\textbf{x}(t) = e^{\textbf{A} t}\textbf{x}(0)$$

Computing $$e^{\textbf{A} t}$$ explicitly is a bit awkward because it requires a series expansion. If, however, $$\textbf{A}$$ is diagonal, then dynamics are uncoupled and the matrix exponent can be calculated normally for each diagonal entry. Therefore, it's common to diagonalize $$\textbf{A}$$ and work in the eigenstate space.

The eigen-decomposition of $$\textbf{A}$$ returns a diagonal eigenvalue matrix $$\mathbf{\Lambda}$$ and eigen-vector matrix $$\textbf{T}$$. The transition matrix in terms of these is $$\textbf{A} = \textbf{T} \mathbf{\Lambda} \textbf{T}^{-1}$$ and the eigenstate vector is $$\textbf{z} = \textbf{T}^{-1}\textbf{x}$$. The solution in eigenspace is

$$\textbf{z}(t) = e^{\mathbf{\Lambda} t}\textbf{z}(0)$$

Because $$\mathbf{\Lambda}$$ is diagonal, we get the desired simplification $$z_i(t) = e^{\lambda_i t} z_i(0)$$.

In terms of the original state-space, where measurements occur, the solution is

$$\textbf{x}(t) = \textbf{T} e^{\mathbf{\Lambda}t}\textbf{T}^{-1}\textbf{x}(0)$$

Discrete-time systems are treated similarly. The dynamics are

$$\textbf{x}_{t+1} = \textbf{Ax}_t$$

The solution in eigenspace is $$\textbf{z}_{t} = \mathbf{\Lambda}^t\textbf{z}_0$$. The solution in state space is $$\textbf{x}_t = \textbf{A}^t \textbf{x}_0 = \textbf{T}\mathbf{\Lambda}^t\textbf{T}^{-1}\textbf{x}_0$$.

To determine stability, we look at eigenvalues.  Continuous-time systems have $$z_i(t) = e^{\lambda_i t} z_i(0) = e^{(a + ib) t} z_i(0) = e^{at}e^{ibt} z_i(0)$$.  The first factor is exponential and decides if the system with blow-up or not.  The second factor is oscillatory and so doesn't play a role in stability.  Looking at the first factor, we see that dynamics are stable iff $$a\le0$$, which is the same as saying eigenvalues are in the left-half of the complex plane.

For discrete-time we have $$(z_i)_t = \lambda_i^t (z_i)_0 = r^te^{it\theta} (z_i)_0$$. Again, the first factor decides stability and the second factor decides oscillations. Stability happens iff $$r = \sqrt{a^2+b^2} \le 1$$, which is the same as saying eigenvalues are inside the unit circle on the complex plane.















## References

- Mathjax commands https://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm
- Lectures: Steve Brunton's Control Bootcamp https://www.youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m
- Book: "Data Driven Science and Control" by Brunton and Kutz http://databookuw.com/databook.pdf, http://databookuw.com/



{% include disqus.html %}