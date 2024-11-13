def decrypt_cypher_text(encrypted_text, key):
#     # function implementation here...
    decrypted_text = ""
    list = []
    for i in encrypted_text:
        list.append(ord(i)-3)
    for i in list:
        decrypted_text += chr(i)
    return decrypted_text

print(decrypt_cypher_text('Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu$', 3))