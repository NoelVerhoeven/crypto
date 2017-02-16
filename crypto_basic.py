import math

# def text2base64(str: text):
#     asci = ''
#     while text:
#         s = text[0]
#         text=text[1:]
#         asci = s.ord()
#         asci = asci + ascii_2_bin(asci)
#         binary to groups of 6
#         padd with 0 to divisible by 6
#         binary to ascii
#         asci to hex
#         pad with = divisible by 8

def ascii_2_bin(num):
    '''Returns a binary string representaton of the integer value'''
    bin = ''
    while num > 0:
        if math.fmod(num,2) == 1:
            bin = '1' + bin
            num = num - 1
        else:
            bin = '0' + bin
        num = num / 2
    return bin

num = 12636633676
l = ascii_2_bin(num)
print('binary of ' + str(num) +' is ' + l)
print('length: ' + str(len(l)))
