---
layout: default
---

# The Hiring Problem

Suppose you're interviewing candidates for a job.  A job that _must_ be filled by the best candidate, otherwise your company is bound to fail.  The candidates you have lined up are top-notch, but this means they have offers on the table from your competitor, and they'll take those offers unless you hire them on the spot.

Candidates are rank-able, so they can be sorted ordinally according to how fit they are.  A candidate's fitness is determined after you interview them, at which time you either hire or pass to the next candidate.  If you pass on a candidate, you can't make them an offer in the future (they've already accepted the job from your competitor).

Your objective is to hire the top-ranking candidate.  What's your strategy?

### The optimal strategy

First I'll tell you the optimal strategy, then we'll solve for the details.

The optimal strategy is to automatically pass on a fixed number of candidates and then select the first one who's better than the rest seen so far.  If no better candidate is found then select the last one (you have to, they're the only one left).

The intuition is as follows: All ranks are independent and candidate order is uniformly random, so knowing the relative rank of the cadidate's you've interviewed doesn't help predict the relative rank of candidates to come, so the best strategy is to pass on the first several candidates (possibly only one) and hope to find the best after this.  As for when to choose, if you did something like "choose the 6th candidate always", you'd ignore the fact that the 6th candidate might not be better than the first 5, and since you're looking for rank-$$1$$ you should pass, even if this means passing until you get to the last candidate (in this version of the problem selecting rank-$$2$$ is equally as bad as selecting the bottom-ranked candidate).

So the question becomes: what's the cutoff whereafter you should look for the best-so-far?

### Finding the cutoff

I'm going to find the cutoff using backward induction.  Like most backward induction problems, it helps to look at the state-action transition diagram:

<center><img src="hiring-problem/state-action-diagram.svg" type="image/svg+xml"></center>

In the diagram time flows downward, with candidates being interviewed sequentially. Arrows point to outcomes; another interview or the option to hire.

When candidate number $$r$$ is interviewed they can either be the best-so-far or not.  If they're not, we pass automatically (as per the heuristic); if they are, we can either hire or pass.  If we hire, we're done.

Given that a candidate is better than the best so far, we need to decide to hire or pass.  This is done by computing two things: the probability that they're rank-1, and the probability that, if we pass, we'll find and hire rank-1.  Let's call the first quantity $$P(1|r,\texttt{bsf})$$ and the second quantity $$V(r+1)$$.  In the parlance of backward induction $$V$$ is called the _value function_, and $$V(r+1)$$ is the value of being in _state_ $$r+1$$.  $$\texttt{bsf}$$ is a binary variable indicating whether or not the current candidate is the best so far.

The solution is to hire when $$P(1|r,\texttt{bsf}) \ge V(r+1)$$, otherwise pass.

### Computing the $P$s and $V$s

The value function is given by $$V(r) = V(r|\texttt{bsf})\theta_r + V(r|\neg\texttt{bsf})(1-\theta_r)$$

where $$V(r|\texttt{bsf})$$ is the value of being in state $$r$$ given that after the interview $$r$$ is the best-so-far.  Similarly, 



