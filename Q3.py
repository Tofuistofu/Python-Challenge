#!\usr\bin\env python

from bs4 import BeautifulSoup, Comment
import requests
import re

def main():
    res = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
    soup = BeautifulSoup(res.text, 'html.parser')
    elem = soup.find_all(string=lambda text:isinstance(text,Comment))
    regex = re.compile(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]')
    groups = regex.findall(elem[0])
    letters = []
    for i in range(len(groups)):
        letters.append(groups[i][4])
    return ''.join(letters)
                   
                     
if __name__ == '__main__':
    print main()
