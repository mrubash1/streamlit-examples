'''
## Deep Reinforcement Learning with Streamlit: Playing Atari games with Deep Q-Networks

In this project, we will attempt to implement a reinforcement learning agent capable of playing Atari video games, by following the approach described in the DQN paper published in 2015 by DeepMind.

In reinforcement learning, research papers often describe an algorithm or a general approach that was able to achieve high performance on an experimental benchmark. In practice, it can be quite tricky to replicate the experimental results, and implementation details that seem subtle can cause large variation in performance. Often a handful of "tricks" are necessary to achieve stability or convergence. Because of this, it's a valuable exercise to start from scratch and to try to write your own high-performance implementation of common algorithms in RL.

[//]: # (
In this case, the DQN algorithm was actually first described in the 2013 paper

Playing Atari with Deep Reinforcement Learning,

It wasn't until a second paper was published in Nature in 2015, describing a handful of important implementation details

but it wasn't until a second more detailed paper was published in Nature in 2015, that the reinforcement community widely replicated the results

, but it wasn't until a more detailed paper was published in Nature in 2015 describing a handful of important implementation details that the reinforcement learning community adopted DQN widely.
)

The Atari games are a common benchmark in reinforcement learning, first proposed in the Arcade Learning Environment in 2013.

The DQN paper is one of the major breakthroughs in reinforcement learning - prior to this paper, artificial agents had only succeeded at learning more specific tasks, like a single Atari game. The DQN agent was able to achieve superhuman performance on a suite of 49 different video games, demonstrating a far more general ability to learn.

The important difference is that previous approaches relied on high-level features to be engineered by hand for the specific game. For instance, it's much easier for an agent to play the Space Invaders game if you hand-engineer a feature describing the position of the launcher, but that feature is of no use in another game.

The DQN agent learns directly from the raw pixels shown on the screen - in fact it only has access to the three pieces of information: the raw pixels, the score, and boolean that signals whether the game is over.

**Background:**

The DQN paper combined two existing pieces of

deep convolutional neural networks, which had already shown great success in supervised learning tasks like ImageNet, and q-learning, which had

Deep convolutional neural networks had already shown great success in supervised learning tasks like ImageNet.



(TODO: mention convergence proofs)

The DQN paper combined two existing pieces

: deep convolutional neural networks, which

The Q-learning algorithm (Watkins 1989)

, and the q-learning reinforcement learning algorithm.



The reason that previous agents

was because they relied on high-level features to be engineered by hand for the specific game, like the position



it combined deep neural networks with an existing algorithm called Q-learning

Prior to this paper, artificial agents had

been capable of mastering a single specific domain,

The breakthrough contribution from this paper

That a single agent was able to perform at a superhuman level across a variety of games.

Before this paper,

across a diverse range of games

solve the Atari video games by implementing the approach described in the 2015 DeepMind paper.


seemingly small implementation decisions can lead to significant changes in performance.

Note that the algorithm is receiving only the raw pixels as input observations


Note that the algorithm isn't receiving any "features" or structured information about the state of the game - it receives only the raw pixels

The algorithm receives only the raw pixels as input


Components:
- Whereas supervised learning has long had established benchmark datasets such as ImageNet, reinforcement learning.

 OpenAI gym is a standardized , so they serve as useful benchmarks.

 In addition, OpenAI gym gives us a spectrum from very easy environments to complicated environments,


 When reinforcement learning algorithms fail to learn, they generally fail silently with the only sign of trouble being that...they never solve the game.


Algorithms:
Q-table learning
Q-network learning with a single-layer CNN
Q-network learning with a multilayer CNN
Experience Replay
Target Network freezing
Image preprocessing


-
- OpenAI gym is

- OpenAI gym


st.write('In this project, we will replicate the results of the DQN paper ')


from DeepMind in 2015

human experts in many Atari video games.

st.write('Week 1 - explore OpenAI gym environments with a random agent')

- Random agent implementation
- observation, reward, done, info = env.step(action)



st.write('Week 2 - end-to-end pipeline using q-table learning')

Q-learning learns

It's sometimes called an action-value function or a Q-value function, where Q stands for "quality".

The value of taking a specific action from a specific state is equal to the immediate reward, plus a discounted future reward.

However, we aren't sure that we'll still be alive to receive a future reward, so we generally discount the future reward by a constant factor gamma.

Plot the score over number of frames seen.

The final q-table
(TODO: rearrange that table so it looks more like the 4x4 frozen lake grid.)

### Week 3 - Deep Q-Networks and Experience Replay

In an environment more complex than the 4x4 frozen lake game, it quickly becomes intractable to learn a value for every state-action pair. So we had better start estimating...and what's the only way we know how to estimate a function? With a deep neural network, of course!


The was actually published in 2013,


Experience Replay
Target Network freezing
Clipping Rewards
Skipping Frames
Preprocessing -> grayscale

- Q-learning with a single-layer CNN

st.write('?? Week 4 - productionization')


Future work:
Double Q learning
Prioritized Replay
Dueling DQN
'''
