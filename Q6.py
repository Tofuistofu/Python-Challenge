#!\usr\bin\env python

import zipfile
import re

def main():
    f = zipfile.ZipFile('channel.zip')
    num = '90052'
    comments = []
    
    while True:
        try:
            text = f.read(num + '.txt')
            comments.append(f.getinfo(num + '.txt').comment)
            print text
            num = text.split(' ')[-1]
        except:
            break
        
    print ''.join(comments)

if __name__ == '__main__':
    main()
