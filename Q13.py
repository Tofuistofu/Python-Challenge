#!\usr\bin\env python

import xmlrpc.client

def main():
    conn = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
    print conn.phone('Bert')
    

if __name__ == '__main__':
    main()
