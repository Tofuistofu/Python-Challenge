#!\usr\bin\env python

import re
import requests

from bs4 import BeautifulSoup, Comment
from PIL import Image, ImageDraw
from requests.auth import HTTPBasicAuth

def get_comment_login(url, login):
    # Get comment data from a protected site
    res = requests.get(url, auth = HTTPBasicAuth(login[0], login[1]))
    soup = BeautifulSoup(res.text, 'html.parser')
    elem = soup.find_all(string = lambda text: isinstance(text, Comment))
    return elem

def main():
    comment = get_comment_login('http://www.pythonchallenge.com/pc/return/good.html',
                                ['huge', 'file'])[1]
    comment = comment.split(':\n')[1:3]
    numlist = [re.findall('\d+', x)
               for x in comment]
    [first, second] = [map(int, numlist[x])
                       for x in range(len(numlist))]

    img = Image.new('RGB', (max(first + second), max(first + second)))
    draw = ImageDraw.Draw(img)
    draw.polygon(first, fill = 'white')
    draw.polygon(second, fill = 'white')
    img.show()
    
    
if __name__ == '__main__':
    main()
