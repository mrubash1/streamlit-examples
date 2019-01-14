import streamlit as st
import gym
import time

from render_gym import render_text_game, render_atari_game


st_object = st.empty()
#env = gym.make('Breakout-v0')
env = gym.make('FrozenLake-v0')
# env = gym.make('CartPole-v0')

st_object = st.empty()
env = gym.make('Breakout-v0')
#env = gym.make('FrozenLake-v0')
# env = gym.make('CartPole-v0')

for episode in range(10):
    env.reset()
    j = 0
    done = False
    while j < 99:
        j += 1
        render_atari_game(st_object, env, episode)
        #render_text_game(st_object, env)
        action = env.action_space.sample() # your agent here (this takes random actions)
        observation, reward, done, info = env.step(action)
        if done:
            break
        time.sleep(0.02)
env.close()
