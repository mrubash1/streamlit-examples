import numpy as np
from io import StringIO
import sys
import re


# Removes ANSI escape characters that are used to render text colors/highlighting/formatting
# in the terminal. ANSI is not supported by markdown so they show up as weird characters in streamlit.
def convert_frozen_lake_to_emoji(string):
    # regex finds the ANSI escape characters that are highlighting the agent's curent position
    split_by_current_position = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]').split(string)
    # substite the red highlighted character with the hockey stick emoji (the agent)
    split_by_current_position[1] = '🏒'
    # join the string back together
    agent_string = ''.join(split_by_current_position)
    # replace the remaining letters with the corresponding emoji
    emoji_string = agent_string.replace('S', '🌀').replace('F', '❄️').replace('H', '🕳').replace('G', '🥅')
    return emoji_string

def render_text_game(st_object, env):
    # env.render() in openai gym causes rendering as a side effect. in text-based games
    # it causes text output to stdout.
    # temporarily hijack stdout using StringIO so that we can save it to a variable
    # and then write that variable into streamlit
    normal_stdout = sys.stdout
    result = StringIO()
    sys.stdout = result
    env.render()
    sys.stdout = normal_stdout
    render_string = convert_frozen_lake_to_emoji(result.getvalue())
    st_object.text(render_string)
    return st_object

def render_atari_game(st_object, env, episode, width=400):
    img = env.render(mode='rgb_array')
    caption = "Episode " + str(episode)
    st_object.image(img, caption = caption, width = width)
    return st_object
