# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256

def addroundkey(block,roundKey):
    '''
    :param block:
    :param roundKey:16bitars nyckel som kommer fran keyManager:createRoundKey
    :return:
    '''
    for i in range(len(block)):
        block[i] = block[i] ^ roundKey[i]
    return block