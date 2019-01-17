import streamlit as st
import gym
import time

from render_gym import render_atari_game

string = '''

# **Week 3: Iterating on Deep Q Networks**
---
In Week 3 of this project, we will:
- Define a neural network architecture in Keras
- Define a loss function and optimization algorithm
- Train the neural network to solve another OpenAI gym environment called CartPole
- Improve the performance by implementing experience replay

In an environment more complex than the 4x4 frozen lake game, it quickly becomes intractable to learn a value for every state-action pair. So we had better start estimating...and what's the only way we know how to estimate a function? With a deep neural network, of course!

**Architecture:**

The 2015 Nature paper describes the exact architecture of the convolutional neural network that was used to train Atari games:

| Layer | Input    | Filter size | Stride | Num filters | Activation | Output   |
|-------|----------|-------------|--------|-------------|------------|----------|
| conv1 | 84x84x4  | 8×8         | 4      | 32          | ReLU       | 20x20x32 |
| conv2 | 20x20x32 | 4×4         | 2      | 64          | ReLU       | 9x9x64   |
| conv3 | 9x9x64   | 3×3         | 1      | 64          | ReLU       | 7x7x64   |
| fc4   | 7x7x64   |             |        | 512         | ReLU       | 512      |
| fc5   | 512      |             |        | 18          | Linear     | 18       |

In tensorflow, we would define this architecture like this:

    import tensorflow as tf
    import tensorflow.contrib.layers as layers
    with tf.variable_scope("convnet"):
        # original architecture
        out = layers.convolution2d(out, num_outputs=32, kernel_size=8, stride=4, activation_fn=tf.nn.relu)
        out = layers.convolution2d(out, num_outputs=64, kernel_size=4, stride=2, activation_fn=tf.nn.relu)
        out = layers.convolution2d(out, num_outputs=64, kernel_size=3, stride=1, activation_fn=tf.nn.relu)
    out = layers.flatten(out)
    with tf.variable_scope("action_value"):
        out = layers.fully_connected(out, num_outputs=512,         activation_fn=tf.nn.relu)
        out = layers.fully_connected(out, num_outputs=num_actions, activation_fn=None)

However, we're going to use Keras instead of defining our network in native Tensorflow. Keras is a high-level API that sits on top of Tensorflow, and in this case it is a bit simpler to use Keras. It's a good exercise to build and train some simple networks in Tensorflow as well.

We're also going to use a smaller neural network to reduce the training time. We define the smaller model in Keras like this:
    from keras.models import Sequential
    from keras.layers import Dense

    model = Sequential()
    model.add(Dense(24, input_shape=(self.observation_space,), activation="relu"))
    model.add(Dense(24, activation="relu"))
    model.add(Dense(self.action_space, activation="linear"))
    # Use mean_squared_error as the loss function
    # Use stochastic gradient descent as the optimizer

**Optimization:**
We use the Mean Squared error as the loss function, and stochastic gradient descent as the optimizer, which we define in Keras like this:

    from keras.optimizers import SGD

    model.compile(loss="mean_squared_error", optimizer=SGD(lr=LEARNING_RATE))

It's interesting to try different optimizers and see how the performance changes - in particular, try the Adam optimizer and see how many episodes it takes to solve CartPole as compared to using SGD.

**Next steps:**
If we wanted to get closer to the implementation in the DQN paper, there are few more techniques to implement.

First, there are a couple of image preprocessing steps between the Atari game pixels and the input to the neural net. First the images get resized to 84x84x3, and then converted to grayscale. If you'd like to read more details about the preprocessing step for Atari games, check out this [great article](https://danieltakeshi.github.io/2016/11/25/frame-skipping-and-preprocessing-for-deep-q-networks-on-atari-2600-games/) by Daniel Seita.

Second, the DQN paper uses a trick called Target Network Freezing. Here's the basic idea: when we're updating the neural network after ever observation, our neural net is constantly chasing a moving target. In target network freezing, we periodically copy the network and freeze its state. When calculating the loss, we compare the current value to the output of the target network. Every few thousand steps, we update the target network. This trick has the same overall goal as experience replay: to increase the stability and encourage convergence. In practice the performance benefit from target network freezing is less significant than the benefit from experience replay.

Lastly, we can use a different loss function called the Huber loss. Huber loss is a piecewise function that uses Mean Squared Error for and Mean Absolute Error for large values.

In code, the Huber loss looks like this:

    def huber_loss(a, b):
        error = a - b
        if abs(error) > 1.0:
            return abs(error) - 1/2
        else:
            return error*error / 2



'''

st.write(string)

# TODO: chart with score and cartpole video

string2 = '''
This neural network can solve the CartPole game after about a hundred episodes, which looks like this:

'''

st.write(string2)

with open('cartpole_solved.mp4', 'rb') as f:
    video_bytes = f.read()
    st.video(video_bytes, format='video/mp4')

string3 = '''
In Week 4, we will scale up this model and train on a GPU to solve some Atari games! This can take a few hours or a few days to train. In the meantime, you can entertain yourself by watching a random agent try to play Breakout:
'''

st.write(string3)

st_object = st.empty()
env = gym.make('Breakout-v0')

for episode in range(10):
    env.reset()
    j = 0
    done = False
    while j < 99:
        j += 1
        render_atari_game(st_object, env, episode)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            break
        time.sleep(0.02)
env.close()
