import requests, yaml
config = yaml.safe_load(open("config/sinoPec.yaml"))


def get_response(url):
    """
    Downloads the HTML content of a webpage and saves it to a file.
    Args:
        url (str): The URL of the webpage to download.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error downloading webpage: {e}")


def get_webpage_index(page_no=1):
    """
    Downloads the HTML content of a webpage and saves it to a file.
    Args:
        url (str): The URL of the webpage to download.
        filename (str): The name of the file to save the content to.
    """
    url = config['parent_url']
    index_type = config['payload']['type']
    headers = config['headers']
    payload = {
        "pageNo": page_no,
        "type":index_type 
    }
    try:
        s = requests.Session()
        response = s.post(
            url,
            data=payload,
            headers=headers
        )
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        print(response.status_code)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error downloading webpage: {e}")


def get_listing_from_index(num):
    listing_url = config['listing_url']
    # store_page_string = config['store_page_string']
    url_to_download = listing_url + str(num)
    return get_response(url_to_download)