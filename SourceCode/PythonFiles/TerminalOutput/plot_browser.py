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
            # For more grouping, you can add conditions here to group by general browser type
            if 'Mobile' in browser_family or 'Tablet' in browser_family or 'iOS' in browser_family or 'WebView' in browser_family or 'WebKit' in browser_family:
                browser_family = browser_family.replace('Mobile', '').replace('Tablet', '').replace('iOS', '').replace('WebView', '').replace('WebKit', '')
            #trim whitespace
            browser_family = browser_family.strip()
            browsers.append(browser_family)
    return browsers

def get_all_browsers(data):
    browsers= []
    for record in data: 
        #get entire visitor_useragent
        user_agent = record['visitor_useragent']
        #plot all browsers
        browsers.append(user_agent)
    return browsers    
