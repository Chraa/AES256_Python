# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256

def addroundkey(block,roundKey):
    '''
    :param block: 16byte block som XOR:as med roundKey i langden av block.
    :param roundKey:16bitars nyckel som kommer fran keyManager:createRoundKey
    :return: returnerar ett xorat block
    '''
    for i in range(len(block)):
        block[i] = block[i] ^ roundKey[i]
    return block