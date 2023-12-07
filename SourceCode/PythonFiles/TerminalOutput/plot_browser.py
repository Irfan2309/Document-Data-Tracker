import matplotlib.pyplot as plt
from collections import Counter
from user_agents import parse
from helper_functions import create_histogram

# Function to return the top 10 browsers
def get_browser(data):     
    # List to store the browsers
    browsers = []

    # For every record in the data
    for record in data:
        # If the visitor_useragent is present
        if 'visitor_useragent' in record:
            # Parse the user agent
            user_agent = parse(record['visitor_useragent'])
            # Get the browser family
            browser_family = user_agent.browser.family
            # If the browser family is Chrome
            if 'Chrome' in browser_family:
                # Set the browser family to Chrome
                browser_family = 'Chrome'
            
            # If the browser family is Safari
            elif 'Safari' in browser_family:
                # Set the browser family to Safari
                browser_family = 'Safari'
            
            # If the browser family is Firefox
            elif 'Firefox' in browser_family:
                # Set the browser family to Firefox
                browser_family = 'Firefox'
            # If the browser family is Internet Explorer
            elif 'IE' in browser_family:
                # Set the browser family to Internet Explorer
                browser_family = 'Internet Explorer'
            # If the browser family is Android
            elif 'Android' in browser_family:
                # Set the browser family to Android
                browser_family = 'Android'
            # If the browser family is Opera
            elif 'Opera' in browser_family:
                # Set the browser family to Opera
                browser_family = 'Opera'
            else:
                # Set the browser family to Other
                browser_family = 'Other'
            # Append the browser family to the list
            browsers.append(browser_family.strip())
    # Counting the number of browsers
    browser_counts = Counter(browsers)
    # Sorting the browsers
    sorted_browser_counts = sorted(browser_counts.items(), key=lambda x: x[1], reverse=True)
    # Returning the top 10 browsers
    return dict(sorted_browser_counts[:10])

# Function to return all browsers
def get_all_browsers(data):
    # List to store the browsers
    browsers= []
    # For every record in the data
    visitor_useragent = []
    # For every record in the data
    for record in data:
        # If the visitor_useragent is present
        if 'visitor_useragent' in record:
            # Append the visitor_useragent to the list
            visitor_useragent.append(record['visitor_useragent'])
    # Return the visitor_useragent
    for user_agent in visitor_useragent:
        # Parse the user agent
        browsers.append(user_agent)
    # Return the browsers
    return browsers

