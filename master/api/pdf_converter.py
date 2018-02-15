from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
from os import getcwd,path,makedirs

def pdf_to_text(filepath):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'ascii'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(filepath, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    outpath = getcwd()+'\\Books'
    if path.exists(outpath):
        pass
    else:
        makedirs(outpath)
    outfile = outpath+'\\'+filepath.split('\\')[-1].split('.')[0]+'.txt'

    with file(outfile,'w') as fo:
        fo.write('\n'.join(' '.join(text.split('\n')).split('.')).replace('- ',''))

    fp.close()
    device.close()
    retstr.close()

    return outfile
