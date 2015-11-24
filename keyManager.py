# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256

from sBox import *
from subBytes import *

def keyScheduleCore(word, i):
    newWord = word[1:]+word[:1]
    subBytes(newWord)
    newWord[0] = newWord[0] ^ rCon[i]
    return newWord

def expandKey(cipherKey):
    cipherKeySize = len(cipherKey)
    assert cipherKeySize == 32
    expandedKey = []
    currentSize,rconIter = 0,1

    # temporary list to store 4 bytes at a time
    t = [0,0,0,0]

    # copy the first 32 bytes of the cipher key to the expanded key
    for i in range(cipherKeySize):
        expandedKey.append(cipherKey[i])
    currentSize += cipherKeySize

    # generate the remaining bytes until we get a total key size of 240 bytes
    while currentSize < 240:
        # assign previous 4 bytes to the temporary storage t
        for i in range(4):
            t[i] = expandedKey[(currentSize - 4) + i]

        # every 32 bytes apply the core schedule to t
        if currentSize % cipherKeySize == 0:
            t = keyScheduleCore(t, rconIter)
            rconIter += 1

        # since we're using a 256-bit key -> add an extra sbox transform
        if currentSize % cipherKeySize == 16:
            for i in range(4):
                t[i] = sbox[t[i]]

        # XOR t with the 4-byte block [16,24,32] bytes before the end of the current expanded key. These 4 bytes become the next bytes in the
        # expanded key
        for i in range(4):
            expandedKey.append(((expandedKey[currentSize - cipherKeySize]) ^ (t[i])))
            currentSize += 1

    return expandedKey

def createRoundKey(expandedKey,i):
    return expandedKey[i*16:i*16+16]