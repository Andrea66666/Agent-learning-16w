import pymupdf                    # PyMuPDF 的模块名是 pymupdf
doc = pymupdf.open("2025年度药品审评报告.pdf")
page = doc[0]
text = page.get_text()
print(text[:500])