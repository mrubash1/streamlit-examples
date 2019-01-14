import numpy as np
from io import StringIO
import sys
import re


# Removes ANSI escape characters that are used to render text colors/highlighting/formatting
# in the terminal. ANSI is not supported by markdown so they show up as weird characters in streamlit.
# (copypasta from stackoverflow)
def filter_ansi_escapes(string, sub):
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    split_string = ansi_escape.split(string)
    #print(type(split_string))
    #print("test")
    #print("ansi_escape: ", str(ansi_escape))
    return ansi_escape.sub('🏒', string)

# def convert_frozen_lake_to_emoji(string):
#
#     return result

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
    render_string = filter_ansi_escapes(result.getvalue(), '')
    #render_string = filter_ansi_escapes(result.getvalue(), '**')
    #render_string = '\n\n'.join('`%s`' % line for line in render_string.split('\n'))
    st_object.text(render_string)
    return st_object

def render_atari_game(st_object, env, episode, width=400):
    img = env.render(mode='rgb_array')
    caption = "Episode " + str(episode)
    st_object.image(img, caption = caption, width = width)
    return st_object
