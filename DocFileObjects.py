from DocFile import DocFile

# two = DocFile('test.docx')
# two.word2text()
one = DocFile('CV10.pdf')
raw_text = one.pdf2textlines()
# print(raw_text)
for i in raw_text:
    print(i)
