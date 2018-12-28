---
layout: default
---

<style>
.video-responsive{
    overflow:hidden;
    padding-bottom:56.25%;
    position:relative;
    height:0;
}
.video-responsive iframe{
    left:0;
    top:0;
    height:100%;
    width:100%;
    position:absolute;
}
</style>
<br />

# Reinforcement Learning IRL

<div class="video-responsive"><iframe width="840" height="472" src="https://www.youtube.com/embed/f2nIKFMyfSg?rel=0" frameborder="0" allowfullscreen></iframe></div>
<br />

## The Agent
The agent's body is made of acrylic and has two servos that control two arms.  _The agent's goal is to operate its arms to pull itself forward._ The servos are controlled by a microcontroller (Arduino) that performs one action at each time-step.  The four possible actions are:

- Rotate servo1 up or down by 4 degrees.
- Rotate servo2 up or down by 14 degrees.

The optimal control is a sequence of these actions that move the agent forward at an efficient rate.

## Q-learning
Q-learning is a reinforcement learning algorithm that tries to find optimal actions by learning a state-action _value function_.  The state-action value function, or simply $$Q(s,a)$$, is a table having rows as states, actions as columns, and values as entries.  _Values_ quantify the reward that the agent is expected to collect if it selects the corresponding action from the corresponding state and proceed from-there-on-out by following the optimal policy.  Thus if the value function is known, then the optimal policy is simply to select the action having the highest value for the current state.

The issue is that the $$Q$$-values are initially unknown, so they have to be learned in some way.  Q-learning learns values by exploring the state-action space (literally just trying different action) and updating $$Q$$ based on rewards that are measured after each action.

Thus, the two important components of Q-learning are:

1. Exploring state-action space.
2. Updating $$Q$$.

Many flavors of algorithms have been devised to address these points; we'll focus on one of the simpler and more widely used ones.

__Exploring State-Action Space__.  Exploring state-action space requires us to visit several state-actions and measure their instantaneous rewards, i.e., the reward obtained by performing action $$a$$ from state $$s$$.  Generally state-action space is huge, even for simple problems, so it's necessary to focus exploration in promising regions.  We use an  $$\epsilon$$-greedy approach where the optimal action ($$a = \arg \max_{a}Q(s,a)$$) is selected with probability $$1-\epsilon$$, while an arbitrary action is selected with probability $$\epsilon$$. In addition, we apply a decay that decreases $$\epsilon$$ over time.  This causes the agent to exploit information it's already collected, instead of continuing to explore unvisited state-actions.

__Updating Q__.
$$Q$$ is updated according to the following equation:

$$Q(s,a) \leftarrow Q(s,a) + \alpha (r + \gamma \max_{a}Q(s',a) - Q(s,a))$$

$$s$$ is the agent's current state, $$a$$ is the action it performs, $$r$$ is the instantaneous reward, $$s'$$ is the state the agent finds itself in after the action is performed, and $$\gamma$$ and $$\alpha$$ are parameters.

The update equation is identical to an on-the-fly average $$\overline{x}_{t+1} = \overline{x}_t + ((x_t -\overline{x}_{t})/t)$$ where the "sample" is $$r + \gamma \max_{a}Q_{t}(s',a)$$.  This sample combines the current reward $$r$$ with the future reward $$\max_{a}Q_{t}(s',a)$$ to let information 'leak' backward from $$s'$$ to $$s$$.  This combination allows strong instantaneous rewards to be lessened if the future state is bad, which is intuitively appropriate.  The factor $$\gamma$$ determines the influence of future values on current values, and $$\alpha$$ plays the role of a learning rate.

## Implementation
We implement Q-learning in the robot using an Arduino microcontroller.  The microcontroller takes input from a sonic rangefinder that measures the distance to the wall behind the robot (there needs to be a wall behind the robot).  The distance measurements define the reward $$r$$ as the difference between distances after each action: the distance the robot moved.

At a high level, Q-learning pseudocode looks like:
```python
while True:
    a = get_action(Q[s,:])
    s_new, r = implement_action(a)
    Q = update_Q(s,a,r)
    s = s_new
```

The output of the microcontroller is an action elicited to one of the sevo arms telling it to move up or down by a pre-defined increment.  The increment of servo1 (closer to the body) is 4 degrees and the increment of servo2 (touches the ground) is 14 degrees.  The action that's selected is based on the $$\epsilon$$-greedy approach described above.

The $$Q$$ table has $$144$$ entries representing $$4$$ actions $$\times$$ $$6$$ servo1 states $$\times$$ $$6$$ servo2 states.  $$Q$$ was initialized to have all entries be $$10$$ so as to instill something like optimism in the agent for unseen states.  We somewhat arbitrarily set $$\gamma=0.75$$ and $$\alpha=0.1$$.  As the video above demonstrates, it works!

## Code
[Here](arduino-qlearning.txt).


{% include disqus.html %}
