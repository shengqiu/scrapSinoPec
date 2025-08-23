
import requests


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
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Webpage downloaded successfully to {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading webpage: {e}")