#! /Users/ff/Projects/scrapSinoPec/.conda/bin/python 

import requests, yaml
from util.url import get_bidding_index
config = yaml.safe_load(open("config/sinoPec.yaml"))

if __name__ == "__main__":
    get_bidding_index("1", "openType")
