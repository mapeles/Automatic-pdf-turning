from PyPDF2 import PdfReader,PdfWriter
import os
from tkinter import filedialog
from tkinter import messagebox
                                       
files = filedialog.askopenfilename(initialdir="/",\
                 title = "파일을 선택 해 주세요",\
                    filetypes = (("*.pdf","*pdf"),("*.pdf","*pdf"),("*.pdf","*pdf")))

if files == '':
    messagebox.showwarning("경고", "파일을 추가 하세요")


def pdf(length):
    a = len(length)
    print(a)
    seq = [0 for _ in range(a)]
    seqrev = [False for _ in range(a)]#돌리기 여부
    for i in range(1,a+1,2):
        seq[i-1] = i
    b = 2
    if a % 2 == 0:
        for i in range(-1, -(a), -2):
            seqrev[i] = True
            seq[i] = b
            b+= 2
    else:
        for i in range(-2, -(a), -2):
            seq[i] = b
            seqrev[i] = True
            b+= 2
    print(seq,seqrev)
    return seq,seqrev

pdfReaded = PdfReader(open(files,"rb"))

pdfWriting = PdfWriter()
for i in range(len(pdfReaded.pages)):
    pdfWriting.add_page(pdfReaded.pages[i])
if len(pdfReaded.pages)%2 == 1:
    pdfWriting.add_blank_page()
pdfReaded = pdfWriting

pdf_seq, pdf_rev = pdf(pdfReaded.pages) 

pdfWriting = PdfWriter()
for idx, i in enumerate(pdf_seq):
    page = pdfReaded.pages[i-1]
    if pdf_rev[idx] == True:
        page.rotate(180)
    pdfWriting.add_page(page)


file_name = os.path.basename(files)
base_name, extension = os.path.splitext(file_name)
new_file_name = f"{base_name}-turned{extension}"
new_file_path = os.path.join(os.path.dirname(files), new_file_name)
print(new_file_path)

pdfWriting.write(open(new_file_path, 'wb'))
