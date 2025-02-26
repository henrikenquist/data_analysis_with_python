from unittest import skip

import numpy as np
import pandas as pd

col_names = ['Title', 'Air date', 'Production code', 'Season', 'Number in season',
             'Number in series', 'US viewers (million)', 'Views', 'IMDB rating']
             
df = pd.read_csv('files/simpsons-episodes.tsv',
                 sep='\t',
                 header=0,
                 names=col_names,
                 skiprows=4,
                 na_values=['no_val'],
                 parse_dates=['Air date'],
                 usecols=['Title', 'Air date', 'Production code', 'IMDB rating'],
                 index_col='Production code')

print(df.head())