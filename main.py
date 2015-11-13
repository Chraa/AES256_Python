# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256

import readKeyFile
import readBlockFile
import rowShifter
import columnMixer
from mixColTables import *

print ("Key File:")
#reads key from file
key = readKeyFile.getKey("testKey")
print (key)

#blank rows
print ("\nBlock File:")

#reads block from file
block = readBlockFile.getBlock("testBlock")
print (block)

#blank rows
print ("\nRowShifter:")

shift = rowShifter.shiftRow(block)
print (shift)

#blank rows
print ("\nRowShifterInverter:")

shiftinv = rowShifter.shiftRowInv(block)
print (shiftinv)

#blank rows
print ("\nColumn Mixer:")

colmixer = columnMixer.mixColumns(shiftinv)
print (colmixer)

#blank rows
print ("\nColumn Mixer Inverse:")

colmixerInv = columnMixer.mixColumnsInv(colmixer)
print (colmixerInv)