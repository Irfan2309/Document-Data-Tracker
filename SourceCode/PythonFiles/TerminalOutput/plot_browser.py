import matplotlib.pyplot as plt
from collections import Counter
from user_agents import parse
from helper_functions import create_histogram

# Function to get the browser from the user agent
def get_browser(data):
     
    browsers = []
    for record in data:
        if 'visitor_useragent' in record:
            user_agent = parse(record['visitor_useragent'])
            # Just get the main browser family name without version or device
            browser_family = user_agent.browser.family
            if 'Chrome' in browser_family:
                browser_family = 'Chrome'
            elif 'Safari' in browser_family:
                browser_family = 'Safari'
            elif 'Firefox' in browser_family:
                browser_family = 'Firefox'
            elif 'IE' in browser_family:
                pass
            elif 'Android' in browser_family:
                pass
            elif 'Opera' in browser_family:
                pass
            else:
                browser_family = 'Other'

            browser_family = browser_family.strip()
            browsers.append(browser_family)
    browser_counts = Counter(browsers)
    sorted_browser_counts = sorted(browser_counts.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_browser_counts[:10])

def get_all_browsers(data):
    browsers= []
    visitor_useragent = []
    for record in data:
        if 'visitor_useragent' in record:
            visitor_useragent.append(record['visitor_useragent'])

    
    for user_agent in visitor_useragent:
        browsers.append(user_agent)

    return browsers

