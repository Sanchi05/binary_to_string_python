#Here the function will take string of binary as input.
#Eg: "01000001"

def binary_to_string(cipher_text):
    bin_text = cipher_text
    #print(bin_text)
    length = len(bin_text)
    bin_text_list = list(bin_text)
    #print(bin_text_list)
    final = 0
    alpha = ""
    for n in range(len(bin_text_list)):
        num = int(bin_text_list[n])
        multiplier = 2**(length-1)
        #print(multiplier)
        length = length - 1
        outout = num*multiplier
        final = final + outout
    print(chr(final), end = "")
