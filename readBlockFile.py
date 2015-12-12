# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256


def getDecryptBlock(block):
    '''
    :param block:oppnar filen som skickas fran main i read lage, laser in 2 byte at gangen(hexvarden)
    : gor om det till intvarden stegar upp 2 bytes. Skapar lista med listor 16 byte stora.
    :return:returnerar lista med listor 16 bytes block.
    '''
    file = open(block, 'r')
    byte = file.read()
    blockarray = []
    block = []
    for i in range(0,len(byte),2):
        blockarray.append(int(byte[i:i+2],16))

    for i in range(0,len(blockarray),16):
        block.append(blockarray[i:i+16])
    return block

def getEncryptBlock(block):
    '''
    :param block: oppnar filen binart (rb) och gor om den till hexvarden laser in 2 byte varden i arr[]
    : ar aven med en padding metod som kollar om langden pa arr[] ar mer eller mindre an 16 bytes.
    : detta ar en losning for att padda ut blocket till 16 bytes om det ar for kort.
    :return: returnerar blocket i 16 bytes langd.
    '''
    file = open(block,'rb')
    byte = file.read().encode("hex")
    blockarray = []
    arr = []
    for i in range(0,len(byte),2):
        arr.append(int(byte[i:i+2], 16))

    while len(arr) >= 16:
        blockarray.append(arr[0:16])
        arr = arr[16:]
        if len(arr) < 16:
            temparray = [0]*16
            for k in range(0,len(arr)):
                temparray[k] = arr[k]
            blockarray.append(temparray)
    return blockarray

