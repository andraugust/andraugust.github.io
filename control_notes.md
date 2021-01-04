---
layout: default
---

##Notes on Optimal Control

Optimal control usually begins with the analysis of continuous-time linear dynamical systems. These systems are represented by a state vector $$\textbf{x}(t) \in R^n$$ having dynamics defined by an $$n \times n$$ transition matrix $$\textbf{A}$$:

$$\textbf{\dot x}(t) = \textbf{Ax}(t)$$

The solution of which is

$$\textbf{x}(t) = e^{\textbf{A} t}\textbf{x}(0)$$

The factor $$e^{\textbf{A} t}$$ is awkward to explicitly compute, requiring a series expansion unless $$\textbf{A}$$ is diagonal, so it's common to work in $$\textbf{A}$$'s eigenbasis where dynamics are uncoupled.

The eigen-decomposition of $$\textbf{A}$$ gives us an eigenvalue matrix $$\textbf{\Lambda}$$ and eigen-vector matrix $$\textbf{T}$$. The transition matrix in terms of these is $$\textbf{A} = \textbf{T}\textbf{\Lambda}\textbf{T}^{-1}$$ and the state vector is $$\textbf{z} = \textbf{T}^{-1}\textbf{x}$$. The solution in eigenspace is

$$\textbf{z}(t) = e^{\textbf{\Lambda}t}\textbf{z}(0)$$

Because $$\textbf{\Lambda}$$ is diagonal (containing the eigenvalues of $$\textbf{A}$$), dynamics are uncoupled and we get the simplification:

$$z_i(t) = e^{\lambda_i t} z_i(0)$$

In terms of the original state-space (where measurements (presumably) occur) the solution is

$$\textbf{x}(t) = \textbf{T} e^{\textbf{\Lambda}t}\textbf{T}^{-1}\textbf{x}(0)$$

For a discrete-time system the analysis is similar. The dynamics are

$$\textbf{x}_{t+1} = \textbf{Ax}_t$$

The solution is 





## References

- Mathjax commands https://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm
- Lectures: Steve Brunton's Control Bootcamp https://www.youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m
- Book: "Data Driven Science and Control" by Brunton and Kutz http://databookuw.com/databook.pdf



{% include disqus.html %}