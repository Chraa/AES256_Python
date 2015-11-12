### READS KEY FILE ###


def getKey(filename):
    keyfile = open(filename, 'r')                                                                                       #keyfile opens file specified in main.py
    hexadecimalkey = keyfile.read()                                                                                     #keyfile is read into hexadecimalkey
    keyarray = []                                                                                                       #array to keep values nice and tidy
    for i in range(0, len(hexadecimalkey), 2):                                                                          #for loop to find all hex values and put them in the array
        keyarray.append(int(hexadecimalkey[i:i+2], 16))
    return keyarray                                                                                                     #returns the array.