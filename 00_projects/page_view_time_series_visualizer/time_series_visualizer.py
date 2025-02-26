import calendar

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.pylab import f
from pandas.plotting import register_matplotlib_converters

# Used for converting date strings to datetime objects (months, years)
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',
                 parse_dates=['date'],
                 index_col='date')

# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

print(f'{df.head()=}')


def draw_line_plot():
    """
    Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png".
    
    The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019.
    
    The label on the x axis should be Date and the label on the y axis should be Page Views.
    """
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))

    ax.plot(df.index, df['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    """
    Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png".
    
    It should show average daily page views for each month grouped by year.
    
    The legend should show month labels and have a title of Months.
    
    On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.
    """
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # Create new columns: year and month
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    print(f'{df_bar.head()=}')

    # Group by year and month and calculate the mean
    df_monthly = df_bar.groupby(['year', 'month']).mean().unstack()
    print(f'{df_monthly.head()=}')

    # Create the figure and axes
    fig, ax = plt.subplots()

    df_monthly.plot(kind='bar', ax=ax, figsize=(12, 8), width=0.5)

    # Set labels and title
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    # ax.set_title('Monthly Average Page Views by Year')
    
    # Customize the x-axis labels to include months
    plt.xticks(range(len(df_monthly.index)), df_monthly.index, rotation=90)
    
    # Update the legend with month names
    month_labels = [calendar.month_name[i] for i in range(1, 13)]
    plt.legend(title='Month', labels=month_labels, loc='upper left')

    plt.tight_layout()
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    """
    Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png".
    
    These box plots should show how the values are distributed within a given year or month and how it compares over time.
    
    The title of the first chart should be Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality).
    
    Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data.
    """
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    sns.boxplot(data=df_box, ax=axes[0], x='year', y='value', palette='pastel')
    sns.boxplot(data=df_box, ax=axes[1], x='month', y='value', palette='pastel', order=calendar.month_abbr[1:])

    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[0].set_xlabel('Year')
    axes[1].set_xlabel('Month')
    axes[0].set_ylabel('Page Views')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
