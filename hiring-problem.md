---
layout: default
---

# The Hiring Problem

Suppose you're interviewing candidates for a job.  A job that _must_ be filled by the best candidate, otherwise your company is bound to fail.  The candidates you have lined up are top-notch, but this means they have offers on the table from your competitor, and they'll take those offers unless you hire them on the spot.

Candidates are rank-able, so they can be sorted ordinally according to how fit they are.  A candidate's fitness is determined after you interview them, at which time you either hire or pass to the next candidate.  If you pass on a candidate, you can't go back and make them an offer in the future (they've already accepted your competitor's offer).

Your objective is to hire the top-ranking candidate.  What's your strategy?

### The optimal strategy

First I'll tell you the optimal strategy, then we'll solve for the details.

The optimal strategy is to automatically pass on a fixed number of candidates and then select the first one who's better than the rest seen so far.  If no better candidate is found, select the last one (you have to, they're the only one left).

The intuition is as follows: All ranks are independent, and candidate order is uniformly random, so knowing the relative rank of the cadidate's you've interviewed doesn't help predict the relative rank of candidates to come, so the best strategy is to pass on the first several candidates (possibly only one) and hope to find the best one after this.  As for _when_ to choose, if you did something like "choose the 6th candidate always", you'd ignore the fact that the 6th candidate might not be better than the first 5, and since you're looking for rank-$$1$$ you should pass, even if this means passing until you get to the last candidate (in this version of the problem selecting rank-$$2$$ is equally as bad as selecting the bottom-ranked candidate).

So the question becomes: what's the cutoff after which you should start looking for the best-so-far?

### Finding the cutoff

I'm going to find the cutoff using backward induction.  Like most backward induction problems, it helps to look at a state-action transition diagram:

<center><img src="hiring-problem/state-action-diagram.svg" type="image/svg+xml"></center>

In the diagram time flows downward, with candidates being interviewed sequentially. Arrows point to outcomes, which can either be another interview or an option to hire.

When candidate number $$r$$ is interviewed they can either be the best-so-far or not.  If they're not, we pass automatically (as per the heuristic); if they are, we can hire or pass.  If we hire, we're done.

Given that a candidate is better than the best so far, we need to decide if it's best to hire or pass.  This is done by computing two things: the probability of them being rank-1, and the probability of us finding and hiring rank-1 if we pass.  Let's call the first quantity $$P(1 \vert r,\texttt{bsf})$$ and the second quantity $$V(r+1)$$.  In the parlance of backward induction $$V$$ is called the _value function_ and $$V(r+1)$$ is the value of being in _state_ $$r+1$$.  $$\texttt{bsf}$$ is a binary indicator of if the current candidate is the best-so-far.

The solution is to hire when $$P(1 \vert r,\texttt{bsf}) \ge V(r+1)$$, otherwise pass.

### Computing the $P$s and $V$s

The value function has a term for the best-so-far outcome and a term for the not-best-so-far ourcome:

$$V(r) = V(r \vert \texttt{bsf})P(\texttt{bsf} \vert r) + V(r \vert \neg\texttt{bsf})(1-P(\texttt{bsf} \vert r))$$

Here, $$P(\texttt{bsf} \vert r)$$ is the probability that candidate $$r$$ will be the best-so-far after their interview.  To compute it, we need to count the number of ways $$\texttt{bsf}$$ can happen.  The following are possible rankings of 5 candidates:

$$\rightarrow \texttt{34}\ul{\texttt{2}}\texttt{51}$$

$$\rightarrow \texttt{34}\underline{\texttt{2}}\texttt{51}$$

$$\texttt{32}\underline{\texttt{5}}\texttt{14}$$

$$\rightarrow \texttt{45}\underline{\texttt{3}}\texttt{12}$$

$$\rightarrow \texttt{45}\underline{\texttt{3}}\texttt{21}$$

$$\texttt{23}\underline{\texttt{4}}\texttt{51}$$







