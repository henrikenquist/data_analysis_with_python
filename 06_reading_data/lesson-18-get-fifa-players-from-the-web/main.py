import numpy as np
import pandas as pd
import requests

# Read and store in a `fifa_df` DataFrame the HTML table found in the `fifa_players.html` file that contains the top 30 FIFA players as of Oct. 30, 2019. The `fifa_players.html` file is a dump generated from this URL: https://www.fifaindex.com/players/top/fifa20_363/

# url = 'https://www.fifaindex.com/players/top/fifa20_363/'
# fifa_df = pd.read_table(url)
url_dump = 'files/fifa_players.html'
dfs = pd.read_html(url_dump, encoding='utf-8')
fifa_df = dfs[0]
print(f'\n{fifa_df.shape=}\n')
print(f'{fifa_df.head()=}\n')

# Remove the first two columns and the last one from the resulting `fifa_df` DataFrame, as they are `Unnamed` and filled with `NaN` objects.
# fifa_df = fifa_df.drop(columns=['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 7'])
fifa_df = fifa_df.iloc[:,2:-1]
print(f'{fifa_df.head()=}\n')


# Create a `most_hits_player` variable containing the player with the most amount of `Hits`.

most_hits_player = fifa_df.sort_values('Hits', ascending=False).head(1)
print(f'{most_hits_player=}\n')
