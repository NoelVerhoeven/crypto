import codecs

Base64Table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']


def hex_2_raw(s):
    """Return raw bytes from a hexadecimal string."""
    return codecs.decode(s, 'hex')


def text_2_base64_full(text):
    '''Show by code what needs to be done to get form text to base64,
        instead of looking up a library call'''

    print(text)
    # get the text and make a hexstring out of it
    hexstr = ''
    while text:
        # get the ordinal number (ascii value)
        o = ord(text[0])
        # convert into hex value, strip off the 0x
        h = hex(o)[2:]
        # add to resulting string
        hexstr += h
        # strip off char of input text
        text = text[1:]

    # continue with coding onthe hex string
    hex_2_base64_full(hexstr)


def hex_2_base64_full(hexstr):
    """Show by code what needs to be done to get form hex to base64,
        instead of looking up a library call

        Note this implementation has errors wrt padding / nr of input < 4"""

    bitpattern = ''
    while hexstr:
        intval = int(hexstr[:2], 16)
        # format to binary, 8 bits format, keeping leading zeroes
        newbits = format(intval, '08b')
        bitpattern += newbits
        hexstr = hexstr[2:]

    # pad the bitstring with zeroes until divisble by 6
    bitpattern += '00000000' * (len(bitpattern) % 6)

    base64 = ''
    while bitpattern:
        # find the index in the base64 table
        index = int(bitpattern[:6], 2)
        # map index to the base64 table
        base64 += Base64Table[index]
        bitpattern = bitpattern[6:]
    return base64


def hex_2_base64(text):
    """Transform a hex string into its Base64 representation."""
    return codecs.encode(hex_2_raw(text), 'base64').decode()


def fixed_xor(in1, in2):
    """function that takes two equal-length buffers and produces
    their XOR combination"""
    if len(in1) != len(in2):
        print('Error: Input lengths not equal!')
        return None

    r1 = hex_2_raw(in1)
    r2 = hex_2_raw(in2)
    xorred = ''
    for b1, b2 in zip(r1, r2):
        xorred += hex(b1 ^ b2)[2:]

    return xorred


# print (
#   text_2_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))
if __name__ == "__main__":
    arg = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print(hex_2_base64(arg))
    print(fixed_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965'))
    print('746865206b696420646f6e277420706c6179')
