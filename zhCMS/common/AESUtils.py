import base64
from Crypto.Cipher import AES
import random

'''
采用AES对称加密算法
'''


# str不是32的倍数那就补足为16的倍数
def add_to_32(value):
    while len(value) % 32 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes


# 加密方法
def encrypt_oracle(v):
    if v is not None:
        # 秘钥
        # key = 'lymhqnoetl15321'
        key = 'zhaoxuniubi'
        # 待加密文本
        # 初始化加密器
        aes = AES.new(add_to_32(key), AES.MODE_ECB)
        # 先进行aes加密
        encrypt_aes = aes.encrypt(add_to_32(v))
        # 用base64转成字符串形式
        encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
        # print(encrypted_text)
        return encrypted_text
    else:
        return ''

# 解密方法
def decrypt_oralce(text):
    # 秘钥
    key = 'zhaoxuniubi'
    # 密文
    # 初始化加密器
    aes = AES.new(add_to_32(key), AES.MODE_ECB)
    # 优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
    # 执行解密密并转码返回str
    decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')
    return decrypted_text


def sub():
    sub_code = ''
    for i in range(6):
        sub_code += str(random.randint(0, 9))
    return sub_code


if __name__ == '__main__':
    # encrypt_oracle()
    a = encrypt_oracle(sub(6))
    print(a)
    #
    # print(decrypt_oralce('a' + a))
