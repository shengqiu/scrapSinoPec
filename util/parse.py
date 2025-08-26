from bs4 import BeautifulSoup as bs
import json


def get_index_list_from_index_response(response):
    """
    Extracts a list of indices from the HTML content of a webpage.
    Args:
        html_content (str): The HTML content of the webpage.
    Returns:
        list: A list of indices extracted from the content.
    """
    data = json.loads(response.text)['result']['result']
    id_list = [x['id'] for x in data]
    return id_list

