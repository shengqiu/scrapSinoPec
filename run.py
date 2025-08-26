from util.url import config, get_listing_from_index, get_webpage_index
from util.parse import get_index_list_from_content, get_winner_from_response, get_date_from_response, get_contact_from_response
import time

if __name__ == "__main__":
    page_no = config['payload']['pageNo']
    index_response = get_webpage_index(page_no)
    index_list = get_index_list_from_content(index_response)
    for index in index_list:
        print(index)
        listing_response = get_listing_from_index(index)
        winner = get_winner_from_response(listing_response)
        contact = get_contact_from_response(listing_response)
        dates = get_date_from_response(listing_response)
        print(dates)
        print(winner)
        print(contact)
        time.sleep(1)