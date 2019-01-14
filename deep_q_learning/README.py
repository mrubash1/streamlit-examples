import streamlit as st
a = '''
## Deep Reinforcement Learning with Streamlit: Playing Atari games with Deep Q-Networks
### by Katie Everett
---

In this project, we will implement a reinforcement learning agent capable of playing Atari video games, by following the approach described in the DQN paper published in 2015 by DeepMind.

(TODO: link papers, mention both 2013 and 2015 versions)

In reinforcement learning, research papers often describe an algorithm or a general approach that was able to achieve high performance on an experimental benchmark. In practice, it can be quite tricky to replicate the experimental results, and implementation details that seem subtle can cause large variation in performance. Often a handful of "tricks" are necessary to achieve stability or convergence. Because of this, it's a valuable exercise to start from scratch and to try to write your own high-performance implementation of common algorithms in RL.

### **Background:**
###

**Why Atari?**

You can think of Atari games as being to reinforcement learning, what ImageNet is to supervised learning.

If you aren't familiar with Atari, you may still recognize the games when you see them as being "super old school video games". The Atari 2600 was one of the most popular home video game consoles ever produced, starting in 1977. In a bout of nostalgia, there were later emulators written that let you play the same games from a modern computer instead of on a console with a joystick. Then, in 2013 the [Arcade Learning Environment paper](https://jair.org/index.php/jair/article/view/10819) provided a standard interface for RL agents to play the Atari emulators by exposing (TODO ... corresponding to up to 18 actions you could take with a joystick).

The suite of Atari games are a good reinforcement learning benchmark because they provide a set of tasks that are challenging for humans, where a diverse set of strategies are necessary. Some of the Atari games, such as Pong, are fairly simple. Other games require balancing short-term and long-term rewards - for instance, in the game Seaquest, you collect points in the short-term by shooting fish, but also have to manage your submarine's oxygen supply in order to stay alive in the long-term. In the case of Montezuma's Revenge, the game requires the agent to explore large parts of the game state before collecting any rewards at all.

**What's OpenAI gym?**

OpenAI gym is an open-source Python library that includes the Atari games, as part of a suite of standardized tasks designed for training and evaluating reinforcement learning agents.

All of the OpenAI gym tasks have a consistent format: you can step forward in the environment by passing in a specific action, and getting back the current score, current state, and whether the game is over. You can also render the environment visually, which is extremely helpful for debugging and understanding what your agent is actually doing.

If this is confusing, it's because there's a fair bit of Atari-ception happening here: OpenAI gym is an open-source library containing a suite of reinforcement learning tasks, which includes the Arcade Learning Environment games, which is a standard interface to Atari 2600 emulators, which are simulating playing an old video game console on a computer.

**Why DQN?**

The DQN paper is one of the major breakthroughs in reinforcement learning - prior to this paper, artificial agents had only succeeded at learning more specific tasks, like a single Atari game. The DQN agent was able to achieve superhuman performance on a suite of 49 different video games (retraining the network on each different game but using the same architecture + algorithm + hyperparameters on every game), demonstrating a far more general ability to learn.

The important difference is that previous approaches relied on high-level features to be engineered by hand for the specific game. For instance, it's much easier for an agent to play the Space Invaders game if you hand-engineer a feature describing the position of the launcher, but that feature is of no use in another game.

The DQN agent learns directly from the raw pixels shown on the screen - in fact it only has access to the three pieces of information: the raw pixels, the score, and boolean that signals whether the game is over.

The DQN paper was a novel combination of two existing technologies: deep convolutional neural networks, which had already shown great success in supervised learning tasks such as ImageNet, and the Q-learning algorithm, initially proposed by Chris Watkins in 1989.

**Deep convolutional neural networks:**

(TODO: this section)

**Q-learning:**

(TODO: finish this section)

The Q-learning algorithm may seem obvious in hindsight, but

it framed the problem of reinforcement learning as incremental optimizing control of a Markov Decision Process.

Q-learning can, in principle, learn optimal control directly without modeling the transition probabilities or expected rewards of the MDP.

(This leads to an interesting comment on the reinforment learning in general: the dominant paradigm is to consider that agents inhabit an MDP and that "learning" then consists of finding an optimal policy.)

(TODO: mention convergence proofs)

** Implementation details:**

As mentioned above, the specific implementation details of a reinforcement learning algorithm are almost always essential to get right in order for the algorithm to learn.

As we'll see as we go through this project, our first implementation of DQN won't perform well at all, suffering from overfitting and unstable learning. In order to overcome these challenges, we'll implement four techniques outlined in the 2015 Nature paper: *experience replay*, *target network freezing*, *clipping rewards*, and *skipping frames*.

However, we'll start with a naive implementation to get an end-to-end pipeline up and running, and we'll add these techniques one by one and compare the performance after each improvement.

### **Installation:**
Assuming that:
- you're running on the Data Science AMI on AWS
- you already have Streamlit and Atom setup
- and you have checked this repo out from Github

All you should need to do is install the Python dependencies specific to this project with:
- `pip install -r requirements.txt`
---
## **Contents:**

#### Week 1: OpenAI Gym setup & Random Agent
Generate the week 1 report with `python week1.py`.

(TODO: link to shared week 1 report)

#### Week 2: End-to-end pipeline using Q-Table Learning
Generate the week 2 report with `python week2.py`.

(TODO: link to shared week 2 report)

#### Week 3 - Iterating on Deep Q-Networks
Generate the week 3 report with `python week3.py`.

(TODO: link to shared week 3 report)

#### Week 4 - Productionize with Docker and MPI
Coming soon!

---

### **Future work:**
If you're interested in extending this project, there are some variations of DQN that you could implement and compare the performance:
- Double Q learning
- Prioritized Replay
- Dueling DQN
- (TODO: link papers)
- (TODO: add descriptions)

---

**Citations**:

(TODO: cite the actual research papers)

In addition, the overall structure of this project was inspired by and draws from:
- The Berkeley Deep Reinforcement Learning Course [CS294-112](http://rail.eecs.berkeley.edu/deeprlcourse/) by Sergey Levine, Homework 3 in particular
- Deep RL tutorials by Adrien Ecoffet: https://becominghuman.ai/lets-build-an-atari-ai-part-0-intro-to-rl-9b2c5336e0ec
- The Google Dopamine project

---
'''

st.write(a)


# In this case, the DQN algorithm was actually first described in the 2013 paper
# Playing Atari with Deep Reinforcement Learning,
# It wasn't until a second paper was published in Nature in 2015, describing a handful of important implementation details
# but it wasn't until a second more detailed paper was published in Nature in 2015, that the reinforcement community widely replicated the results
# , but it wasn't until a more detailed paper was published in Nature in 2015 describing a handful of important implementation details that the reinforcement learning community adopted DQN widely.
