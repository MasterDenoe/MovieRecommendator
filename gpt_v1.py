import pandas as pd

# Load the ratings data
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])

# Load the movie titles data
movies = pd.read_csv('ml-100k/u.item', sep='|', encoding='latin-1', names=['item_id', 'title'], usecols=[0, 1])

# Merge the two dataframes
data = pd.merge(ratings, movies, on='item_id')

# Display the first few rows of the merged dataframe
print(data.head())






from surprise import Dataset
from surprise import Reader
from surprise import SVD
from surprise import accuracy
from surprise.model_selection import train_test_split

# Load the MovieLens-100k dataset
data = Dataset.load_builtin('ml-100k')

# Split the data into training and test sets
trainset, testset = train_test_split(data, test_size=0.25)

# Use the SVD algorithm for training
algo = SVD()

# Train the algorithm on the training set
algo.fit(trainset)

# Predict ratings for the test set
predictions = algo.test(testset)

# Compute and print RMSE (Root Mean Squared Error)
accuracy.rmse(predictions)





"""
import pandas as pd
from lenskit.datasets import ML100K
from lenskit import crossfold as xf
from lenskit import topn
from lenskit.algorithms.basic import Popular

# Load the MovieLens-100k dataset
ml = ML100K('path/to/ml-100k.zip') #  <------------------- Change directory location Master Denoe!
ratings = ml.ratings

# Display the first few rows of the ratings dataframe
print(ratings.head())

# Split the data into training and test sets
train, test = xf.sample_rows(ratings, 0.25)

# Use a simple popularity-based algorithm
algo = Popular()

# Train the algorithm on the training set
algo.fit(train)

# Recommend items for a user
recs = algo.recommend(1, 10)
print(recs)
"""
