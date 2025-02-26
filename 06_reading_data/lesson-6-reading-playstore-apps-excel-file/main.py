import numpy as np
import pandas as pd

data_url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'
use_cols = ['App', 'Rating', 'Installs', 'Rating', 'Genres', 'Last_Updated']

playstore_df = pd.read_excel(data_url, usecols=use_cols, parse_dates=['Last_Updated'])
# print(playstore_df.head())

playstore_df_top_rated = playstore_df[playstore_df['Rating'] >= 4.5].sort_values('Rating').head(25)
print(playstore_df_top_rated)

