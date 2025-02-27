import sqlite3

import numpy as np
import pandas as pd

# create a new connection to a db in memory
conn = sqlite3.connect(':memory:')

# create a cursor
c = conn.cursor()

# restore the given cryptos.sql dump
c.executescript(open('files/cryptos.sql', 'r').read())

# your code goes here
# The database we will use contains two tables `cryptocoins_cryptocurrency` and `cryptocoins_exchange`.
# Using the given sqlite3 connection and the `read_sql` method write a single query that:
#  - Join both tables and return the list of cryptocurrencies with its exchanges. You should use the column with the exchange ID on each table to perform the join.
#   - As both tables have a `name` column you should rename `cryptocoins_cryptocurrency.name` as `coin_name` and `cryptocoins_exchange.name` as `exchange`. Also select `symbol`, `price_usd` and `percent_change_7d` columns.
#   - Store the information in a `crypto_df` DataFrame.
crypto_df = pd.read_sql('''
                        SELECT
                        cryptocoins_cryptocurrency.name AS coin_name,
                        cryptocoins_cryptocurrency.symbol, cryptocoins_cryptocurrency.price_usd, cryptocoins_cryptocurrency.percent_change_7d,
                        cryptocoins_exchange.name AS exchange
                        FROM cryptocoins_cryptocurrency
                        JOIN cryptocoins_exchange
                        ON cryptocoins_cryptocurrency.exchange_id = cryptocoins_exchange.id
                        ''', conn)

# - Once you have the `crypto_df` DataFrame, create a new `weekly_change_df` with the `crypto_df` data sorted by `percent_change_7d` from highest to lowest.
weekly_change_df = crypto_df.sort_values(by='percent_change_7d', ascending=False)
print(f'{weekly_change_df.head(10)=}')

# Housekeeping
c.close()
conn.close()
