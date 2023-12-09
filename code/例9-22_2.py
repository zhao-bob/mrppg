from io import StringIO
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

def pdf2txt(pdf_file):
    result = StringIO()
    with open(pdf_file, 'rb') as fp:
        parser = PDFParser(fp)
        doc = PDFDocument()
        parser.set_document(doc)
        doc.set_parser(parser)
        doc.initialize(password='')
        resource_manager = PDFResourceManager()
        device = TextConverter(resource_manager,
                               result,
                               laparams=LAParams())
        interpreter = PDFPageInterpreter(resource_manager,
                                         device)
        for page in doc.get_pages():
            interpreter.process_page(page)

    with open(pdf_file[:-3]+'txt', 'w', encoding='utf8') as fp:
        fp.write(result.getvalue())

pdf2txt('D:/教学课件/Python程序设计基础（第3版）/code/需要覆盖内容的文件.pdf')
