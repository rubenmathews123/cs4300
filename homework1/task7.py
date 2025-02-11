# Task 7: Package Control

import requests
def fetch_data(url):
    """Fetches data from a given URL and returns the HTTP status code."""
    response = requests.get(url)
    return response.status_code