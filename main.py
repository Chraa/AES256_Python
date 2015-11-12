# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256

import readKeyFile
import readBlockFile

print ("Key File:")
#reads key from file
key = readKeyFile.getKey("testKey")
print (key)

#blank rows
print ("\nBlock File:")

#reads block from file
block = readBlockFile.getBlock("testBlock")
print (block)

