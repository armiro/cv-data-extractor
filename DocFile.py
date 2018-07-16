import zipfile
import unicodedata
from xml.etree.ElementTree import XML
import fitz


WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'


class DocFile:

    def __init__(self, name):
        self.location = './cv_docs/' + name
        self.format = self.location.split(".")[-1]

    def pdf2text(self):
        document = list()
        file_text = list()
        if self.format == 'pdf':
            document = fitz.open(self.location)
        else:
            print('Error! This file is not in PDF format')
        if document:
            for page in document:
                raw_text = page.getText()
                print(page.getFontList())
                file_text.append(raw_text)
            if file_text:
                return file_text
            else:
                return 'Empty file!'
        else:
            print('Reading PDF file aborted.')
            return None

    def word2text(self):
        document = zipfile.ZipFile(self.location)
        xml_content = document.read('word/document.xml')
        document.close()
        tree = XML(xml_content)

        paragraphs = list()
        cleared_text = list()
        for paragraph in tree.getiterator(PARA):
            text = [node.text for node in paragraph.getiterator(TEXT) if node.text]
            if text:
                for word in text:
                    word = unicodedata.normalize("NFKD", word)
                    word.strip()
                    print(word)
        # print(cleared_text)
        # if text:
        #     paragraphs.append(''.join(text))
        return paragraphs


