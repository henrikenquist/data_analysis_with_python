import sqlite3

import numpy as np
import pandas as pd

# create a new connection to a db in memory
conn = sqlite3.connect(':memory:')

# create a cursor
c = conn.cursor()

# restore the given van_crime_2003.sql dump
c.executescript(open('files/van_crime_2003.sql', 'r').read())

# your code goes here
# Store all the crimes committed after 18:00 h in a `late_crimes` variable.
late_crimes = pd.read_sql_query("SELECT * FROM van_crimes WHERE hour > 17", conn)
print(f'{late_crimes.head()=}')

# Store the number of crimes committed on the month with most crimes in a `dangerous_month_crimes` variable.
dangerous_month_crimes = pd.read_sql_query("SELECT month, COUNT(*) AS crimes FROM van_crimes GROUP BY month ORDER BY crimes DESC LIMIT 1", conn)
print(f'{dangerous_month_crimes=}')

# Housekeeping
c.close()
conn.close()