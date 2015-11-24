# # # # # # # # # # # #
# DT2016
# PATRIC WALLIN
# DU.SE
# PYTHON ENCRYPTOR/DECRYPTOR AES 256

def blockfileColumn(filename):
    test2 = filename
    testarr = []
    for row in range(0,4):
        for column in range(0,len(test2),4):
            testarr.append(test2[row+column])

    return testarr