import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Take a peek at the data
    print(f'{df.head()}\n')
    print(f'{df.info()}\n')
    print(f'{df.describe()}\n')

    # Create scatter plot
    # Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    # Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.

    # https://docs.scipy.org/doc//scipy-1.10.1/reference/generated/scipy.stats.linregress.html
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_range = range(1880, 2051)
    plt.plot(x_range,
             res.slope * x_range + res.intercept,
             color='red')


    # Create second line of best fit
    # Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
    res = linregress(df[df['Year'] >= 2000]['Year'], df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])

    x_range = range(2000, 2051)
    plt.plot(x_range,
             res.slope * x_range + res.intercept,
             color='purple')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    plt.show()
    return plt.gca()