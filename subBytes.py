# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256

from sBox import *

def subBytes(block):
    '''
    :param block:Block byts ut mot sBox nummer,
    korresponderat mot [i] (hi:lo) ger rad:kolumn som tas fran sBox i.e 53 = rad 5 kolumn 3 = ed
    :return: returnerar sBox nummret
    '''
    for i in range(len(block)):
        block[i] = sbox[block[i]]
    return block

def subBytesInv(block):
    '''
    :param block:Block byts ut mot den inverterade sBox tabellen,
    mot [i], som ovan fast inverterat i.e ed = rad e kolumn d = 53
    :return:returnerar nummret.
    '''
    for i in range(len(block)):
        block[i] = sboxInv[block[i]]
    return block