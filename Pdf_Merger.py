#py -m pip install PyPDF2
import PyPDF2

pdfiles=["pdf1.pdf","pdf2.pdf"]
merger=PyPDF2.PdfMerger()

if(__name__=="__main__"):

    for filename in pdfiles:
        pdfFile=open(filename,"rb")
        pdfReader=PyPDF2.PdfReader(pdfFile)
        merger.append(pdfReader)
    pdfFile.close()
    merger.write("merged.pdf")    