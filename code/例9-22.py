import os
import sys
import time

pdfs = (pdf for pdf in os.listdir('.') if pdf.endswith('.pdf'))
for pdf1 in pdfs:
    pdf = pdf1.replace(' ', '_').replace('-', '_').replace('&', '_')
    os.rename(pdf1, pdf)
    print('='*30 + '\n', pdf)

    txt = pdf[:-4] + '.txt'
    exe = '"' + sys.executable + '" "'
    pdf2txt = os.path.dirname(sys.executable) + \
              '\\scripts\\pdf2txt.py" -o'

    cmd = exe + pdf2txt + txt + ' ' + pdf
    try:
        os.popen(cmd)
        time.sleep(3)
        with open(txt, encoding='utf-8') as fp:
            print(fp.read(200))
    except:
        pass

