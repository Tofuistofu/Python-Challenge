#!\usr\bin\env python

from PIL import Image
from Q7 import img_download

def main():
    img_download('https://the-python-challenge-solutions.hackingnote.com/images/cave.jpg')

    img = Image.open('cave.jpg')
    (w, h) = img.size

    even = Image.new('RGB', (w // 2, h // 2))
    odd = Image.new('RGB', (w // 2, h // 2))

    for i in range(w):
        for j in range(h):
            p = img.getpixel((i,j))
            if (i+j) % 2 == 1:
                odd.putpixel((i // 2, j // 2), p)
            else:
                even.putpixel((i // 2, j // 2), p)

    even.save('even.jpg')
    odd.save('odd.jpg')

if __name__ == '__main__':
    main()
