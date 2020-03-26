#Model Free Reinforcement learning 

In Model-free , we just focus on figuring out the value functions directly from the interactions with the environment

All model free learning algorithms are gonna the learn value functions directly from the environment.


##There are few approaches for solving these kind of problems
1.Monte carlo approach
2.Temporal-Difference approach

##Monte carlo approach
Monte Carlo learning → it learns value functions directly from episodes of experience.
Monte Carlo learning → We only get the reward at the end of an episode

Episode = S1 A1 R1, S2 A2 R2, S3 A3 R3…… ST(Sequence of steps till the termination state)
we know the value function from the last story.

v(s) = E [Gt | St = s] and Gt = Rt+1+ γRt+2+…
we learn value functions from sample returns with the MDP

###what is a sample return??

it’s like an average of bunch of numbers
{1,2,3,4} → 10/4 → 2.5

so sample return could mean average of returns(rewards) from episodes.
Monte Carlo takes means of episodes. Period!

There are two different types in MC

1.First visit MC
in this, we average returns only for first time s is visited in an episode

2. Every visit MC
in this, we average returns for every time s is visited in an episode
let’s take a sample episode

S1 A1 R1, S2 A2 R3, S3 A3 R3, S1 A4 R4 →End

in first visit MC → we take the reward till R3
in every visit MC → we take the reward till the end of the episode

Usually the focus should be on first visit MC.


##Temporal-Difference approach

Temporal difference is the combination of Monte Carlo and Dynamic Programming
Just like Monte Carlo → TD methods learn directly from episodes of experience and model free.

Just like Dynamic Programming → TD methods boot strap , meaning it will not wait until the end of the episode to update the expected future reward estimation(V) , it will only wait until the next time step to update the value estimates.

for example
in MC
V(s) = E [Gt | St = s] and Gt = Rt+1+ γRt+2+…
in TD & DP

in TD, at every time step t they immediately form a TD target using the observed reward Rt+1 and the current estimate V(St+1).
The simplest TD method, known as TD(0)
V (St) ← V (St) + α (Rt+1 + γV (St+1) − V (St))