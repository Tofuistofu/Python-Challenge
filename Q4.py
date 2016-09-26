#!\usr\bin\env python

from bs4 import BeautifulSoup
import requests
import sys

def nextnothing(nothing):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % nothing
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    newnothing = str(soup).split(' ')[-1]
    return str(newnothing)

def iter_print(function, args, iterations):
    for i in range(iterations):
        print function(args), i
        args = function(args)

if __name__ == '__main__':
    iter_print(nextnothing, '12345', 400)
