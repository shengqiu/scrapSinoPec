import requests, yaml
from util.url import get_bidding_index
config = yaml.safe_load(open("config/sinoPec.yaml"))


def get_webpage_index(pageNo, biddingType, paramJson):
    """
    Downloads the HTML content of a webpage and saves it to a file.
    Args:
        url (str): The URL of the webpage to download.
        filename (str): The name of the file to save the content to.
    """
    url = "https://ec.sinopec.com/f/supp/bid/queryBidNotices.do?"
    payload = {
	    "pageNo": pageNo,
	    "type": biddingType,
	    "paramJson": paramJson
    }
    try:
        s = requests.Session()
        response = s.post(
            url,
            data=payload
        )
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        print(response.status_code)
        print(response.text)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error downloading webpage: {e}")


get_bidding_index("1", "openType")