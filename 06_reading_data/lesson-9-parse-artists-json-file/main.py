import numpy as np
import pandas as pd

# Read the `artists.json` into an `artists` DataFrame variable, without using `json_normalize`.
artists = pd.read_json('files/artists.json')
print(f'{artists.head()=}\n')

# Remove the `bio` column.
artists.drop(columns='bio', inplace=True)

# Set the `name` column as index.
artists.set_index('name', inplace=True)

# Save it as `artists.csv` keeping the index.
artists.to_csv('files/artists.csv', index=True)
