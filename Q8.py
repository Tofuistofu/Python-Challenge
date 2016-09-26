#!\usr\bin\env python

import bz2
import requests

from bs4 import BeautifulSoup, Comment


def get_comment(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    elem = soup.find_all(string = lambda text: isinstance(text,Comment))
    return elem

def main():
    comments = get_comment('http://www.pythonchallenge.com/pc/def/integrity.html')
    decomp = comments[0].split("'")[1:4:2]
    [un, pw] = [bz2.decompress(x.decode('string_escape'))
                for x in decomp]
    print 'un: ' + un
    print 'pw: ' + pw

    
if __name__ == '__main__':
    main()
