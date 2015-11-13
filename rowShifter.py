# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256

def rotate(word, n):
    return word[n:]+word[0:n]

def shiftRow(blockfile):
    for i in range(4):
        blockfile[i*4:i*4+4] = rotate(blockfile[i*4:i*4+4], i)
        #return block



def shiftRowInv(block):


    return block