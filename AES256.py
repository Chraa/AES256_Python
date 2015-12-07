# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256

from keyManager import *
from addRoundKey import *
from rowShifter import *
from columnMixer import *

def encrypt(block,key):
    '''
    :param block:blocket kommer fran main, dar vi itererar igenom filen som ska krypteras. 16byte langt varde
    :param key: Nyckeln som kommer fran Main(alltsa "huvudnyckeln")
    :return:returnerar krypterade block 16byte i taget.
    '''
    #INITIALIZE
    expandedKey = expandKey(key)#Gor om nyckel till 256bit nyckel.
    #0 ROUND
    roundKey = createRoundKey(expandedKey,0)#roundKey = 16bit nyckeldel
    block = addroundkey(block,roundKey)
    #ROUND 1 - 13
    for i in range(1,14):
        roundKey = createRoundKey(expandedKey,i)
        block = subBytes(block)
        block = shiftRow(block)
        block = mixColumns(block)
        block = addroundkey(block,roundKey)

    #Round 14
    roundKey = createRoundKey(expandedKey,14)
    block = subBytes(block)
    block = shiftRow(block)
    block = addroundkey(block,roundKey)

    return block

def decrypt(block,key):
    '''
    :param block:
    :param key:
    :return:
    '''
    #initialize decrypt
    expandedKey = expandKey(key)
    roundKey = createRoundKey(expandedKey,14)
    block = addroundkey(block,roundKey)
    block = shiftRowInv(block)
    block = subBytesInv(block)

    for i in range(13,0,-1):
        roundKey = createRoundKey(expandedKey,i)
        block = addroundkey(block,roundKey)
        block = mixColumnsInv(block)
        block = shiftRowInv(block)
        block = subBytesInv(block)

    roundKey = createRoundKey(expandedKey,0)
    block = addroundkey(block,roundKey)

    return block