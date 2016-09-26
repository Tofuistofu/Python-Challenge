#!\usr\bin\env python

import string

def alpha_trans(text, shift):
    alphabet = string.ascii_lowercase
    x = string.maketrans(alphabet, alphabet[shift:] + alphabet[:shift])
    return text.translate(x)

if __name__ == '__main__':  
    text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. \
rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr \
ylb rfyr'q ufw rfgq rcvr gq qm jmle.sqgle qrpgle.kyicrpylq()\
gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    print alpha_trans(text,2)
    print 'next url keyword is: ' + alpha_trans('map',2)

