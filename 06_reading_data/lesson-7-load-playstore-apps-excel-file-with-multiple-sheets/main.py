from re import S

import numpy as np
import pandas as pd

data_url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'

file = pd.ExcelFile(data_url)

playstore_df = file.parse(index_col=0) # Defaults to the first sheet
# playstore_df = file.parse('Google_playstore', index_col=0) # Explicitly specify the sheet name
content_id_df = file.parse('Content_ID', index_col='Content_ID')

# Alternative
# playstore_df = pd.read_excel(data_url,
#                              sheet_name='Google_playstore',index_col=0)

# content_id_df = pd.read_excel(data_url,
#                               sheet_name='Content_ID',
#                               index_col='Content_ID')

print(playstore_df.head())
print(content_id_df.head())
