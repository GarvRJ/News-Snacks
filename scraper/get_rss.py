import requests
from init_setup.creds import get_rss_url, key

# API endpoint URL

response = requests.post(get_rss_url, data={'key': key})


def get_links():
    print('Fetching identified sources...')
    rss_links = []
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the list data from the response
        list_data = response.json()
        for data in list_data:
            rss_links.append(data['rss_feed'])
        return rss_links
    elif response.status_code == 403:
        print("Request failed due to invalid key:", response.status_code)
        return []
    else:
        print("Request failed with status code:", response.status_code)
        return []
