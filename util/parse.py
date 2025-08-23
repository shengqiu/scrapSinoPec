from bs4 import BeautifulSoup as bs


def get_index_list_from_content(html_content):
    """
    Extracts a list of indices from the HTML content of a webpage.
    Args:
        html_content (str): The HTML content of the webpage.
    Returns:
        list: A list of indices extracted from the content.
    """
    soup = bs(html_content, 'html.parser')
    index_list = []
    # Example logic to extract indices (modify as needed)
    for item in soup.find_all("a", href=True):
        index = item.get_text(strip=True)
        index_list.append(index)
    return index_list