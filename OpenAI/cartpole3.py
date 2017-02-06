import gym
import random
import numpy as np
import time


"""
    The observation of the cartpole yields the the location/position
    of the cart and the angle of the pole attached to the cart

    the available action space is {0,1}

    direct quote:
    "A simple way to map these observations to an action choice is a linear
    combination. we define a vector of weights, each weight corresponds to one
    of the observations.Start off by initializing them randomly between [-1,1]

    >> parameters = np.random.rand(4) * 2 - 1
"""

"""
    matrix multiplier allows the alternation of actions based on the state
    and the location of the cart using the data from each step(action)
"""

def episode():
    env = gym.make('CartPole-v0')
    observation = env.reset()
    parameters = np.random.rand(4) * 2 - 1                         #generates 4 random numbers, in the range of 2, minus 1: range {-1,1}
    actions = 0;
    score = 0
    rounds = 0
    for ep in range (40):                                             #plays 20 rounds
        rounds += 1                                                   #increment rounds
        observation = env.reset()                                     #reset the game
        actions = 0                                                   #reset the action count
        totalreward = 0                                               #reset rewards
        for _ in xrange(100000):
            env.render()
            action = 0 if np.matmul(observation,parameters) < 0 else 1 #{0 or 1} by multiplying the matrix
            actions += 1                                               #increment actions
            observation, reward, done, info = env.step(action)         #perform action                                        #weight
                                                                       #rewards are used to feed an agents compulsion loop
            time.sleep(0.04)                                           #slow down
            print observation                                          #print obs data

            if done:                                                   #if done == true
                print("game ended after ", actions, " actions")        #show action count
                break
        print("round: ")
        print(rounds)

episode()
"""
    https://www.youtube.com/watch?v=IMwh7JTcEsg
    https://www.youtube.com/watch?v=IK7l4ZLm55I

    author of the video details why its important to have a reward system to
    incentivize an intelligent agent
"""
