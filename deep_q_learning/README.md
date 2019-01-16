### Playing Atari games with Deep Q-Networks
#### A Deep Reinforcement Learning Project in Streamlit
#### by Katie Everett

In this project, we will implement a reinforcement learning agent capable of playing Atari video games, by following the Deep Q-Network approach described in two papers published in [2013](https://arxiv.org/pdf/1312.5602.pdf) and [2015](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf) by Google DeepMind.

In reinforcement learning, research papers often describe an algorithm or a general approach that was able to achieve high performance on an experimental benchmark. In practice, it can be quite tricky to replicate the experimental results, and implementation details that seem subtle can cause large variation in performance. Often a handful of "tricks" are necessary to achieve stability or convergence. Because of this, it's a valuable exercise to start from scratch and to try to write your own high-performance implementation of common algorithms in RL.

### **Background:**

**Why Atari?**

You can think of Atari games as being to reinforcement learning, what ImageNet is to supervised learning.

If you aren't familiar with Atari, you may still recognize the games when you see them as being "super old school video games". The Atari 2600 was one of the most popular home video game consoles ever produced, starting in 1977. In a bout of nostalgia, there were later emulators written that let you play the same games from a modern computer instead of on a console with a joystick. Then in 2013, the [Arcade Learning Environment](https://jair.org/index.php/jair/article/view/10819) provided a standard interface for RL agents to play the Atari emulators by exposing consistent input formats corresponding to the 18 actions you could take with a joystick.

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

** Implementation details:**

As mentioned above, the specific implementation details of a reinforcement learning algorithm are almost always essential to get right in order for the algorithm to learn.

As we'll see as we go through this project, our first implementation of DQN won't perform well at all, suffering from overfitting and unstable learning. In order to overcome these challenges, we'll implement four techniques outlined in the 2015 paper: *frame skipping*, *experience replay*, *target network freezing*, and *reward clipping*.

However, we'll start with a naive implementation to get an end-to-end pipeline up and running, and we'll then add these techniques one by one and compare the performance after each improvement.

---
## **Contents:**

#### Week 1: OpenAI Gym setup & Random Agent
Generate the week 1 report with `python week1.py`.

#### Week 2: End-to-end pipeline using Q-Table Learning
Generate the week 2 report with `python week2.py`.

#### Week 3: Iterating on Deep Q-Networks
Generate the week 3 report with `python week3.py`.

#### Week 4: Productionize with Docker and MPI
Coming soon!

---

### **Future work:**
If you're interested in extending this project, there are a number of variations of DQN that you could explore. In particular, it would be interesting to implement [Double Q-Learning](https://arxiv.org/abs/1509.06461), [Prioritized Replay](https://arxiv.org/abs/1511.05952), or [Dueling DQN](https://arxiv.org/abs/1511.06581), and see how these variations impact the performance.

---

**References**:

Papers:
- [Bellemare et al., The Arcade Learning Environment: An evaluation platform for general agents. Journal of Artificial Intelligence Research, 2013.](https://jair.org/index.php/jair/article/view/11182)
- [Mnih et al. Playing atari with deep reinforcement learning. arXiv preprint arXiv:1312.5602, 2013.](https://arxiv.org/pdf/1312.5602.pdf)
- [Mnih et al., Human-level Control through Deep Reinforcement Learning. Nature, 2015.](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf)

In addition, the overall structure and various pieces of this project were inspired by or draw from:
- The Berkeley Deep Reinforcement Learning Course [CS294-112](http://rail.eecs.berkeley.edu/deeprlcourse/), Homework 3 in particular
- [Deep RL tutorials](https://becominghuman.ai/lets-build-an-atari-ai-part-0-intro-to-rl-9b2c5336e0ec) by Adrien Ecoffet
- The [Google Dopamine](https://github.com/google/dopamine) project
