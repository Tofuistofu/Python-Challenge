#!\usr\bin\env python

import requests

from os import path
from io import BytesIO
from PIL import Image

def img_download(imgurl):
    res = requests.get(imgurl)
    imgFile = open(path.basename(imgurl), 'wb')
    for chunk in res.iter_content(100000):
        imgFile.write(chunk)
    imgFile.close()


def main():
    img_download('http://www.pythonchallenge.com/pc/def/oxygen.png')
    img = Image.open('oxygen.png')
    row = [img.getpixel((x, img.height / 2))
           for x in range(img.width)]
    row = row[::7]
    ords = [r for r,g,b,a in row
            if r == g == b]
    print ''.join(map(chr,ords))
    print ''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))

if __name__ == '__main__':
    main()
