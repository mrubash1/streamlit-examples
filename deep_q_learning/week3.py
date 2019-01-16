import streamlit as st

string = '''

# **Week 3: Iterating on Deep Q Networks**
---
In Week 3 of this project, we will:
- Define a neural network architecture in Keras
- Define a loss function and optimization algorithm
- Solve another OpenAI gym environment called CartPole
- Implement a replay buffer and experience replay

In an environment more complex than the 4x4 frozen lake game, it quickly becomes intractable to learn a value for every state-action pair. So we had better start estimating...and what's the only way we know how to estimate a function? With a deep neural network, of course!

**Q-network learning:**
(TODO: regression problem)

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

However, we're going to use Keras instead of defining our network in native Tensorflow. Keras is a high-level API that sits on top of Tensorflow, and in

It's a good exercise to build and train some simple networks in Tensorflow as well.

We define the model in Keras like this:
    from keras.models import Sequential
    from keras.layers import Dense

    model = Sequential()
    model.add(Dense(24, input_shape=(self.observation_space,), activation="relu"))
    model.add(Dense(24, activation="relu"))
    model.add(Dense(self.action_space, activation="linear"))
    # Use mean_squared_error as the loss function
    # Use stochastic gradient descent as the optimizer

**Optimization:**
(TODO: explain loss function and stochastic gradient descent)

In Keras, we define the loss function and the optimizer like this:

    from keras.optimizers import SGD

    model.compile(loss="mean_squared_error", optimizer=SGD(lr=LEARNING_RATE))

Experience Replay:



If you'd like to see the details of the preprocessing step for Atari games, check out this great article.



**Image preprocessing -> grayscale:**

**Target Network freezing:**

**Reward Clipping:**

**Skipping Frames:**





'''

st.write(string)

# TODO: chart with score and cartpole video

string2 = '''
In Week 4, we will scale up this model and train on a GPU to solve some Atari games! This can take a few hours or a few days to train. In the meantime, you can entertain yourself by watching a random agent try to play Breakout:
'''

st.write(string2)

#TODO: insert Breakout animation
