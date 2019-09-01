import gym
import numpy as np

env = gym.make("MountainCar-v0")
env.reset()

while 100:
    action = 2
    new_state,reward,done,_ = env.step(action)
    print(new_state,reward)
    env.render()

env.close()