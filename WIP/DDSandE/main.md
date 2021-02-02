---
layout: default
---

# Notes on Dynamic Mode Decomposition

## Overview

Main objectives in data-driven dynamical systems analysis:

- Learning nonlinear dynamics models from data. Approaches: dynamic mode decomposition (DMD), sparse identification of nonlinear dynamics (SINDy), Koopman methods 
- Learning coordinate transformations that map non-linear systems to equivalent linear ones. Approach: Koopman methods
- Handling high-dimensional systems. Approach: reduced order modeling (ROM)

## Dynamic Mode Decomposition

DMD is a data-driven method for linear modeling.  Given several samples of a system's state $$ [\textbf{x}_1, \textbf{x}_2, ..., \textbf{x}_T] $$, where $$\textbf{x}_t$$ is a column vector representing the state at time $$t$$, DMD finds a best-fit transition matrix $$\textbf{A}$$ such that $$\textbf{x}_{t+1} \approx \textbf{A}\textbf{x}_t$$ for all $$t$$ in the dataset.

To find $$\textbf{A}$$ it's convenient to work with $$ \textbf{X} = [\textbf{x}_1, \textbf{x}_2, ..., \textbf{x}_{T-1}] $$ and $$ \textbf{X}' = [\textbf{x}_2, \textbf{x}_3, ..., \textbf{x}_T] $$, so that $$\textbf{X}' = \textbf{A}\textbf{X}$$.









## References

- http://databookuw.com/databook.pdf
- http://databookuw.com/
- https://epubs.siam.org/doi/book/10.1137/1.9781611974508

{% include disqus.html %}