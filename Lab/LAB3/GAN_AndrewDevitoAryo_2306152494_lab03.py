# Nama  : Andrew Devito Aryo
# NPM   : 2306152494
# Kelas : C

# PROGRAM TO CONVERT DEC -> HEX, AND HEX -> DEC

# WAY TO CONVERT DEC TO HEX
# for example, we have input = 24
# To find the Hex representation, then:
#     24
# 8 ------- %16
#      1
# 1 ------- %16
#      0 
# Then, the representation of 24 in hex is 0x18

print('Lab 03\n')
print('From Decimal to Hexadecimal')
print('---------------------------')

# read the user's input
myInt = int(input('Give a positive integer in decimal representation: ')) 

# convert the integer stored in myInt to hex digits
hexstr = '' # accumulator for hex digits, starting with empty string
temp = myInt # Store myInt in Temporary Variable
while temp != 0:
    hexdigit = temp%16 # Find the remainder of temp divided by 16
    if (hexdigit < 10):
        hexstr = str(hexdigit) + hexstr # Add the hexdigit from right to left
    else:
        # If-statement to convert 10, 11, 12, 13, 14, 15 to Hex
        if hexdigit == 10:
            hexstr = "A" + hexstr
        elif hexdigit == 11:
            hexstr = "B" + hexstr
        elif hexdigit == 12:
            hexstr = "C" + hexstr
        elif hexdigit == 13:
            hexstr = "D" + hexstr
        elif hexdigit == 14:
            hexstr = "E" + hexstr
        elif hexdigit == 15:
            hexstr = "F" + hexstr
    temp = temp // 16 # Find the floor division of temp divided by 16

print('The hexadecimal representation of',myInt,'is','0x' + hexstr + '\n')


# WAY TO CONVERT HEX TO INT
# For example we have input = 0x123
# To convert hex to int, we must know the power of each digit
#   1        2      3
# 16**2   16**1   16**0
# And then, to find the dec representation, 
# Dec = 3*16**0 + 2*16**1 + 1*16**2
# Dec = 291
# Then, the Decimal Representation of 0x123 is 291

# read the hex string from the user
hexstr = input('Give a positive integer in hexadecimal representation: ')

# convert the hex string to a correct decimal integer
temp = hexstr[2:] # remove '0x' using string slicing
newInt = 0 # accumulator for decimal value
power = 0

while temp != '':
    hexdigitstr = temp[-1]
    # Determine the value of A, B, C, D, E, and F in Dec
    if hexdigitstr == 'A':
        hexdigitstr = 10
    elif hexdigitstr == 'B':
        hexdigitstr = 11
    elif hexdigitstr == 'C':
        hexdigitstr = 12
    elif hexdigitstr == 'D':
        hexdigitstr = 13
    elif hexdigitstr == 'E':
        hexdigitstr = 14
    elif hexdigitstr == 'F':
        hexdigitstr = 15

    newInt += int(hexdigitstr) * (16**power)
    power += 1
    temp = temp[:-1]

print('The decimal representation of', hexstr, 'is', newInt)
print()
print('Thanks for using this program.')
print()
input('Press Enter to continue ...') # hold the screen display

# --- END OF THE PROGRAM --- 