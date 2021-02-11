from PyPDF2 import PdfFileWriter, PdfFileReader
def sec_pdf(file, pswd):
    parser = PdfFileWriter()
    pdf = PdfFileReader(file)
    for pg in range(pdf.numPages):
        parser.addPage(pdf.getPage(pg))
    parser.encrypt(pswd)
    with open(f"encrypted_{file}", "wb") as f:
        parser.write(f)
        f.close()
    print(f"encrypted_{file} created!")
if _name_ == "_main_":
    file = "filename.pdf"
    pswd = "mypass"
    sec_pdf(file, pswd)
