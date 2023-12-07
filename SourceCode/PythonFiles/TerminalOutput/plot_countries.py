from helper_functions import create_histogram
import pycountry_convert as pc
from collections import Counter

# Function to plot the countries of the visitors of a document
def plot_countries(data, doc_id):
    # Filter the data to only include the visitors of the document
    filtered_data = []

    # For loop for every record in the data
    for entry in data:
        # If the record has the document id, add the country code to the filtered data
        if 'env_doc_id' in entry and entry['env_doc_id'] == doc_id:
            # Add the country code to the filtered data
            filtered_data.append(entry['visitor_country'])
    
    # Count the number of times each country code appears in the filtered data
    country_count = Counter(filtered_data)

    # Plot the histogram
    create_histogram(country_count, 'Histogram of Country Codes', 'Country Code')

# Function to get the continent names according to the country codes
def map_country_to_continent(country_code):
    try:
        # Get the continent code and name
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)

        # Return the continent name
        return continent_name
    except:
        return 'Unknown'

# Function to plot the continents of the visitors of a document
def plot_continents(data, doc_id):
    filtered_data = []
    # FOr record in data
    for record in data:
        # Tf the record has the document id, add the country code to the filtered data
        if 'env_doc_id' in record and record['env_doc_id'] == doc_id:
            filtered_data.append(record['visitor_country'])
    
    # Map the country codes to the continent names
    continent_data = [map_country_to_continent(country_code) for country_code in filtered_data]

    # Count the number of times each continent appears in the filtered data
    continent_count = Counter(continent_data)
    
    # Plot the histogram
    create_histogram(continent_count, 'Histogram of Continents', 'Continent', color='darkgreen')

