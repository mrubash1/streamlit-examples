# The published output of this file currently lives here:
# http://share.streamlit.io/0.23.0-2CETv/index.html?id=JhGfWhy7Rgt4SGeuPVcsDZ

import keras
import math
import numpy as np
import pandas as pd
import streamlit as st
import os.path
import urllib.request
from scipy.sparse.linalg import svds
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from streamlit.Chart import Chart
from zipfile import ZipFile

interactive_mode = True

st.title('Run at scale')
st.write("""
In this part, we take the rating prediction (aka matrix-filling) part of the
Week 3 and run it on a
[larger MovieLens dataset](https://grouplens.org/datasets/movielens/20m/).
This dataset has 20 million ratings, which is **200X** larger than what we
worked with in Week 3!

Sadly, this larger dataset does not have demographic information about users -
so we don't get to play with our full recommendation system this time. But let's
watch our model train on this 20 million row dataset!
""")

if interactive_mode:
    st.info("""
    Uncomment the next section to learn what we must do to run our code
    on a GPU.
    """)

# # -----------------------------------------------------------------------------

# st.header("Running on a GPU")
# st.write("""
# In order to run our code on such a large dataset in a reasonable amount of time,
# we need to run it on a GPU. For this, we've created a conda environment named
# `movie_recs_env_gpu`. The only difference being that we use the `tensorflow-gpu`
# library instead of `tensorflow`.

# To switch conda environments, run the following commands on your AWS instance:
# ```
# source deactivate
# source activate movie_recs_env_gpu
# ```
# """)

# if interactive_mode:
#     st.info("""
#     Uncomment the next section to download the large dataset, unzip it, and read in
#     ratings.csv.
#     """)
# # # -----------------------------------------------------------------------------

# st.header("Downloading & Reading the Large Dataset")
# st.write("""
# To get started, we download the 20M MovieLens dataset,
# save it to the `/tmp/` directory,
# and then we read in ratings.csv from the unzipped directory.
# We do two things to save ourselves time.

# 1. We only download the zip if we haven't already (duh!)
# 2. We `@st.cache` the `read_ratings()` function.

# """)
# rating_cols = ['user_id', 'item_id', 'rating', 'timestamp']
# movielens_20m_url = "http://files.grouplens.org/datasets/movielens/ml-20m.zip"
# tmp_zip_path = "/tmp/ml-20m.zip"

# st.subheader("Downloading")
# with st.echo():
#     if not os.path.isfile(tmp_zip_path):
#         st.write("%s doesn't exist, so let's download it." % tmp_zip_path)
#         progress = st.info('No stats yet.')
#         progress.progress(0)

#         def show_progress(block_num, block_size, total_size):
#             downloaded = block_num * block_size
#             percent = math.ceil(downloaded / total_size * 100)
#             progress.progress(percent)

#         urllib.request.urlretrieve(movielens_20m_url, tmp_zip_path, show_progress)
#         st.write("Successfully downloaded to %s" % tmp_zip_path)
#     else:
#         st.write("%s exists, so we skip the download step." % tmp_zip_path)

#     @st.cache
#     def read_ratings(tmp_zip_path):
#         z = ZipFile(tmp_zip_path)
#         ratings = pd.read_csv(z.open('ml-20m/ratings.csv'), sep=',', names=rating_cols, skiprows=1, dtype={"user_id": int, "item_id": int, "rating": float}, encoding='latin-1')
#         ratings = ratings.drop(['timestamp'], axis=1)
#         return ratings

#     ratings_20m = read_ratings(tmp_zip_path)
#     n_users, n_movies = len(ratings_20m.user_id.unique()), len(ratings_20m.item_id.unique())

# if interactive_mode:
#     st.info("""
#     Uncomment the next section to find out the size of this dataset!
#     """)

# # # -----------------------------------------------------------------------------

# st.subheader("Size of the new dataset")
# st.write("**Number of ratings**: %d" % len(ratings_20m))
# st.write("**n_users:** %d" % n_users)
# st.write("**n_movies:** %d" % n_movies)

# if interactive_mode:
#     st.info("""
#     Uncomment the next section to run predict ratings over this *huge* dataset!
#     """)

# # # -----------------------------------------------------------------------------

# @st.cache
# def split(ratings):
#     return train_test_split(ratings, test_size=0.2)

# class MyCallback(keras.callbacks.Callback):
#     def __init__(self, x_test, num_epochs):
#         self._num_epochs = num_epochs
#         self._sample_tests = x_test[0:10]
#     def on_train_begin(self, logs=None):
#         st.header('Progress')
#         self._summary_chart = self._create_chart('area', 300)
#         st.header('Percentage Complete')
#         self._progress = st.empty()
#         self._progress.progress(0)
#         st.header('Current Epoch')
#         self._epoch_header = st.empty()
#         st.header('A Few Tests')
#         self._sample_test_results = st.empty()
#         self._sample_test_results.dataframe(self._sample_tests)
#     def on_epoch_begin(self, epoch, logs=None):
#         self._epoch = epoch
#         self._epoch_header.text(f'Epoch in progress: {epoch}')
#     def on_batch_end(self, batch, logs=None):
#         if batch % 1000 == 999:
#             rows = pd.DataFrame([[logs['mean_squared_error']]],
#                 columns=['mean_squared_error'])
#             self._summary_chart.add_rows(rows)
#             batch_percent = logs['batch'] * logs['size'] / self.params['samples']
#             percent = self._epoch / self._num_epochs + (batch_percent / self._num_epochs)
#             self._progress.progress(math.ceil(percent * 100))
#     def on_epoch_end(self, epoch, logs=None):
#         t = self._sample_tests
#         prediction = np.round(self.model.predict([t.user_id, t.item_id]),0)
#         self._sample_tests[f'epoch {epoch}'] = prediction
#         self._sample_test_results.dataframe(self._sample_tests)
#     def _create_chart(self, type='line', height=0):
#         empty_data = pd.DataFrame(columns=['mean_squared_error'])
#         epoch_chart = Chart(empty_data, f'{type}_chart', height=height)
#         epoch_chart.y_axis(type='number', orientation='right',
#             y_axis_id="mse_axis", allow_data_overflow="true")
#         epoch_chart.cartesian_grid(stroke_dasharray='3 3')
#         epoch_chart.legend()
#         getattr(epoch_chart, type)(type='monotone', data_key='mean_squared_error',
#             stroke='#82ca9d', fill='#82ca9d',
#             dot="false", y_axis_id='mse_axis')
#         return st.DeltaConnection.get_connection().get_delta_generator()._native_chart(epoch_chart)

# @st.cache
# def adam_predictions_with_monitoring(x_train, x_test):
#     n_latent_factors = 3
#     movie_input = keras.layers.Input(shape=[1],name='Item')
#     movie_embedding = keras.layers.Embedding(n_movies + 1, n_latent_factors, name='Movie-Embedding')(movie_input)
#     movie_vec = keras.layers.Flatten(name='FlattenMovies')(movie_embedding)
#     user_input = keras.layers.Input(shape=[1],name='User')
#     user_embedding = keras.layers.Embedding(n_users + 1, n_latent_factors,name='User-Embedding')(user_input)
#     user_vec = keras.layers.Flatten(name='FlattenUsers')(user_embedding)

#     prod = keras.layers.dot([movie_vec, user_vec], axes = 1)

#     model = keras.Model([user_input, movie_input], prod)
#     model.compile('adam', 'mean_squared_error', metrics=["accuracy", "mae", "mse"])

#     num_epochs = 10
#     model.fit([x_train.user_id, x_train.item_id], x_train.rating, validation_data=([x_test.user_id, x_test.item_id], x_test.rating),epochs=num_epochs, batch_size=256, verbose=0, callbacks=[MyCallback(x_test, num_epochs)])
#     return np.round(model.predict([x_test.user_id, x_test.item_id]),0), model

# st.header("Prediction on 20M Dataset")
# st.write("""
# In this section, we run *almost* the same code as in Week 3:
# * we split our dataset into a training dataset and a testing dataset, and
# * we run adam_predictions_with_monitoring().

# The only difference is that we run keras with a batch_size of 256 this time. The
# batch size determines the number of training examples we push through in a pass.
# Since we can process the examples in a batch in parallel, this is the way we make
# use of our GPU. There are many factors to consider when picking a batch size,
# including the trade-offs between changing the batch size versus the number of
# epochs, how these can effect the quality of your model, and how fast your model
# will converge. We encourage the reader to do their own research and experimentation
# when working with a different dataset.
# """)

# if interactive_mode:
#     st.info("Uncomment the next section to kick off this long-running computation.")
#     st.error("""
#     Hint: You'll actually hit an error in this first attempt. When you do:
#     read the error, comment out the section, and uncomment the next one.
#     """)

# # ------------------------------------------------------------------------------

# if interactive_mode:
#     with st.echo():
#         x_train, x_test = split(ratings_20m)
#         y_true = x_test.rating
#         adam_preds, model = adam_predictions_with_monitoring(x_train, x_test)

# # ------------------------------------------------------------------------------

# if interactive_mode:
#     st.write("""
#     Hmmm ... we seem to have hit an index out of bounds style bug.Perhaps you
#     noticed that the number 26745 is very similar to `n_movies` (26744).

#     This error is happening because there is some rating where the `item_id`
#     (aka movie_id) is greater than 26745. Keras expects our input to be nicely
#     formatted so that all the `item_id`'s are less than `n_movies`. (Same for
#     `user_id` as well).

#     The easiest option will be to set `n_movies` to be the max `item_id` we see,
#     but this might actually slow us down too much.

#     Instead, we make use of pandas functionality to map categorical data into
#     numbers. The `item_id` column is full of `int`'s - but for the purposes of
#     formatting the data correctly - we can treat it like a category.
#     """)

# with st.echo():
#     ratings_20m['item_id'] = ratings_20m['item_id'].astype('category').cat.codes
#     x_train, x_test = split(ratings_20m)
#     y_true = x_test.rating
#     adam_preds, model = adam_predictions_with_monitoring(x_train, x_test)

# st.write("Training complete. 🎉 ")

# if interactive_mode:
#     st.info("Uncomment the remainder of the report to see how we did.")

# # ------------------------------------------------------------------------------

# st.write('**Keras Adam Predictions**')
# st.write(adam_preds[1:1000])
# st.write('**MSE for Keras Adam Prediction**: %s' % mean_squared_error(y_true, adam_preds))

# st.write("Congratulations! You've now finished the final part of this project!")
# st.balloons()

# if not interactive_mode:
#     st.write("""
#     *Viewing this online? You can check out the underlying code
#     [here](https://github.com/streamlit/streamlit-examples/blob/master/movie_recs/src/week4_run_at_scale.py).*
#     """)
