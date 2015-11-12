### READS KEY FILE ###


def getKey(filename, i=2):
    filename = open(filename)
    while i < len(filename):
        chars = filename.read(i-2, i)
        encode = int(chars)
        i += 2
    return encode

HEJEHEJEHHEJESWDAJLA