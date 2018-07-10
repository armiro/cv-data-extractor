import io
import zipfile
import unicodedata
from xml.etree.ElementTree import XML

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'


def is_english(complex_text):
    try:
        complex_text.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


class DocFile:

    def __init__(self, name):
        self.location = './cv_docs/' + name

    def pdf2text(self):
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle, 'ascii')
        page_interpreter = PDFPageInterpreter(resource_manager, converter)
        with open(self.location, 'rb') as file:
            for page in PDFPage.get_pages(file, caching=True, check_extractable=True):
                page_interpreter.process_page(page)
            text = fake_file_handle.getvalue()
        converter.close()
        fake_file_handle.close()
        if text:
            return text
        else:
            return 'Empty'

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


# two = DocFile('test.docx')
# two.word2text()
one = DocFile('test.pdf')
txt = one.pdf2text()
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


