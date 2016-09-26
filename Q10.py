#!\usr\bin\env python

import re


def look_and_say(start, iterations):
    iternum = 0
    x = start
    while iternum < iterations:
        x = ''.join([str(len(i+j)) + i
                     for i, j in re.findall(r'(\d)(\1*)', x)]) # i is the number, len(j) is amount i repeated afterwards
        iternum += 1
    return x


def main():
    print len(look_and_say('1', 30))


if __name__ == '__main__':
    main()
