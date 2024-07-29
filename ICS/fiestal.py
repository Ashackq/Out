def slice_half(pl:str):
    return pl[:len(pl)//2],pl[len(pl)//2:]

def feistel_struct(li:str,ri:str,keyi:str):
    return ri,xor(li,f_block(keyi,ri))

def f_block(keyi:str,ri:str):
    retrun xor(keyi,ri)

def xor(str1:str,str2:str):
    xored =''
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            xored +="0"
        else:
            xored +="1"
    return xored

def encrypt_process(pl:str,keys:list[str],rounds:int):
    l1,r1 = slice_half(pl)
    for i in range(rounds):
        l1,r1 = feistel_struct(l1,r1,keys[i])
    return l1+r1
    
def decrypt_process(cipher:str,keys:list[str],rounds:int):
    r1,l1 = slice_half(cipher)
    for i in range(rounds):
        l1,r1 = feistel_struct(l1,r1,keys[i])
    return l1+r1
    
# plain_text = input("Enter Plain text :")
# rounds = int(input("Enter number of rounds :"))
# keys = []
# for i in range(rounds):
#     keys.append(input("Enter the keys"))
plain_text = '0100111101001011'
keys= ["10100110"]
rounds = 1
print(encrypt_process(plain_text,keys,rounds))