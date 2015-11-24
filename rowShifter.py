# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256
from rowToCol import *

def rotate(rotate, n):
    return rotate[n:]+rotate[0:n]

def shiftRow(blockfile):
    block = blockfileColumn(blockfile)
    for i in range(4):
        block[i*4:i*4+4] = rotate(block[i*4:i*4+4], i)
    blockDone = blockfileColumn(block)
    return blockDone

def shiftRowInv(blockfile):
    for i in range(4):
        blockfile[i*4:i*4+4] = rotate(blockfile[i*4:i*4+4], -i)

    return blockfile