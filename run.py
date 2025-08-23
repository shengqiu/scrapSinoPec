import sys
from utl import download_webpage


if __name__ == "__main__":
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    for num in [num1, num2]:
        url_to_download = "https://ec.sinopec.com/f/supp/notice/bidNotice.do?id=" + str(num)
        download_webpage(url_to_download, "webpage/{}.html".format(num))