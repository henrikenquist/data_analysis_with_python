import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.figure import figaspect
from matplotlib.pylab import f

# 1
# Import the data from 'medical_examination.csv' 
df = pd.read_csv('medical_examination.csv')

# 2
# Add an overweight column to the data.
heights = df['height'] / 100
bmi = df['weight'] / (heights ** 2)
df['overweight'] = bmi.apply(lambda x: 1 if x > 25 else 0)
# print(f'{df["overweight"].head()=}')
# print(f'{df[df["overweight"] == 1].size=}')

# 3.
# Normalize data by making 0 always good and 1 always bad.
# If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
# df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else (1 if x > 1 else x))
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)
# print(f'{df["cholesterol"].head()=}')
# print(f'{df["gluc"].head()=}')

# 4
# Draw the Categorical Plot

def draw_cat_plot():
    # 5
    # Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.

    # Put 'cardio' first since it will be used in the melt function as id
    sorted_cols = ['cardio'] + sorted(['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = pd.DataFrame(df, columns=sorted_cols)  
    print(f'\nBefore melt:\n{df_cat.shape=}\n') 
    df_cat = df_cat.melt(id_vars=sorted_cols[0], value_vars=sorted_cols[1:])
    # print(f'{df_cat.head()=}')

    # 6
    # Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    
    # Seems to work without renaming 'variable' to 'feature'
    # df_cat.rename(columns={'variable': 'feature'}, inplace=True)

    # Group the data and count the occurrences
    df_counts = df_cat.groupby(['variable', 'value']).size().unstack().reset_index()
    # Display the count of each column
    print(f'{df_counts=}')

    # 7
    # Convert the data into long format and create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library import: sns.catplot().

    # In data manipulation, "long format" refers to the structure of the DataFrame, where each row contains a single observation for a particular variable and value, rather than having multiple observations spread across columns (which would be "wide format"). When you "melt" a DataFrame using pd.melt(), you're transforming it from wide format to long format, making it easier to perform certain types of analysis and visualization, especially when dealing with categorical data. This can be very useful for plotting, grouping, and summarizing data.

    print(f'\nAfter melt:\n{df_cat.shape=}')
    
    #8
    # Get the figure for the output and store it in the fig variable
    
    fig = sns.catplot(data=df_cat,
                      kind='count',
                      x='variable',
                      hue='value',
                      col='cardio',
                      sharey=True,
                      legend_out=True)
    fig.set_axis_labels('variable', 'total')

    # Similar plot using matplotlib
    # catplot_matplotlib(df_cat)

    # 9
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# 10
# Draw the Heat Map.
def draw_heat_map():
    # 11
    # Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data:
    # - diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
    # - height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
    # - height is more than the 97.5th percentile
    # - weight is less than the 2.5th percentile
    # - weight is more than the 97.5th percentile
    df_heat = df.copy()
    df_heat = df_heat[(df['ap_lo'] <= df['ap_hi']) &
                      (df['height'] >= df['height'].quantile(0.025)) &
                      (df['height'] <= df['height'].quantile(0.975)) &
                      (df['weight'] >= df['weight'].quantile(0.025)) &
                      (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)

    # 14
    fig, _ = plt.subplots()

    # 15
    sns.heatmap(corr,
                annot=True,
                fmt='.1f',
                linewidths=1,
                mask=mask,
                square=True,
                cmap='coolwarm',
                cbar_kws={'shrink': 0.5})
    plt.show()

    # 16
    fig.savefig('heatmap.png')
    return fig


def catplot_matplotlib(df_cat):
    """
    Just to show how much work seaborn.catplot() does for you
    """

    df_cat_0_sum = df_cat[df_cat['cardio'] == 0].groupby(['variable', 'value']).size().unstack().reset_index()
    print(f'{df_cat_0_sum.size=}')

    # Sum values for cardio = 1
    df_cat_1_sum = df_cat[df_cat['cardio'] == 1].groupby(['variable', 'value']).size().unstack().reset_index()
    print(f'{df_cat_0_sum.size=}')

    # Create subplots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6), sharey=True)

    # Bar plot for 'cardio' = 0
    df_cat_0_sum.plot(kind='bar', stacked=False, x='variable', ax=axes[0], color=['#1f77b4', '#ff7f0e'])
    axes[0].set_title('Cardio = 0')
    axes[0].set_ylabel('Count')

    # Bar plot for 'cardio' = 1
    df_cat_1_sum.plot(kind='bar', stacked=False, x='variable', ax=axes[1], color=['#1f77b4', '#ff7f0e'])
    axes[1].set_title('Cardio = 1')

    plt.tight_layout()
    plt.show()