from util.url import config, get_listing_from_index, get_webpage_index
from util.parse import get_index_list_from_index_response
import time

if __name__ == "__main__":
    page_no = config['payload']['pageNo']
    index_response = get_webpage_index(page_no)
    index_list = get_index_list_from_index_response(index_response)
    for index in index_list:
        print(index)
        print(get_listing_from_index(index))
        time.sleep(1)