# Solving cartpole with DQN
# Adapted from https://github.com/gsurma/cartpole by Greg Surma

import random
import gym
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

GAMMA = 0.95
LEARNING_RATE = 0.001

MEMORY_SIZE = 1000000
BATCH_SIZE = 20

EXPLORATION_MAX = 1.0
EXPLORATION_MIN = 0.01
EXPLORATION_DECAY = 0.995

class DeepQNetwork():

    def __init__(self):
        self.exploration_rate = EXPLORATION_MAX
        self.env = gym.make('CartPole-v1')
        self.observation_space = self.env.observation_space.shape[0]
        self.action_space = self.env.action_space.n
        self.memory = deque(maxlen=MEMORY_SIZE)
        self.model = self.small_network()

    def small_network(self):
        model = Sequential()
        model.add(Dense(24, input_shape=(self.observation_space,), activation="relu"))
        model.add(Dense(24, activation="relu"))
        model.add(Dense(self.action_space, activation="linear"))
        # Use mean_squared_error as the loss function
        # Use stochastic gradient descent as the optimizer
        model.compile(loss="mean_squared_error", optimizer=SGD(lr=LEARNING_RATE))
        return model

    def epsilon_greedy_action(self, state):
        if np.random.rand() < self.exploration_rate:
            return random.randrange(self.action_space)
        q_values = self.model.predict(state)
        return np.argmax(q_values[0])

    def update_exploration_parameter(self):
        self.exploration_rate *= EXPLORATION_DECAY
        self.exploration_rate = max(EXPLORATION_MIN, self.exploration_rate)

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def experience_replay(self):
        if len(self.memory) < BATCH_SIZE:
            return
        batch = random.sample(self.memory, BATCH_SIZE)
        for state, action, reward, state_next, terminal in batch:
            q_update = reward
            if not terminal:
                q_update = (reward + GAMMA * np.amax(self.model.predict(state_next)[0]))
            q_values = self.model.predict(state)
            q_values[0][action] = q_update
            self.model.fit(state, q_values, verbose=0)
        self.update_exploration_parameter()

    def train(self):
        rList = []
        run = 0
        for run in range(50):
            state = self.env.reset()
            state = np.reshape(state, [1, self.observation_space])
            step = 0
            while True:
                step += 1
                action = self.epsilon_greedy_action(state)
                s1, r, done, _ = self.env.step(action)
                r = r if not done else -r
                s1 = np.reshape(s1, [1, self.observation_space])
                self.remember(state, action, r, s1, done)
                state = s1
                if done:
                    # The "score" in cartpole is how many steps you stayed alive
                    print("Run: ", run, ", exploration: ", self.exploration_rate, ", score: ", step)
                    rList.append((run, r, step))
                    break
                self.experience_replay()
        print(rList)


if __name__ == "__main__":
    DeepQNetwork().train()
