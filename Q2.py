#!\usr\bin\env python

import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import re

def main():
    res = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
    soup = BeautifulSoup(res.text, 'html.parser')
    elem = soup.find_all(string=lambda text:isinstance(text,Comment))
    letters =  re.findall('[a-zA-Z]', elem[1])
    print ''.join(letters)

if __name__ == '__main__':
    main()
    

