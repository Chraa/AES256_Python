# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256
from readKeyFile import *
from keyManager import *
from addRoundKey import *
from rowShifter import *
from columnMixer import *

def encrypt(block,key):

    #INITIALIZE
    expandedKey = expandKey(key)
    #0 ROUND
    roundKey = createRoundKey(expandedKey,0)
    block = addroundkey(block,roundKey)

    for i in range(1,14):
        roundKey = createRoundKey(expandedKey,i)
        block = subBytes(block)
        block = shiftRow(block)
        block = mixColumns(block)
        block = addroundkey(block,roundKey)

    roundKey = createRoundKey(expandedKey,14)
    block = subBytes(block)
    block = shiftRow(block)
    block = addroundkey(block,roundKey)

    return block
