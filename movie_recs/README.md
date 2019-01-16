# Movie Recommendation with Streamlit

In this guide, we walk you through the lifecycle of an Insight ML project. You
can think of this guide as a "making-of" Amber Robert’s
[Project Orient](https://github.com/AstronomerAmber/Project-Orient).
Together, we will build a movie recommendation system using the
[MovieLens](https://grouplens.org/datasets/movielens/) dataset.

The project is broken into four parts, which correspond roughly to the weeks of
an Insight session.

1. **Exploring Data with Streamlit** - to better understand what we're working
with, we slice and dice and explore the MovieLens dataset.
2. **Recommendation System v0** - we build a naive recommendation system
end-to-end.
3. **Iterating on our recommendation system** - we experiment with two different
matrix factorization techniques to generate better recommendations.
4. **Running at scale** - we take our algorithm and scale it up! This time we
run it over a dataset that is 200X larger than in week 3!

## To Get Started

1. Go through the installation instructions [here](https://docs.google.com/presentation/d/1qo_MDz3iF0YRykuElF6I9WC4yAQIYzOA-GY16_NOuUM/edit?usp=sharing). Make sure you know
the IP address of your AWS instance (`AWS_INSTANCE_IP_ADDRESS`). 

2. SSH into your AWS instance: 

```shell
ssh ubuntu@[AWS_INSTANCE_IP_ADDRESS]
```

3. On your AWS instance: 

	i. Clone this repo: 

	```shell
	git clone https://github.com/streamlit/streamlit-examples
	```

	ii. Create the conda environment, which has all the libraries we need for this project (*this takes a few minutes*):  

	```shell
	cd streamlit-examples/movie_recs
	conda env create -f movie_recs_env.yml 
	``` 

	iii. Activate the conda environment that you just created: 
	```shell
	source activate movie_recs_env
	```

4. On your local machine, in a terminal: 

	i. Run this command to be able to remotely edit your streamlit-examples directory: 
	```shell
	sshfs streamlit-aws:streamlit-examples streamlit-examples
	```

	ii. Open this directory in Atom: 
	```shell 
	atom streamlit-examples
	```

5. Back on your AWS instance: 

	i. Change into the `src` directory and run week1_explore.py
	```shell
	cd src
	python week1_explore.py
	```

6. On your local machine, in Atom: 

	i. Open `week1_explore.py`

	ii. `ctrl+option+o` (on mac) or `ctrl+alt+o` (on ubuntu) to open the Streamlit side pane. 

	iii. Your screen should look like this at this point: 
	![alt text](static/week1-screenshot.png "Screenshot of week1_explore.py in Atom")

7. Next, follow the instructions in week1_explore.py. Enjoy! 
