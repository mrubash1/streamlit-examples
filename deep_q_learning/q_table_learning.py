import numpy as np
from render_gym import render_text_game, render_atari_game

def q_table_learning(env, st_object, lr=0.8, y=0.95, num_episodes=1000):
    # Initialize the Q table to zero for every (state, action) pair
    Q = np.zeros([env.observation_space.n, env.action_space.n])

    # Create lists to store the rewards and steps from each episode
    rList = [] #list of rewards (one value per episode)
    average_rList = [] #list of average rewards since the first episode
    for i in range(num_episodes):
        print(i)
        #Reset environment and get starting state
        s = env.reset()
        rAll = 0 # the total rewards we've accumulated in this episode
        d = False # whether this episode is done
        j = 0 # the current step

        # The Q-Table Learning algorithm
        while j < 99:
            j+=1
            # Pick the best action from the Q-table, except with noise
            a = np.argmax(Q[s,:] + np.random.randn(1,env.action_space.n)*(1./(i+1)))
            # Step forward in the environment - tell it the action, get back the new state and reward
            s1,r,done,_ = env.step(a)
            # Draw the current state of the environment in Streamlit
            st_object = render_text_game(st_object, env)
            # Update Q-Table based on results of this step
            Q[s,a] = Q[s,a] + lr*(r + y*np.max(Q[s1,:]) - Q[s,a])
            rAll += r
            s = s1
            if d == True:
                break
        rList.append(rAll)
        average_rList.append(sum(rList)/(i+1))
    return rList, average_rList, Q
