def ROT13(word):
    out = []
    for i in word.lower():
        new_word = ord(i)+13
        if new_word > ord('z'):
            new_word -= 26
        out.append(chr(new_word))
    return ''.join(out)

# print(ROT13('apple'))
'''
import codecs

print(codecs.encode('apple','rot_13'))
'''


