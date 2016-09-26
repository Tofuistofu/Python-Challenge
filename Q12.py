#!\usr\bin\env python

def main():
    with open('evil2.gfx', 'rb') as f:
        data = f.read()
        
    for i in range(5):
        with open('%d.jpg' % i, 'wb') as f:
            f.write(data[i::5])


    
if __name__ == '__main__':
    main()
