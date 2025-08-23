import requests, sys
from bs4 import BeautifulSoup as bs

def download_webpage(url, filename="webpage.html"):
    """
    Downloads the HTML content of a webpage and saves it to a file.
    Args:
        url (str): The URL of the webpage to download.
        filename (str): The name of the file to save the content to.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        html_content = response.content
        with open(filename, "wb") as f:
            f.write(html_content)
        soup = bs(html_content, 'html.parser')
        print(f"Webpage downloaded successfully to {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading webpage: {e}")




if __name__ == "__main__":
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    for num in [num1, num2]:
        url_to_download = "https://ec.sinopec.com/f/supp/notice/bidNotice.do?id=" + str(num)
        download_webpage(url_to_download, "webpage/{}.html".format(num))