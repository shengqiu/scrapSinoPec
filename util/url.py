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
        print(response.status_code)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error downloading webpage: {e}")


def get_bidding_index(pageNo="1", biddingType="openType"):
    """
    Downloads the HTML content of a webpage and saves it to a file.
    Args:
        pageNo (str): max page number, need to be specified
        bidding (str): bidding type can be openType or closeType
    """
    url = config[biddingType]['parent_url']
    payload = {
        "pageNo": pageNo,
        "type": config[biddingType]['typeId'],
        "paramJson": "{}"
    }
    try:
        s = requests.Session()
        response = s.post(
            url,
            data=payload
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