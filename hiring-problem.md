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

The solution is to hire when $$P(1 \vert \texttt{bsf}) \ge V(r+1)$$, otherwise pass.

### Computing the $P$s and the $V$s

The value function has a term for the best-so-far outcome and a term for the not-best-so-far ourcome:

$$V(r) = V(r \vert \texttt{bsf})P(\texttt{bsf} \vert r) + V(r \vert \neg\texttt{bsf})(1-P(\texttt{bsf} \vert r))$$

Here, $$P(\texttt{bsf} \vert r)$$ is the probability that candidate $$r$$ will be the best-so-far after their interview.  To compute this probability, we need to count the number of ways $$\texttt{bsf}$$ can happen.

Here's an example.  Suppose there are 5 candidates and we're about to interview candidate 3.  The following are possible rank outcomes, ordered left to right by order of interview:

$$\rightarrow \texttt{34152}$$

$$\rightarrow \texttt{43251}$$

$$\texttt{32514}$$

$$\rightarrow \texttt{45312}$$

$$\rightarrow \texttt{45321}$$

$$\texttt{23451}$$

$$\vdots$$

These are the outcomes we would see if we interviewed to the end. If we're at $$r=3$$, the arrowed outcomes are the ones that have $$\texttt{bsf}=True$$. Our job is to count the number of arrowed outcomes and divide by the total number of possible outcomes.

To start, observe that $$\texttt{bsf}=True$$ when $$rank(3) \in \{1,2,3\}$$.  For each rank in this set, there are a different number of ways to fill in the other 4 ranks. For example, if $$rank(3)=3$$, then the only ranks that can be to the left are 4 and 5, but if $$rank(3)=2$$, then the ranks that can be to the left are 3, 4, and 5.  Note that the number of possible ranks to the left can exceed the number of spaces to the left, and that the ranks to the left and right of $$r$$ are independently permutable.  For example, both $$\texttt{45312}$$ and $$\texttt{54321}$$ have $$\texttt{bsf}=True$$.

Putting this all together we get

$$P(\texttt{bsf} \vert r )=\frac{1}{R!} \sum_{i=1}^{R-r+1}N(i)$$

where

$$N(i) = \binom{R-i}{r-1}(r-1)!(R-r)!$$

The probability simplifies conveniently to $$1/r$$.

Next, let's look at $$V(r \vert \neg \texttt{bsf})$$.  This one's much easier.  This is the case where we automatically pass to the next candidate, in otherwords $$V(r \vert \neg \texttt{bsf}) = V(r+1)$$. Done.

Now $$V(r \vert \texttt{bsf})$$.  This is where we know candidate $$r$$ is best-so-far.  So what's the value then?  It's the value of choosing the optimal decision.  If the decision is pass, then we move to $$r+1$$ and the value is $$V(r+1)$$. If the decision is keep, then the value is the probability they're rank-1; this probability we'll call $$P(1 \vert \texttt{bsf})$$.  So we have

$$V(r \vert \texttt{bsf}) = \max \left\{ P(1 \vert \texttt{bsf}), V(r+1) \right\}$$

To calculate $$P(1 \vert \texttt{bsf})$$ our job is to count the number of ways a candidate can be rank-1, assuming they're best-so-far, and divide by the total number of ways they can be best-so-far.  $$N(i)$$ does exactly that:

$$P(1 \vert \texttt{bsf}) = \frac{N(1)}{\sum_{i=1}^{R-r+1}N(i)}$$

Which simplifies conveniently to $$r/R$$.

Finally, putting all the pieces together we end up with

$$V(r) = \max \left\{ P(1 \vert \texttt{bsf}), V(r+1) \right\} \frac{1}{r} + V(r+1)(1-1/r)$$

And the optimal policy is to hire if $$r$$ is the best so-far and $$r/R  \ge V(r+1)$$.