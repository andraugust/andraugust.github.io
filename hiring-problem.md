---
layout: default
---

# The Hiring Problem

### The problem

Suppose you're interviewing candidates for a job.  A job that _must_ be filled by the best candidate, otherwise your company is bound for failure.  The candidates you interview are top-notch, but this means they have offers on the table from your competitor, and they'll take those offers unless you hire them on the spot.

The candidates are rank-able, so they can be sorted ordinally according to how fit they are.  A candidate's fitness is determined after you interview them, at which time you either hire or pass to the next candidate.  If you pass, you can't return to make them an offer in the future (they've accepted the job from your competitor).  Your objective is to hire the top-ranking candidate.  What's your strategy?

###The optimal heuristic

First I'll tell you the optimal heuristic, then we'll solve for the details.

The optimal heuristic is to automatically pass on a fixed number of candidates and then select the first who's better than everyone interviewed so far.  If no better candidate is found then select the last one (you have to, they're the only one left).

The intuition is as follows: All ranks are independent, and candidate order is uniformly random, so knowing the relative rank of, say, the first r candidates doesn't help predict the rank of future candidates, so the best we can do is pass on the first several candidates (possibly only one) and hope to find the best after this.  As for choosing, if we did something like "choose the 6th candidate always", we'd ignore information about the 6th candidate.  In particular, since we're trying to find rank-1, if the 6th candidate isn't better than the previous 5, then we know they're not rank-1, so we should pass, even if this means passing until we get to the last candidate (in this version of the problem selecting rank-2 is equally as bad as selecting rank-R.)

So the real question is: what's the cutoff whereaftter we should start looking for the best-so-far?

### Finding the cutoff

I'm going to find the cutoff using backward induction.  Here's the diagram of possible state-actions, for assistance:

<img src="hiring-problem/state-action-diagram.svg" type="image/svg+xml">







Solution and value function



Numeric values and stopping criteria



