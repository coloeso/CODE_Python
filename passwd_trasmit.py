'''
step1.input original passwd
step2.switch original to ascii
step3.use xor drop the ascii in (0x8-f) interval
'''
def char_to_ascii(char):
    return ord(char)

inputstr = input("input your passwd: \n")

ascii_text = []
for i in inputstr:
    ascii_text.append(char_to_ascii(i))

ascii_text_hex = []
ascii_text_bin = []

ascii_text_hex = [hex(x) for x in ascii_text]
ascii_text_bin = [bin(x) for x in ascii_text]

ascii_text_xor = []
for i in ascii_text:
    ascii_text_xor.append(i ^ mask_xor)

ascii_text_final = []
for i in ascii_text_xor:
    ascii_text_final.append(i & mask_and)



print("the final passwd is:", ascii_text_final_hex)
