"""
Sana : 20/11/2022
Sobirjonov Khusanboy
Matnni shifrlab beruvchi hamda shifrdan chiqaruvchi bot 1 - qism
Amaliyot
"""
def is_num(text):
    """Matnni shifrlangan yoki shifrlanmaganini tekshiruvchi funksiya"""
    str1 = ''
    if 'cipher1' == text[:7]:
        str1 = shifr_key(text)
    elif 'cipher2' == text[:7]:
        str1 = shifr_sezar_key(text[9:])
    elif '2' == text[0]:
        str1 = shifr_sezar(text)
    else:
        str1 = shifr(text)
    return str1
   
def shifr_sezar(text):
    """Yuliy Sezar shifri asosida shifrlovchi funksiya"""
    cipher = ''
    for i in range(len(text)):
        cipher += chr(ord(text[i]) + 3)
    return cipher
 
def shifr_sezar_key(text):
    """Yuliy Sezar shifridan chiqaruvchi funksiya"""
    cipher_key = ''
    for i in range(len(text)):
        cipher_key += chr(ord(text[i]) - 3)
    return cipher_key
    
def bintodec(binary):
    """Sonni ikkilik sanoq sistemasidan 10 lik sanoq sistemasiga o'tkazadi"""
    binary = int(binary)
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def shifr(text):
    """Matnni shifrlab beruvchi funksiya"""
    size = len(text)
    shifr = ''
    for i in range(size):
        shifr += bin(ord(text[i]))[2:] + ' '
    return shifr

def shifr_key(text):
    """Matnni shifrdan chiqaruvchi funksiya"""
    size = len(text)
    str1 = ''
    ans = False
    mn, mx = 7, 0
    for i in range(7,size):
        if text[i] == ' ':
            mx = i
            ans = True
        if ans:
            str1 += chr(bintodec(text[mn:mx]))
            mn = mx
            ans = False
    if text[size - 1] != ' ':
        str1 += chr(bintodec(text[mn:]))
    return str1













