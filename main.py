# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256

import readKeyFile
import readBlockFile
import rowShifter
import columnMixer
#from mixColTables import *
from sBox import *
from subBytes import *
from rowToCol import *
import addRoundKey
import keyManager

print("Key Sched 1st step:\n")
word = [1,2,3,4]
newWord = keyManager.keyScheduleCore(word,1)
print(word)
print(newWord)
block = readBlockFile.getBlock("testBlock")
key = readKeyFile.getKey("testKey")
print(key)
expandedKey = keyManager.expandKey(key)
print expandedKey
roundKey0 = keyManager.createRoundKey(expandedKey,0)
roundKey7 = keyManager.createRoundKey(expandedKey,7)
roundKey14 = keyManager.createRoundKey(expandedKey,14)

print(roundKey0)
print(roundKey7)
print(roundKey14)

addedRoundKey = addRoundKey.addroundkey(roundKey0,block)
print(addedRoundKey)

'''
print ("Key File:")
key = readKeyFile.getKey("testKey")
print (key)

print ("\nBlock File:")
block = readBlockFile.getBlock("testBlock")
print (block)

print("\nrowToCol:")
test = blockfileColumn(block)
print (test)
print (blockfileColumn(test))#INVERTERING SAME SAME BUT DIFFERENT

print ("\nRowShifter:")
shift = rowShifter.shiftRow(test)
print (shift)
print (blockfileColumn(shift))

print ("\nRowShifterInverter:")
shiftinv = rowShifter.shiftRowInv(block)
print (shiftinv)

print ("\nColumn Mixer:")
colmixer = columnMixer.mixColumns(shiftinv)
print (colmixer)

print ("\nColumn Mixer Inverse:")
colmixerInv = columnMixer.mixColumnsInv(colmixer)
print (colmixerInv)

print ("\nSboxes:")
print (sbox[0]),
print (sboxInv[0]),
print (rCon[0])

print ("SubBytes:")
sub = subBytes(block)
print (sub)

print ("SubBytesInv:")
subInv = subBytesInv(sub)
print (subInv)
'''