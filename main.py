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

print ("Key File:")
key = readKeyFile.getKey("testKey")
print (key)

print ("\nBlock File:")
block = readBlockFile.getBlock("testBlock")
print (block)

print ("\nRowShifter:")
shift = rowShifter.shiftRow(block)
print (shift)

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


