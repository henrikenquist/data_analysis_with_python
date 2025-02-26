from re import S

import numpy as np
import pandas as pd

data_url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'


playstore_df = pd.read_excel(data_url,
                             sheet_name='Google_playstore',index_col=0)

content_id_df = pd.read_excel(data_url,
                              sheet_name='Content_ID',
                              index_col='Content_ID')

print(playstore_df.head())
print(content_id_df.head())
