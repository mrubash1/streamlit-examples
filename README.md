# Streamlit Example Reports for Insight
Welcome! In this repo, we walk you through examples of two projects.
Each project is broken into four parts, which correspond roughly to the four
weeks of an Insight session.

1. 🎬 **[Movie Recommendation](https://github.com/streamlit/streamlit-examples/tree/master/movie_recs)**:
In this project, we build a movie recommendation system together (inspired by Amber Robert’s
[Project Orient](https://github.com/AstronomerAmber/Project-Orient)).
Here is a snapshot of what you’ll create:
[Week1](http://share.streamlit.io/0.23.0-2EMF1/index.html?id=F5rVwqPj43bt4bbdLnPua5)
| [Week2](http://share.streamlit.io/0.19.0-qYak/index.html?id=G9AGybo1qFHPSfCmSy2hjn)
| [Week3](http://share.streamlit.io/0.23.0-2EMF1/index.html?id=8hMSF5ZV3Wmbg5sA3UH3gW)
| [Week4](http://share.streamlit.io/0.23.0-2CETv/index.html?id=JhGfWhy7Rgt4SGeuPVcsDZ)

2. 🎮 **[Deep Q-Learning](https://github.com/streamlit/streamlit-examples/tree/master/deep_q_learning)**: In this project, we build reinforcement learning agents to tackle the environments of OpenAI Gym, including some classic Atari games! Here is a snapshot of what you’ll create: [README](http://share.streamlit.io/0.24.0-2GZ3y/index.html?id=5xtcG7c5FkZfPkBX4jSwLt) | [Week1](http://share.streamlit.io/0.24.0-2GZ3y/index.html?id=37RzRoMHeAzze5g5FNJzBW) | [Week2](http://share.streamlit.io/0.24.0-2GZ3y/index.html?id=Ux73f9D6PVBB2tiWjWnVfM) | [Week3](http://share.streamlit.io/0.24.0-2GZ3y/index.html?id=MigTt8LYvfXWoKEKkMSf6d) | Week4 (Coming soon!)

If you are more interested in a supervised learning project, we recommend you start with the Movie Recommendation project.
If you are interested in reinforcement learning, we recommend the Deep Q-Learning project.

Enjoy!

### **Installation:**

The installation steps to run these projects **locally** are the same for both projects. We assume you're using `conda` or `miniconda`.

Both projects have `environment.yml` files that define the project-specific dependencies.

1. Check out this git repo:
`git clone https://github.com/streamlit/streamlit-examples`

2. Navigate into the project directory:
  - For the movie recs project: `cd streamlit-examples/movie_recs`
  - For the deep q-learning project: `cd streamlit-examples/deep_q_learning`

3. Create a conda environment with all the libraries we need for the project. Conda will read the `environment.yml` file, which tells conda what to install.
  - `conda env create -f environment.yml`

4. Activate the conda environment that you just created
  - For the movie recs project: `conda activate movie_recs`
  - For the deep q-learning project: `conda activate deep_q_learning`

5. To open your project in Atom, run: `atom .`
