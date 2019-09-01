import numpy as np
import gym
import random
import time
from IPython.display import clear_output

env = gym.make("FrozenLake-v0")

action_space_size = env.action_space.n
state_space_size = env.observation_space.n

q_table = np.zeros((state_space_size,action_space_size))
print(q_table)

num_episodes = 10000
max_steps_per_episode = 100

learning_rate = 0.1
discount_rate = 0.99

exploration_rate = 1
max_exploration = 1
min_exploration = 0.01
exploration_decay_rate = 0.001

reward_all_episode = []

for episode in range(num_episodes):
    state = env.reset()
    done = False
    rewards_current_episode = 0

    for step in range(max_steps_per_episode):
        exploration_rate_threshold = random.uniform(0,1)
        if exploration_rate_threshold > exploration_rate:
             action = np.argmax(q_table[state,:])
        else:
            action = env.action_space.sample()

        new_state,reward,done,info = env.step(action)

        q_table[state,action] = q_table[state,action]*(1-learning_rate) + learning_rate*(reward+discount_rate*np.max(q_table[new_state,:]))

        state = new_state
        rewards_current_episode += reward

        if done == True:
            break
    exploration_rate = min_exploration + (max_exploration-min_exploration)*np.exp(-exploration_decay_rate*episode)
    reward_all_episode.append(rewards_current_episode)

rewards_per_thosand_episode = np.split(np.array(reward_all_episode),num_episodes/1000)
count = 1000
print("average reward per thousand episodes")
for r in rewards_per_thosand_episode:
    print(count,":",str(sum(r/1000)))
    count += 1000

print("\n\n_____Q-table______\n")
print(q_table)