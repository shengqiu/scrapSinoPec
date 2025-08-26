#! /Users/ff/Projects/scrapSinoPec/.conda/bin/python 
from util.url import config, get_listing_from_index, get_webpage_index
from util.parse import get_index_list_from_content, parse_winner_response
from util.database import db_init, db_insert
import time


if __name__ == "__main__":
    db_init()
    page_max = config['payload']['pageNo']
    for page in range(11, int(page_max)+1):
        index_response = get_webpage_index(str(page))
        index_list = get_index_list_from_content(index_response)
        winner_list = []
        for index in index_list:
            listing_response = get_listing_from_index(index)
            winner_result = parse_winner_response(listing_response)
            winner_result['id'] = index
            winner_result['url'] = config['listing_url'] + str(index)
            sql_value = [(winner_result['id'], winner_result['winner'], winner_result['contact'], winner_result['url'], winner_result['date'])]
            db_insert(sql_value)
            print(sql_value)
            time.sleep(10)
    