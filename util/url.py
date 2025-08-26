
import requests, time


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


def get_parent_webpage(url, payload):
    """
    Downloads the HTML content of a webpage and saves it to a file.
    Args:
        url (str): The URL of the webpage to download.
        filename (str): The name of the file to save the content to.
    """
    try:
        s = requests.Session()
        response = s.post(
            url, 
            data=payload,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
            }
        )
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        print(response.status_code)
        print(response.text)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error downloading webpage: {e}")