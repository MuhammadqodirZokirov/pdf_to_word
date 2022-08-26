from pdf2docx import converter

pdffile = "test.pdf"
docxfile = "test.docx"

cv = converter.Converter(pdffile, docxfile)
cv.convert()
cv.make_docx(docxfile)
cv.close()
