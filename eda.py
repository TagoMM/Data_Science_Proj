import matplotlib.pyplot as plt
import seaborn as sns
import mplcursors
from matplotlib.ticker import FuncFormatter

def format_millions(x, pos):
    'The two args are the value and tick position'
    return f'${x * 1e-6:.1f}M'

def exploratory_data_analysis(data):
    """
    Plots exploratory scatter plots of price vs. bedrooms, acre lot, and house size.
    Each plot has a cursor with a price annotation that displays the price when hovered over a data point.

    Parameters
    ----------
    data : pandas.DataFrame
        The DataFrame containing the data to be plotted.

    Returns
    -------
    None
    """
    sns.set(style="whitegrid")

    # Price vs. Bedrooms (Scatter Plot)
    plt.figure(figsize=(10, 6))
    scatter = sns.scatterplot(x=data['bed'], y=data['price'], hue=data['price'], palette='viridis', s=100, alpha=0.6, legend=False)
    plt.title('Price vs. Bedrooms')
    plt.xlabel('Bedrooms (Units)')
    plt.ylabel('Price (Millions of $)')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))

    # Add cursor with price annotation
    cursor = mplcursors.cursor(scatter)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"Price: ${sel.target[1] * 1e-6:.2f}M"))

    plt.show()

    # Zoomed-in Price vs. Bedrooms (Scatter Plot)
    plt.figure(figsize=(10, 6))
    scatter = sns.scatterplot(x=data['bed'], y=data['price'], hue=data['price'], palette='viridis', s=100, alpha=0.6, legend=False)
    plt.title('Zoomed-in Price vs. Bedrooms')
    plt.xlabel('Bedrooms (Units)')
    plt.ylabel('Price (Millions of $)')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))
    plt.xlim(0, 5)  # Adjust these limits based on your data
    plt.ylim(0, 1e6)  # Adjust these limits based on your data

    # Add cursor with price annotation
    cursor = mplcursors.cursor(scatter)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"Price: ${sel.target[1] * 1e-6:.2f}M"))

    plt.show()

    # Price vs. Bathrooms (Scatter Plot)
    plt.figure(figsize=(10, 6))
    scatter = sns.scatterplot(x=data['bath'], y=data['price'], hue=data['price'], palette='viridis', s=100, alpha=0.6, legend=False)
    plt.title('Price vs. Bathrooms')
    plt.xlabel('Bathrooms (Units)')
    plt.ylabel('Price (Millions of $)')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))

    # Add cursor with price annotation
    cursor = mplcursors.cursor(scatter)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"Price: ${sel.target[1] * 1e-6:.2f}M"))

    plt.show()

    # Zoomed-in Price vs. Bathrooms (Scatter Plot)
    plt.figure(figsize=(10, 6))
    scatter = sns.scatterplot(x=data['bath'], y=data['price'], hue=data['price'], palette='viridis', s=100, alpha=0.6, legend=False)
    plt.title('Zoomed-in Price vs. Bathrooms')
    plt.xlabel('Bathrooms (Units)')
    plt.ylabel('Price (Millions of $)')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))
    plt.xlim(0, 5)  # Adjust these limits based on your data
    plt.ylim(0, 1e6)  # Adjust these limits based on your data

    # Add cursor with price annotation
    cursor = mplcursors.cursor(scatter)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"Price: ${sel.target[1] * 1e-6:.2f}M"))

    plt.show()


    # Price vs. Acre Lot (Scatter Plot)
    plt.figure(figsize=(10, 6))
    scatter = sns.scatterplot(x=data['acre_lot'], y=data['price'], hue=data['price'], palette='viridis', s=100, alpha=0.6, legend=False)
    plt.title('Price vs. Acre Lot')
    plt.xlabel('Acre Lot (Acres)')
    plt.ylabel('Price (Millions of $)')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))

    # Add cursor with price annotation
    cursor = mplcursors.cursor(scatter)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"Price: ${sel.target[1] * 1e-6:.2f}M"))

    plt.show()


    # Zoomed-in Price vs. Acre Lot (Scatter Plot)
    plt.figure(figsize=(10, 6))
    scatter = sns.scatterplot(x=data['acre_lot'], y=data['price'], hue=data['price'], palette='viridis', s=100, alpha=0.6, legend=False)
    plt.title('Zoomed-in Price vs. Acre Lot')
    plt.xlabel('Acre Lot (Acres)')
    plt.ylabel('Price (Millions of $)')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))
    plt.xlim(200, 500)  # Adjust these limits based on your data
    plt.ylim(0, 1e6)  # Adjust these limits based on your data

    # Add cursor with price annotation
    cursor = mplcursors.cursor(scatter)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"Price: ${sel.target[1] * 1e-6:.2f}M"))

    plt.show()

    # Price vs. House Size (Scatter Plot)
    plt.figure(figsize=(10, 6))
    scatter = sns.scatterplot(x=data['house_size'], y=data['price'], hue=data['price'], palette='viridis', s=100, alpha=0.6, legend=False)
    plt.title('Price vs. House Size')
    plt.xlabel('House Size (Square Feet)')
    plt.ylabel('Price (Millions of $)')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))

    # Add cursor with price annotation
    cursor = mplcursors.cursor(scatter)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"Price: ${sel.target[1] * 1e-6:.2f}M"))

    plt.show()


    # Zoomed-in Price vs. House Size (Scatter Plot)
    plt.figure(figsize=(10, 6))
    scatter = sns.scatterplot(x=data['house_size'], y=data['price'], hue=data['price'], palette='viridis', s=100, alpha=0.6, legend=False)
    plt.title('Zoomed-in Price vs. House Size')
    plt.xlabel('House Size (Square Feet)')
    plt.ylabel('Price (Millions of $)')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))
    plt.xlim(300, 600)  # Adjust these limits based on your data
    plt.ylim(0, 1e6)  # Adjust these limits based on your data

    # Add cursor with price annotation
    cursor = mplcursors.cursor(scatter)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"Price: ${sel.target[1] * 1e-6:.2f}M"))

    plt.show()

def correlation_scatter_plots(data):
    """
    Creates scatter plots with regression lines to visualize correlations between
    'price' and other features in the dataset.

    Parameters
    ----------
    data : pandas.DataFrame
        The DataFrame containing the data to be visualized.

    Returns
    -------
    None
    """
    sns.set(style="whitegrid")

    # Price vs. House Size (Scatter Plot with Regression Line)
    plt.figure(figsize=(10, 6))
    scatter = sns.regplot(x=data['house_size'], y=data['price'], scatter_kws={'s': 100, 'alpha': 0.6}, line_kws={'color': 'red'})
    plt.title('Price vs. House Size')
    plt.xlabel('House Size (Square Feet)')
    plt.ylabel('Price (Millions of $)')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))

    # Add cursor with price annotation
    cursor = mplcursors.cursor(scatter)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"Price: ${sel.target[1] * 1e-6:.2f}M"))

    plt.show()

    # Price vs. Acre Lot (Scatter Plot with Regression Line)
    plt.figure(figsize=(10, 6))
    scatter = sns.regplot(x=data['acre_lot'], y=data['price'], scatter_kws={'s': 100, 'alpha': 0.6}, line_kws={'color': 'red'})
    plt.title('Price vs. Acre Lot')
    plt.xlabel('Acre Lot (Acres)')
    plt.ylabel('Price (Millions of $)')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))

    # Add cursor with price annotation
    cursor = mplcursors.cursor(scatter)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"Price: ${sel.target[1] * 1e-6:.2f}M"))

    plt.show()

    # Price vs. Bathrooms (Scatter Plot with Regression Line)
    plt.figure(figsize=(10, 6))
    scatter = sns.regplot(x=data['bath'], y=data['price'], scatter_kws={'s': 100, 'alpha': 0.6}, line_kws={'color': 'red'})
    plt.title('Price vs. Bathrooms')
    plt.xlabel('Bathrooms (Units)')
    plt.ylabel('Price (Millions of $)')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))

    # Add cursor with price annotation
    cursor = mplcursors.cursor(scatter)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"Price: ${sel.target[1] * 1e-6:.2f}M"))

    plt.show()

def location_impact(data):
    """
    Plots bar charts of average prices by city, state, and zip code.

    Parameters
    ----------
    data : pandas.DataFrame
        The DataFrame containing the data to be plotted.

    Returns
    -------
    None
    """
    # Average Price by City
    plt.figure(figsize=(20, 10))
    city_prices = data.groupby('city')['price'].mean().reset_index()
    city_prices = city_prices.sample(n=20, random_state=42)  # Show 20 random cities
    bar = sns.barplot(x='city', y='price', data=city_prices, palette='viridis')
    plt.title('Average Price by 20 Random Cities')
    plt.xlabel('City')
    plt.ylabel('Average Price (Millions of $)')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))
    plt.xticks(rotation=90)
    plt.show()

    # Average Price by State
    plt.figure(figsize=(20, 10))
    state_prices = data.groupby('state')['price'].mean().reset_index()
    bar = sns.barplot(x='state', y='price', data=state_prices, palette='viridis')
    plt.title('Average Price by State')
    plt.xlabel('State')
    plt.ylabel('Average Price (Millions of $)')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))
    plt.xticks(rotation=90)
    plt.show()

    # Average Price by Zip Code
    plt.figure(figsize=(20, 10))
    zip_code_prices = data.groupby('zip_code')['price'].mean().reset_index()
    zip_code_prices = zip_code_prices.sample(n=20, random_state=42)  # Show 20 random zip codes
    bar = sns.barplot(x='zip_code', y='price', data=zip_code_prices, palette='viridis')
    plt.title('Average Price by 20 Random Zip Codes')
    plt.xlabel('Zip Code')
    plt.ylabel('Average Price (Millions of $)')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))
    plt.xticks(rotation=90)
    plt.show()

def housing_status_comparison(data):
    """
    Plots a pie chart of the distribution of prices across 'for sale' and 'sold' housing statuses.

    Parameters
    ----------
    data : pandas.DataFrame
        The DataFrame containing the data to be plotted.

    Returns
    -------
    None
    """
    plt.figure(figsize=(12, 8))
    # Filter data for 'for sale' and 'sold' statuses
    filtered_data = data[data['status'].isin(['for_sale', 'sold'])]
    status_prices = filtered_data.groupby('status')['price'].sum().reset_index()
    plt.pie(
        status_prices['price'],
        labels=status_prices['status'],
        autopct='%1.1f%%',
        colors=sns.color_palette('viridis', len(status_prices))
    )
    plt.title('Distribution of Prices across For Sale and Sold Housing Statuses')
    plt.show()

def historical_trends(data):
    """
    Plots a bar chart of average prices by previous sold year.

    Parameters
    ----------
    data : pandas.DataFrame
        The DataFrame containing the data to be plotted.

    Returns
    -------
    None
    """
    plt.figure(figsize=(12, 8))
    data['prev_sold_year'] = data['prev_sold_date'].dt.year
    prev_sold_prices = data.groupby('prev_sold_year')['price'].mean().reset_index()
    bar = sns.barplot(x='prev_sold_year', y='price', data=prev_sold_prices, palette='viridis')
    plt.title('Average Price by Previous Sold Year')
    plt.xlabel('Previous Sold Year')
    plt.ylabel('Average Price (Millions of $)')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))
    plt.xticks(rotation=90)
    plt.show()

def brokers_and_streets(data):
    """
    Plots two bar charts: one of the top 20 brokers by average price and one of
    average prices by 20 random streets.

    Parameters
    ----------
    data : pandas.DataFrame
        The DataFrame containing the data to be plotted.
    """
    # Top 20 Brokers by Average Price
    plt.figure(figsize=(12, 8))
    broker_prices = data.groupby('brokered_by')['price'].mean().reset_index()
    broker_prices = broker_prices.sort_values(by='price', ascending=False).head(20)  # Show top 20 brokers by average price
    bar = sns.barplot(x='brokered_by', y='price', data=broker_prices, palette='viridis')
    plt.title('Top 20 Brokers by Average Price')
    plt.xlabel('Broker')
    plt.ylabel('Average Price (Millions of $)')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))
    plt.xticks(rotation=90)
    plt.show()

    # Top 20 Streets by Average Price
    plt.figure(figsize=(12, 8))
    street_prices = data.groupby('street')['price'].mean().reset_index()
    street_prices = street_prices.sort_values(by='price', ascending=False).head(20)  # Show top 20 streets by average price
    bar = sns.barplot(x='street', y='price', data=street_prices, palette='viridis')
    plt.title('Top 20 Streets by Average Price')
    plt.xlabel('Street')
    plt.ylabel('Average Price (Millions of $)')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))
    plt.xticks(rotation=90)
    plt.show()