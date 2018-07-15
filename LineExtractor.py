from DocFileObjects import *


def is_english(complex_text):
    try:
        complex_text.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


txt.encode('utf-8')
txt = txt.strip().split()
txt = txt[::-1]

# print(txt)

cleared = list()
for word in txt:
    if is_english(word):
        pass
    else:
        word = word[::-1]
    cleared.append(word)

print(cleared)