#!\usr\bin\env python

import requests
from bs4 import BeautifulSoup as BS
import pickle

def main():
    res = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
    soup = BS(res.text, 'html.parser')

    with open('Q5.txt', 'w+') as txt:
        txt.write(str(soup))
        
    with open('Q5.txt') as txt: #Putting both lines in the same with loop caused the .txt file to not fully write
        data = pickle.load(txt)
        
    for line in data:
        print ''.join([i*j for i, j in line])

if __name__ == '__main__':
    main()
