import gym
import streamlit as st
import numpy as np

from q_table_learning import q_table_learning

string1 = '''
# **Week 2: Q-Table Learning**
---
In Week 2 of this project, we will:
- Implement the simplest version of Q-learning, where we learn Q*(s, a) in a table containing every (state, action) pair
- Build an end-to-end pipeline for Q-Table Learning where we plot its performance across episodes
- See which games Q-Table Learning can solve, and which games are too complex

**Q-Table Learning:**

In our 4x4 FrozenLake grid, there are only 16 states and 4 possible actions from each state. This means that we can solve the environment with the simplest version of Q-learning, where we explicitly learn Q\*(s,a) in a table containing every (state, action) pair. In a larger or more complex environment, we'll need to use a function to approximate Q\*(s,a), but Q-Table Learning will work for now.

Q-learning learns a "quality" function, sometimes called an action-value function, using the following principle: *The value of taking a specific action from a specific state is equal to the immediate reward, plus a discounted future reward.*

Why do we discount the future expected reward? We aren't sure that we'll still be alive to receive a future reward, so we generally discount it by a constant factor gamma.

In our implementation, we'll start by initializing the Q-table to all zeros. At each step, we take what we think is the best action from our current state (plus some noise). After each move, we iteratively update Q using the Bellman equation:

`Q[s,a] = Q[s,a] + lr*(r + y*np.max(Q[s1,:]) - Q[s,a])`

Then we'll plot the fraction of successful games, which we will see increase on FrozenLake as our agent plays more episodes!

'''
st.write(string1)

# Make a placeholder for the frozen lake environment to render
st_object = st.empty()

env = gym.make('FrozenLake-v0')

# Set learning parameters
lr = .8
y = .95
num_episodes = 1000

rList, average_rList, Q = q_table_learning(env, st_object, lr, y, num_episodes)

print("rList: ", rList)
print(average_rList)

st.write("Fraction of successful games since beginning")
st.line_chart(average_rList)

st.write("Final fraction of successful games:")
st.write(sum(rList)/num_episodes)

string2 = '''
We can look at the Q-table itself and see what the agent learned. This Q-table is shaped just like the FrozenLake grid, where each tuple shows the value of taking the (up, right, down, left) action from that state.

Note that in all the spaces with holes, and the goal space, the game is over as soon as the agent reaches that space. Therefore, the agent never updates the table with values other than the zeros it was initialized to.

If you visually "solve" the FrozenLake game and look at which safe paths you can take from the start to the goal, you'll notice that all the possible paths have to pass through the frozen space just to the right of the goal. And sure enough, the Q-table learned that the value of moving right from that space, is almost one.

'''

st.write(string2)
st.write("Final Q-Table Values:")
new_Q = np.reshape(Q, (4, 4, 4))
final_Q = np.zeros((4,4), dtype=object)
for i in range(4):
    for j in range(4):
        final_Q[i][j] = tuple(new_Q[i][j])
st.write(final_Q)

#TODO: plot on Breakout and show that the q-table learning agent doesn't learn
