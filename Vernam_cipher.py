#Vernam cipher for binary
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
    

def encrypt_text(text,one_t_p):
    binary_text = ''.join(format(ord(letter),'08b') for letter in text)
    #print(binary_text)
    one_t_p = ''.join(format(ord(p),'08b') for p in one_t_p)
    #print(one_t_p)
    final_encrypt = ''
    for j in range(len(binary_text)):     
        perf_oper = int(binary_text[j]) ^ int(one_t_p[j])
        final_encrypt = final_encrypt + str(perf_oper)
    return final_encrypt


def decrypt_text(en_text,o_t_p):
    o_t_p = ''.join(format(ord(r),'08b')for r in o_t_p)
    final_decrypt = ""
    for k in range(len(en_text)):
        perf_oper = int(en_text[k])^int(o_t_p[k])
        final_decrypt = final_decrypt + str(perf_oper)
    #print(final_decrypt)
    individual_alpha = [final_decrypt[i:i+8] for i in range(0, len(final_decrypt), 8)]
    #print(individual_alpha)
    for one in individual_alpha:
        binary_to_string(one)


individual_alpha = []
ch = input("Encryption(E) or Decryption(D): ")
if ch.upper() == "E":
    plain_text = input("Enter your text here: ")
    otp_s = input('Enter one time pad: ')
    if len(plain_text) == len(otp_s):
        encrypt_text(plain_text,otp_s)
        func_text = encrypt_text(plain_text,otp_s)
        
        print("Encrypted text(binary): ",func_text)
    else:
        print("The length is of text and one time pad is different.\nPlease try again.😊")
if ch.upper() == "D": 
    en_text_ = input("Enter your binary string: ")
    otp_r_ = input("Enter one time pad: ")
    decrypt_text(en_text_,otp_r_)
    
