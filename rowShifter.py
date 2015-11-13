# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256

def rotate(rotate, n):
    return rotate[n:]+rotate[0:n]

def shiftRow(blockfile):
    for i in range(4):
        blockfile[i*4:i*4+4] = rotate(blockfile[i*4:i*4+4], i)
    return blockfile

def shiftRowInv(blockfile):
    for i in range(4):
        blockfile[i*4:i*4+4] = rotate(blockfile[i*4:i*4+4], -i)

    return blockfile