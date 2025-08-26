import sys
from util.url import download_webpage


if __name__ == "__main__":
    num = sys.argv[1]
    url_to_download = "https://ec.sinopec.com/f/supp/notice/bidNotice.do?id=" + str(num)
    download_webpage(url_to_download, "webpage/{}.html".format(num))