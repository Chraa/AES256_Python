# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256

from subBytes import *

def keyScheduleCore(word, i):
    '''
    :param word:T fran expandKey som ar de 4 sista bytes per 32byte iteration som skapar nastkommande rotering av nyckelvarden
    :param i:iterationen fran expandKey. ar 1-8 (keyScheduleCore anvands 8ggr per nyckel)
    :return:returnerar vardet av newWord dar forsta vardet blir Xor med rCon[i] dar [i] kommer fran expandKey rConIter
    '''
    newWord = word[1:]+word[:1]#Skiftar vardet ett steg vanster
    subBytes(newWord)#Skickar newWord till subBytes som far nya varden.
    newWord[0] = newWord[0] ^ rCon[i]#forsta vardet i newWord blir Xor med rCon[i]
    return newWord

def expandKey(cipherKey):
    '''
    :param cipherKey:
    Denna klarade inte jag av att skriva sjalv och all credit ar:
    http://brandon.sternefamily.net/wp-content/uploads/2007/06/pyAES.txt
    :return:returnerar en expanderad nyckel pa 256 bit(dar borjan ar originalnyckel)
    Anvander sista 4 bit av nyckeln for att skapa resterande varden sa att nyckeln blir 256 bit.
    detta sker i rundor av 32bit
    '''
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
    '''
    :param expandedKey: far in expanded key tar ut i*16bits och i*16+16bits
    :param i: iterationen fran vilken runda AESCryptot ar pa, Borjar pa 0.
    :return:returnerar ett 16 bit langt varde, beroende pa iteration.
    '''
    return expandedKey[i*16:i*16+16]