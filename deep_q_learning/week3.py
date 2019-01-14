string = '''
In an environment more complex than the 4x4 frozen lake game, it quickly becomes intractable to learn a value for every state-action pair. So we had better start estimating...and what's the only way we know how to estimate a function? With a deep neural network, of course!

**Q-network learning with a single-layer CNN:**

**Q-network learning with a multilayer CNN:**

Next we will try using the network architecure described in the 2015 Nature paper, which is as follows:

    Input: An 84x84x4 image produced by the preprocessing step.
    First hidden layer: 32 convolutional filters of 8x8 with stride 4 using RELU
    Second hidden layer: 64 convolutional filters of 4x4 with stride 2 using RELU
    Third hidden layer: 64 convolutional filters of 3x3 with stride 1 using RELU
    Fourth hidden layer: Fully connected with 512 rectifier units
    Output layer: Fully connected linear layer with a single output for each valid action
    (The number of valid actions is between 4 and 18 depending on the Atari game.)

The network architecture is illustrated in the paper like this:

(TODO: architecture image here)

In tensorflow, we define the architecture like this:

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

**Image preprocessing -> grayscale:**

**Experience Replay:**

**Target Network freezing:**

**Reward Clipping:**

**Skipping Frames:**
'''
