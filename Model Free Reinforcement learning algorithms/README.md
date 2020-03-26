# Model Free Reinforcement learning 

In Model-free , we just focus on figuring out the value functions directly from the interactions with the environment
All model free learning algorithms are gonna the learn value functions directly from the environment.


## There are few approaches for solving these kind of problems

* Monte carlo approach
* Temporal-Difference approach

## Monte carlo approach

Monte Carlo learning → it learns value functions directly from episodes of experience.
Monte Carlo learning → We only get the reward at the end of an episode

Episode = S1 A1 R1, S2 A2 R2, S3 A3 R3…… ST(Sequence of steps till the termination state)
we know the value function from the last story.

v(s) = E [Gt | St = s] and Gt = Rt+1+ γRt+2+…
we learn value functions from sample returns with the MDP

### what is a sample return??

it’s like an average of bunch of numbers
{1,2,3,4} → 10/4 → 2.5

so sample return could mean average of returns(rewards) from episodes.
Monte Carlo takes means of episodes. Period!

There are two different types in MC

* First visit MC
in this, we average returns only for first time s is visited in an episode

* Every visit MC
in this, we average returns for every time s is visited in an episode
let’s take a sample episode

S1 A1 R1, S2 A2 R3, S3 A3 R3, S1 A4 R4 →End

in first visit MC → we take the reward till R3
in every visit MC → we take the reward till the end of the episode

Usually the focus should be on first visit MC.



## Temporal-Difference approach

Temporal difference is the combination of Monte Carlo and Dynamic Programming
Just like Monte Carlo → TD methods learn directly from episodes of experience and model free.

Just like Dynamic Programming → TD methods boot strap , meaning it will not wait until the end of the episode to update the expected future reward estimation(V) , it will only wait until the next time step to update the value estimates.

For example:
In MC
V(s) = E [Gt | St = s] and Gt = Rt+1+ γRt+2+…

In TD, at every time step t they immediately form a TD target using the observed reward Rt+1 and the current estimate V(St+1).
The simplest TD method, known as TD(0)
V (St) ← V (St) + α (Rt+1 + γV (St+1) − V (St))


Now let’s focus on TD- Control
Just like in Monte Carlo , we use policy iteration for TD Control
The first step is to learn an action-value function rather than a state-value function.
There are two algorithms in TD control

1. SARSA ( state-action-reward-state-action)

→The agent starts in S1, performs A1, and gets R1, and goes to S2

→Now the agent chooses another action A2 from S2

→Then updates the value of A1 performed in S1.

That gives the above equation.
S → current state, A → current action, R → current reward
S → next state, A → next action


2. Q-learning aka SARSAMAX

One of the most important breakthroughs in reinforcement learning was the development of an off-policy TD control algorithm known as Q-learning
Q-learning estimates a state-action value function for a target policy that deterministically selects the action of highest value


3. Expected Sarsa

Expected Sarsa exploits knowledge about stochasticity in the behavior policy to perform updates with lower variance. Doing so allows for higher learning rates and thus faster learning. In deterministic environments, Expected Sarsas updates have zero variance, enabling a learning rate of 1. We prove that Expected Sarsa converges under the same conditions as Sarsa and formulate specific hypotheses about when Expected Sarsa will outperform Sarsa and Q-learning. Experiments in multiple domains confirm these hypotheses and demonstrate that Expected Sarsa has significant advantages over these more commonly used methods.

* SARSA
→ On policy learning method , means it uses the same policy to choose the next action A

* Q-Learning
→ Off policy learning method , means, it uses the target policy (greedy) to choose the best next action, A while following the behavior policy (epsilon-greedy)

![image](https://github.com/aayushrai/Reinforcement_learning/blob/master/Model%20Free%20Reinforcement%20learning%20algorithms/image/Capture.JPG)



## Difference b/w MC and TD

Monte-Carlo
→ it only works for episodic tasks
→ it can only learn from complete sequences
→it has to wait until the end of the episode to get the reward

TD
→ it only for both episodic and continuous tasks
→it can learn from incomplete sequences
→ it will only wait until the next time step to update the value estimates.

Summary
→ We use model free algorithms when Transition probability P (dynamics of the system)is not given in MDP.
→ Monte Carlo takes the means of episodes to calculate the V and Q values for both prediction and control tasks.
→ TD combines the features of both DP and MC by learning through interacting with the environment with bootstrapping.
→ We use epsilon greedy policy to avoid the exploration problem in the env.
→ Sarsa updates the Q value by choosing the current action and next action using the same policy, making it an on policy method.
→ Q-learning updates Q values by acting greedily on the environment while following another policy, making it an off policy method.

## Reference links

https://medium.com/deep-math-machine-learning-ai/ch-12-1-model-free-reinforcement-learning-algorithms-monte-carlo-sarsa-q-learning-65267cb8d1b4
