#! /Users/ff/Projects/scrapSinoPec/.conda/bin/python 
from util.url import config, get_listing_from_index, get_webpage_index
from util.parse import get_index_list_from_content, parse_winner_response
from util.database import db_init, db_insert
import time


if __name__ == "__main__":
    db_init()
    page_no = config['payload']['pageNo']
    index_response = get_webpage_index(page_no)
    index_list = get_index_list_from_content(index_response)
    winner_list = []
    for index in index_list:
        listing_response = get_listing_from_index(index)
        winner_result = parse_winner_response(listing_response)
        winner_result['id'] = index
        sql_value = [(winner_result['id'], winner_result['winner'], winner_result['contact'], winner_result['date'])]
        db_insert(sql_value)
        time.sleep(1)
    