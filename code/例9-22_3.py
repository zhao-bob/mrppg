from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

def pdf2txt(pdf_file):
    with open(pdf_file[:-3]+'txt', 'w', encoding='utf8') as fp_out:
        with open(pdf_file, 'rb') as fp_in:
            # 创建解析器
            parser = PDFParser(fp_in)
            doc = PDFDocument()
            # 关联PDF文档
            parser.set_document(doc)
            # 关联解析器，使得可以根据解析进度动态导入数据
            doc.set_parser(parser)
            doc.initialize(password='')
            # 复用字体、图像等共享资源，避免重复分配内存
            resource_manager = PDFResourceManager()
            # 文本转换器，提取到的文本直接写入文件fp_out
            # 参数laparams指定提取文本的规则，LAParams对象默认值为：
            '''LAParams(line_overlap=0.5, char_margin=2.0,
                        line_margin=0.5, word_margin=0.1,
                        boxes_flow=0.5, detect_vertical=False,
                        all_texts=False, paragraph_indent=None,
                        heuristic_word_margin=False)'''
            device = TextConverter(resource_manager,
                                   fp_out,
                                   laparams=LAParams())
            interpreter = PDFPageInterpreter(resource_manager,
                                             device)
            for page in doc.get_pages():
                # 逐页提取PDF文件中的文本
                interpreter.process_page(page)

    with open(pdf_file[:-3]+'txt', encoding='utf8') as fp:
        print(fp.read())

pdf2txt('测试文件.pdf')
