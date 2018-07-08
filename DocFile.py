import io
import zipfile
from xml.etree.ElementTree import XML

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'


class DocFile:

    def __init__(self, name):
        self.location = './cv_docs/' + name

    def pdf2text(self):
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle)
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
        for paragraph in tree.getiterator(PARA):
            text = [node.text for node in paragraph.getiterator(TEXT) if node.text]
            for word in text:
                if text:
                    print(text)
                    for word in text:
                        if word == ' ' or word == u'/xa0':
                            text.remove(word)

            # if text:
            #     paragraphs.append(''.join(text))
        return paragraphs


# two = DocFile('test.docx')
# two.word2text()
one = DocFile('test.pdf')
txt = one.pdf2text()
print(txt[::-1])
print(len(txt))