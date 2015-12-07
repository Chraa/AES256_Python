# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256

import readKeyFile
from readBlockFile import *
from AES256 import *
import argparse
from argparse import RawTextHelpFormatter
import time

parser = argparse.ArgumentParser(description='''
    ---------------------------------------
    HOGSKOLAN DALARNA (www.du.se)
    Course:     DT2017 Kryptologi
    Project:    AES256
    Written by: Patric Wallin
    Hela detta program har diskuterats
    igenom och skapats med hjalp av mina
    klasskamrater Martin Lindstrand &
    Christoffer Claesson.
    ---------------------------------------

''', formatter_class=RawTextHelpFormatter)
parser.add_argument('mode',help="encrypt or decrypt")
args = parser.parse_args()

mode = str(args.mode).lower()


def fileEncrypt():
    '''
    :KRYPTERINGSINITIERINGEN
    :Startar tid och skickar ivag getEncryptedBlock() till sin metod i readBlockFile.py
    :skriver ut langden pa Blocket
    :Key lases in genom readKeyFile.getKey() i readKeyFile.py
    :outfile = filen som returneras ut fran programmet
    :sedan kors en iterering av langden i blocket dar jag skickar med block for block som blir krypterat
    :efter det sa itereras lister av listor igenom sa att jag far ut en enda ren textstrang
    :har kommer hex() och zfill till anvandning hex(item) vardet so mska till strangen, 2: och frammot fylls med 0
    :zfill(2) fyller ut med nollor om det inte ar fullt av varden i de 2 slotsen.
    :return:BLANK.. stanger filer och skriver ut resultat.
    '''
    start = time.clock()
    block = getEncryptBlock("tWotW.7z")
    print len(block)
    startkrypt = time.clock()
    key = readKeyFile.getKey("testKey")
    outfile = open("encrypted_file_7z","wb")
    strangen = ""
    cryptLargeblock = []
    for i in range(len(block)):
        cryptLargeblock.append(encrypt(block[i],key))

    while i < len(cryptLargeblock):
        for row in cryptLargeblock:
            for item in row:
                strangen += hex(item)[2:].zfill(2)
        i += 1
    outfile.write(strangen)
    outfile.close()
    kryptelapsed = time.clock()-startkrypt
    elapsed = time.clock()-start
    print len(cryptLargeblock)
    print "Total Tid: " + str(elapsed)
    print "Krypteringstid: " + str(kryptelapsed)

def fileDecrypt():
    start = time.clock()
    key = readKeyFile.getKey("testKey")
    file = open("decrypted_file.7z","wb")
    decrypttime = time.clock()
    decryptBlock = []
    decString = ""
    eblock = getDecryptBlock("encrypted_file_7z")
    print len(eblock)

    for i in range(len(eblock)):
        decryptBlock.append(decrypt(eblock[i],key))

    for row in decryptBlock:
        for item in row:
            decString += chr(item)

    file.write(decString)
    file.close()
    decryptelapsed = time.clock()-decrypttime
    elapsed = time.clock()-start
    print "Total Tid: " + str(elapsed)
    print "Dekrypteringstid: " + str(decryptelapsed)

if mode == "encrypt" or mode == "e":
    fileEncrypt()
elif mode == "decrypt" or mode == "d":
    fileDecrypt()




