# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256


def getBlock(filename):
    blockfile = open(filename, 'r')                                                                                     #blockfile opens file specified in main.py
    hexadecimalblock = blockfile.read()                                                                                 #blockfilefile is read into hexadecimalkey
    blockarray = []                                                                                                       #array to keep values nice and tidy
    for i in range(0, len(hexadecimalblock), 2):                                                                        #for loop to find all hex values and put them in the array
        blockarray.append(int(hexadecimalblock[i:i+2], 16))
    return blockarray