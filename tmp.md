---
layout: default
---

##Notes on Optimal Control

Optimal control usually begins with the analysis of continuous-time linear dynamical systems. These systems are represented by a state vector ${\bf x}(t) \in R^n$ having dynamics defined by an $n \times n$ transition matrix ${\bf A}$:

$${\bf \dot x}(t) = {\bf Ax}(t)$$

The solution of which is

$${\bf x}(t) = e^{ {\bf A} t }{\bf x}(0)$$

The factor $e^{{\bf A}t}$ is awkward to explicitly compute, requiring a series expansion unless ${\bf A}$ is diagonal, so it's common to work in ${\bf A}$'s eigenbasis where dynamics are uncoupled.

The eigen-decomposition of ${\bf A}$ gives us an eigenvalue matrix ${\bf \Lambda}$ and eigen-vector matrix ${\bf T}$. The transition matrix in terms of these is ${\bf A} = {\bf T}{\bf \Lambda}{\bf T}^{-1}$ and the state vector is ${\bf z} = {\bf T}^{-1}{\bf x}$. The solution in eigenspace is

$${\bf z}(t) = e^{{\bf \Lambda}t}{\bf z}(0)$$

Because ${\bf \Lambda}$ is diagonal (containing the eigenvalues of ${\bf A}$), dynamics are uncoupled and we get the simplification:

$$z_i(t) = e^{\lambda_i t} z_i(0)$$

In terms of the original state-space (where measurements (presumably) occur) the solution is

$${\bf x}(t) = {\bf T} e^{{\bf \Lambda}t}{\bf T}^{-1}{\bf x}(0)$$

For a discrete-time system the analysis is similar. The dynamics are

$${\bf x}_{t+1} = {\bf Ax}_t$$

The solution is 





## References

- Mathjax commands https://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm
- Lectures: Steve Brunton's Control Bootcamp https://www.youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m
- Book: "Data Driven Science and Control" by Brunton and Kutz http://databookuw.com/databook.pdf



{% include disqus.html %}