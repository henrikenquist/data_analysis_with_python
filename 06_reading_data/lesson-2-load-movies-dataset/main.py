import numpy as np
import pandas as pd

column_names = ['color', 'director_name', 'num_critic_for_reviews', 'duration',
                'gross', 'movie_title', 'num_user_for_reviews',	'country',
                'cotent_rating', 'budget', 'title_year', 'imdb_score', 'genre']

df = pd.read_csv('files/movies.csv',
                  sep='|',
                  header=None, names=column_names, skiprows=3)

print(df.head())