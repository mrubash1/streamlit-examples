import time
from render_gym import render_text_game


def random_agent(env, st_object, num_episodes=3, sleep=0.1):
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
            time.sleep(sleep)
    env.close()
