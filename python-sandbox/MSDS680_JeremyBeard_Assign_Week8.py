import gym
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

print("Hello World!")

# first following: https://www.youtube.com/watch?v=yMk_XtIEzH8

import gym

env = gym.make("MountainCar-v0", render_mode='rgb_array')
env.reset()
plt.imshow(env.render())

print(env.observation_space.high)
print(env.observation_space.low)
print(env.action_space.n)

LEARNING_RATE = 0.1 #anything from 0 to 1, 0.1 is kinda low
DISCOUNT = 0.95 #kinda a 'weight', how important do we find future actions/reward over current actions/reward
EPISODES = 25000 #25000 not too long
DISCRETE_OS_SIZE = [20] * len(env.observation_space.high) #will/may/should change based on environment, WARNING
#this will create 20 distinct values between the ranges shown by .high and .low above
#helps to create 'buckets'

discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE
#discrete_os_win_size = np.asarray(discrete_os_win_size, dtype=object)

print(discrete_os_win_size) #shows the sizes of each chunk
#will show that position chunk size is 0.09, and velocity chunk size is 0.007

#now create Q table
#objective is to create massive Q table
#at top, action 0, action 1, action2
#rows are labeled Combination1, combination2, etc.
#cells show Q values
#is exploratory at first, searches for highest Q values

#q-table we will set as a 20x20x3 of every combination of environment observations, * 3 ACTIONS we can take. 
# to start we will have random values between -2 and 0 and it will get better over time
q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n])) # these values take some exploration/intuition
print(f'q_table size is {q_table.shape}')
#print(q_table)

def get_discrete_state(state):
    operation1 = state - env.observation_space.low
    discrete_state = operation1 / discrete_os_win_size
    return tuple(discrete_state.astype(np.int))

env_reset_state = env.reset()
env_reset_state = np.asarray(env_reset_state, dtype=object)
env_reset_state = env_reset_state[0]
discrete_state = get_discrete_state(env_reset_state)
print(f'Starting discrete state is {discrete_state}')

print('Passing discrete state into q_table')
print(q_table[discrete_state]) #shows starting q-values
print('Finding maximum initial q-value')
print(np.argmax(q_table[discrete_state]))

done = False

while not done:
    action = np.argmax(q_table[discrete_state])
    #new_state, reward, done, _ = env.step(action)
    obs, reward, terminated, truncated, info = env.step(action)
    #we need to bucket up these continuous states/obs into discrete
    new_discrete_state = get_discrete_state(obs)
    print('New State')
    print(new_discrete_state)
    #print(reward, obs) # reward will always be -1 until it finally reaches the flag and the reward becomes 0. then it back-propagates those actions
    env.render()
    if not done:
        print(q_table[new_discrete_state])
        max_future_q = np.max(q_table[new_discrete_state])
        print(f'max_future_q')
        print(max_future_q)
        current_q = q_table[discrete_state + (action, )]
        new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
        q_table[discrete_state+(action, )] = new_q
    elif new_state[0] >= env.goal_position:
        q_table[discrete_state+(action, )] = 0
        
    discrete_state = new_discrete_state
    
env.close()