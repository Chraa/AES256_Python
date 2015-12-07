# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256
from rowToCol import *

def rotate(rotate, n):
    '''
    :param rotate: Roterar varden i 16 bytes blocket
    :param n: iterations vardet fran shiftRow/shiftRowInv
    :return: roterad rad (1,2,3,4)->(1,2,3,4) (5,6,7,8)->(6,7,8,5) (9,10,11,12)->(11,12,9,10) (13,14,15,16)->(16,13,14,15)
    '''
    return rotate[n:]+rotate[0:n]

def shiftRow(blockfile):
    '''
    :param blockfile:rowToCol metod sa att alla kolumner ar korrekt, shiftar med rotate, tar i*4 och hamtar 4 bytes fran det offsetet itereras igenom.
    :return:returnerar ett roterat block
    '''
    block = blockfileColumn(blockfile)
    for i in range(4):
        block[i*4:i*4+4] = rotate(block[i*4:i*4+4], i)
    blockDone = blockfileColumn(block)
    return blockDone

def shiftRowInv(blockfile):
    '''
    :param blockfile:samma som shiftRow fast inverterar tillbaka blocken.
    :return:ursprungsblocket returneras tillbaka.
    '''
    block = blockfileColumn(blockfile)
    for i in range(4):
        block[i*4:i*4+4] = rotate(block[i*4:i*4+4], -i)
    block = blockfileColumn(block)
    return block