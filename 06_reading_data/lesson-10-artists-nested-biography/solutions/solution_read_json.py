import json

import numpy as np
import pandas as pd
from pandas import json_normalize

# from pandas.io.json import json_normalize # This is the old import

with open('../files/artists.json') as file:
    json_dict = json.load(file)

artists = json_normalize(json_dict)

biography = json_normalize(json_dict,
                           record_path='bio',
                           meta=['name'])

print(f'{biography.head()=}')