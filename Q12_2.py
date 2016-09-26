#!\usr\bin\env python

import requests

from requests.auth import HTTPBasicAuth

def main():
    res = requests.get('http://www.pythonchallenge.com/pc/return/evil4.jpg', auth = HTTPBasicAuth( 'huge', 'file'))
    with open('evil4.jpg', 'wb') as f:
        for chuck in res.iter_content(100000):
            f.write(chuck)
    with open('evil4.jpg', 'rb') as f:
        print f.read()


if __name__ == '__main__':
    main()
    
