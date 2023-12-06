from helper_functions import create_histogram
import pycountry_convert as pc
from collections import Counter

# Function to plot countries for each document
def plot_countries(doc_id, data):
    # Filter views for the specific document and check if 'env_doc_id' exists in the record
    filtered_data = [entry['visitor_country'] for entry in data if 'env_doc_id' in entry and entry['env_doc_id'] == doc_id]
    # Count occurrences of each country code
    country_count = Counter(filtered_data)
    # Create a histogram for country codes
    create_histogram(country_count, 'Histogram of Country Codes', 'Country Code')

# This function will use the pycountry_convert library to map country codes to continent names
def map_country_to_continent(country_code):
    try:
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        return continent_name
    except:
        # If the country code is not found, return 'Unknown'
        return 'Unknown'
    


def plot_continents(doc_id,data):
    # Filter views for the specific document and check if 'env_doc_id' exists in the record
    filtered_data = [entry['visitor_country'] for entry in data if 'env_doc_id' in entry and entry['env_doc_id'] == doc_id]
    # Map country codes to continents
    continent_data = [map_country_to_continent(country_code) for country_code in filtered_data]
    # Count occurrences of each continent
    continent_count = Counter(continent_data)
    # Create a histogram for continents
    create_histogram(continent_count, 'Histogram of Continents', 'Continent', color='darkgreen')

