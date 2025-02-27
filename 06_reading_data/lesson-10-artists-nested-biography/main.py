import json

import numpy as np
import pandas as pd
from pandas import json_normalize

# from pandas.io.json import json_normalize # This is the old import

# Read the `artists.json` into an `artists` DataFrame variable, using `json_normalize`. Keep the default index.
with open('files/artists.json') as file:
    json_dict = json.load(file)

artists = json_normalize(json_dict)

# Using the `bio` column, create a new `biography` DataFrame variable with the bio of each artist.
# When creatng the `biography` DataFrame also add the `name` column.
biography = json_normalize(json_dict,
                           record_path='bio',
                           meta=['name'])
print(f'{biography.head()=}')
