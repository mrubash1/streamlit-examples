import gym
import streamlit as st
from random_agent import random_agent


string1 = '''
# **Week 1: OpenAI Gym setup & Random Agent**
---
In Week 1 of this project, we will:
- Explore an OpenAI gym environment called FrozenLake
- Run a random agent on FrozenLake
- Render the FrozenLake animation in our Streamlit report

**Frozen Lake:**

Frozen Lake v0 is a super simple environment, represented by a 4x4 grid where your agent can move up/down/left/right on each step. One frame in the game usually looks like this:
'''

st.write(string1)

st.text('SFFF\nFHFH\nFFFH\nHFFG')

string2 = '''
The game works like this: Your agent always starts in the top left corner on the Start (S) space. You are safe on a Frozen (F) space, but you die if you fall into a Hole (H). If you make it to the Goal (G) space in the bottom right, you win!

The catch is...you're on a frozen lake! The ice is slippery and you won't always move in the direction you tell your agent to move. 🥶
'''

string2 = '''
FrozenLake is one of the text-based games in OpenAI Gym, which are designed to render as text in a terminal window. It normally uses ANSI escape characters to highlight your agent's current position red, but those don't cooperate that well with Streamlit. Instead we'll do something better...instead of letters we'll draw our frozen lake out of emoji!

We'll write a helper function named `render_text_game` so the Streamlit report will render FrozenLake using emojis for Start (🌀), Frozen (❄️), Hole (🕳), and Goal (🥅). (You can borrow this function for your project if it's helpful!)

In emoji, one frame of FrozenLake will look like this:
'''
st.write(string2)

st.text('🌀❄️❄️❄️\n❄️🕳❄️🕳\n❄️❄️❄️🕳\n🕳❄️❄️🥅')

string3 = '''
**Random Agent:**

It's always a good idea in a reinforcement learning project to start with a random agent. Sometimes a random agent does better than you expect, and it should be the baseline that you use to compare whether your agent is actually learning anything.

Let's get a random agent running on FrozenLake, and see an animated game render in Streamlit.

There are a few functions that we'll need from OpenAI gym:

- To restart the game: `env.reset()`
- To render a visual representation of the current game state: `env.render()`
- Specify which action to take, get back new game state: `observation, reward, done, info = env.step(action)`
- To get a list of possible actions: `env.action_space`
- To close the environment when you're done playing games: `env.close()`

Here is the code for the random agent:

    def random_agent(env, st_object, num_episodes):
        # an episode is one "game", or until your agent either wins or dies
        for episode in range(num_episodes):
            env.reset()
            j = 0
            done = False
            # iterate through "steps" in the game
            while j < 99:
                j += 1
                render_text_game(st_object, env)
                action = env.action_space.sample() # pick a random action
                observation, reward, done, info = env.step(action)
                if done:
                    break
                time.sleep(0.02)
        env.close()

Finally, let's see our random agent run on FrozenLake! Notice the agent (🏒) doesn't get to the goal very often...stay tuned for next week!

'''
st.write(string3)

# Make a Streamlit object where FrozenLake plays a random agent
st_object = st.empty()
env = gym.make('FrozenLake-v0')
random_agent(env, st_object, num_episodes = 5, sleep = 0.3)
