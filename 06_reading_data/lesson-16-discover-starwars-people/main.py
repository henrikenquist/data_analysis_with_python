import numpy as np
import pandas as pd
import requests

# SWAPI is a StarWars REST API with information about  `people`, `films`, `starships` and `planets` within the StarWars universe.

# Using the _requests_ library make a GET request to https://swapi.co/api/people/?format=json to get the `people` of StarWars universe.
# Outdated endpoint
# req = requests.get('https://swapi.co/api/people/?format=json')
url = 'https://swapi.dev/api/people/?format=json'
response = requests.get(url) # JSON response

# Store the JSON response into a `swapi_dict` dictionary variable.
swapi_dict = response.json()
print(f'\n\n{swapi_dict.keys()=}\n')
print(f'{swapi_dict["count"]} characters found in the StarWars universe.\n')

# Store the swapi_dict into a `starwars_people_df` DataFrame variable.
starwars_people_df = pd.DataFrame(swapi_dict['results'])
print(f'{starwars_people_df.head()=}\n')

# Filter blue-eyed characters on `blue_eyed_people_df`.
blue_eyed_people_df = starwars_people_df[starwars_people_df['eye_color'] == 'blue']
print(f'{blue_eyed_people_df["name"].values} have blue eyes.\n')
