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
# Select `TYPE`, `MONTH`, `DAY` and `NEIGHBOURHOOD` from the `van_crimes` table, but only the crime observations from `Stanley Park` or `West End`. Store the information in a `van_crimes_df` DataFrame.
van_crimes_df = pd.read_sql_query(
    """
    SELECT TYPE, MONTH, DAY, NEIGHBOURHOOD
    FROM van_crimes
    WHERE NEIGHBOURHOOD IN ('Stanley Park', 'West End')
    """, conn
)
print(f'{van_crimes_df.head()}=')

# Store the count of crimes per `TYPE` in a `crime_types_count` variable.
crime_types_count = pd.read_sql_query(
    """
    SELECT TYPE, COUNT(TYPE) AS COUNT
    FROM van_crimes
    GROUP BY TYPE
    ORDER BY COUNT DESC
    """, conn
)
print(f'{crime_types_count.head()}=')

# Housekeeping
c.close()
conn.close()