import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

files=glob.glob('excel_files/*.xlsx')

for filepath in files:
    file_1=pd.read_excel(filepath)
    pdf=FPDF(orientation="P",unit='mm',format='A4')
    pdf.add_page()
    path=Path(filepath).stem
    invoice_nr=path.split('-')[0]
    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8,txt=f"Invoice nr. {invoice_nr}")
    pdf.output(f"PDFs/{path}.pdf")


