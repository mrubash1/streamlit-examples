from q_table_learning import q_table_learning

string1 = '''
# **Week 2: Q-Table Learning**
---
In Week 2 of this project, we will:
- Implement the simplest version of Q-learning, where we learn Q*(s, a) in a table containing every (state, action) pair
- Watch the performance of our Q-learning implementation across episodes

**Q-Table Learning:**

In our 4x4 FrozenLake grid, there are only 16 states and 4 possible actions from each state. This means that we can solve the environment with the simplest version of Q-learning, where we explicitly learn Q*(s,a) in a table containing every (state, action) pair.

In a larger or more complex environment, we'll need to use a function to approximate Q*(s,a), but Q-Table Learning will work for now.

Q-learning learns

It's sometimes called an action-value function or a Q-value function, where Q stands for "quality".

The value of taking a specific action from a specific state is equal to the immediate reward, plus a discounted future reward.

However, we aren't sure that we'll still be alive to receive a future reward, so we generally discount the future reward by a constant factor gamma.

We'll start by initializing the Q-table to all zeros, and always pick what we think is the best move from our current state (plus some noise). After each move, we iteratively update Q using the Bellman equation:
Q[s,a] = Q[s,a] + lr*(r + y*np.max(Q[s1,:]) - Q[s,a])

'''
st.write(string1)


#st.title('Week 1: Q-Table Learning')


# Make a placeholder for the frozen lake environment to render
st_object = st.empty()

env = gym.make('FrozenLake-v0')

# Set learning parameters
lr = .8
y = .95
num_episodes = 10

rList, average_rList, Q = q_table_learning(env, st_object, lr, y, num_episodes)

st.write("Fraction of successful games since beginning")
st.line_chart(average_rList)

st.write("Final fraction of successful games:")
st.write(sum(rList)/num_episodes)

st.write("Final Q-Table Values")
st.write(Q)

#TODO: rearrange that table so it looks more like the 4x4 frozen lake grid.
