from bs4 import BeautifulSoup as bs
import json


def get_index_list_from_content(response):
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


def parse_winner_response(response, biddingType):
    """
    Extracts a table from the HTML content of a webpage.
    Args:
        html_content (str): The HTML content of the webpage.
    Returns:
        bs4.element.Tag: The extracted table as a BeautifulSoup Tag object.
    """
    soup = bs(response.text, 'html.parser')
    if biddingType == 'closeType':
        winner_table = soup.find_all('table')[1]
        winner =  winner_table.get_text(strip=True).replace('物资名称成交供应商', '')
        contact_table = soup.find_all('table')[2]
        contact = contact_table.get_text(strip=True)
        date_elements = soup.find('div', class_='wrapTitle').find_all('b')
        data_elements_text = ' '.join([x.get_text(strip=True) for x in date_elements]).split('浏览量')[0].strip()
    elif biddingType == 'openType':
        winner_table = soup.find_all('table')[2]
        winner =  winner_table.get_text(strip=True).replace('物资名称成交供应商', '')
        contact_elements = soup.find_all('div')[4].find_all('p')
        contact = ' '.join([x.get_text(strip=True).replace('\xa0', '') for x in contact_elements[:5]])
        date_elements = soup.find('div', class_='wrapTitle').find_all('b')
        data_elements_text = ' '.join([x.get_text(strip=True) for x in date_elements]).split('浏览量')[0].strip()
    return {
        'winner': winner,
        'contact': contact,
        'date': data_elements_text
    }