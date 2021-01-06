---
layout: default
---

# Notes on Optimal Control

Optimal control usually begins with the analysis of continuous-time linear dynamical systems. These systems are represented by a state vector $$\textbf{x}(t) \in R^n$$ having dynamics defined by an $$n \times n$$ transition matrix $$\textbf{A}$$:

$$\dot{\textbf{x}}(t) = \textbf{Ax}(t)$$

The solution of which is

$$\textbf{x}(t) = e^{\textbf{A} t}\textbf{x}(0)$$

The factor $$e^{\textbf{A} t}$$ is awkward to compute explicitly because it requires a series expansion, but if $$\textbf{A}$$ is diagonal then dynamics are uncoupled and the matrix exponent is calculated like a normal exponent for each diagonal entry, so it's common to diagonalize $$\textbf{A}$$ and work in the eigenbasis.

The eigen-decomposition of $$\textbf{A}$$ returns an eigenvalue matrix $$\mathbf{\Lambda}$$ and eigen-vector matrix $$\textbf{T}$$. The transition matrix in terms of these is $$\textbf{A} = \textbf{T} \mathbf{\Lambda} \textbf{T}^{-1}$$ and the state vector is $$\textbf{z} = \textbf{T}^{-1}\textbf{x}$$. The solution in eigenspace is

$$\textbf{z}(t) = e^{\mathbf{\Lambda} t}\textbf{z}(0)$$

Because $$\mathbf{\Lambda}$$ is diagonal (containing the eigenvalues of $$\textbf{A}$$), we get the simplification:

$$z_i(t) = e^{\lambda_i t} z_i(0)$$

In terms of the original state-space where measurements occur (presumably), the solution is

$$\textbf{x}(t) = \textbf{T} e^{\mathbf{\Lambda}t}\textbf{T}^{-1}\textbf{x}(0)$$

For discrete-time systems the analysis is similar. The dynamics are

$$\textbf{x}_{t+1} = \textbf{Ax}_t$$

The solution in eigen space is $$\textbf{z}_{t} = \mathbf{\Lambda}^t\textbf{z}_0$$ and the solution in state space is $$\textbf{x}_t = \textbf{A}^t \textbf{x}_0 = \textbf{T}\mathbf{\Lambda}^t\textbf{T}^{-1}\textbf{x}_0$$.

To determine stability, we look at eigenvalues.  Continuous-time systems have $$(z_i)_t = e^{\lambda_i t} (z_i)_0 = e^{(a + ib) t} (z_i)_0 = e^{at}e^{ibt} (z_i)_0$$.  The first factor is exponential and the second factor is oscillatory.  Thus, dynamics are stable iff $$a\le0$$. 

For discrete-time we have $$(z_i)_t = \lambda_i^t (z_i)_0 = r^te^{it\theta} (z_i)_0$$. Again the first factor is exponential and the second factor is oscillatory, so stability happens iff $$r = \sqrt{a^2+b^2} \le 1$$.







## References

- Mathjax commands https://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm
- Lectures: Steve Brunton's Control Bootcamp https://www.youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m
- Book: "Data Driven Science and Control" by Brunton and Kutz http://databookuw.com/databook.pdf, http://databookuw.com/



{% include disqus.html %}