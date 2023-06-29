import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

files = glob.glob('excel_files/*.xlsx')

for filepath in files:
    file_1 = pd.read_excel(filepath)
    pdf = FPDF(orientation="P", unit='mm', format='A4')
    pdf.add_page()
    path = Path(filepath).stem
    invoice_nr = path.split('-')[0]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date {path.split('-')[1]}", ln=1)
    total_price = 0

#Add a header
    header = list(file_1.columns)

    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=header[0].replace('_',' '), border=1)
    pdf.cell(w=70, h=8, txt=header[1].replace('_',' '), border=1)
    pdf.cell(w=30, h=8, txt=header[2].replace('_',' '), border=1)
    pdf.cell(w=30, h=8, txt=header[3].replace('_',' '), border=1)
    pdf.cell(w=30, h=8, txt=header[4].replace('_',' '), border=1, ln=1)
#Add Rows to the table
    for index, row in file_1.iterrows():
        pdf.set_font(family="Times", size=10, style="")
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=70, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)
        total_price += row['total_price']

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=30, h=8, txt=f"Total Price-{total_price}", ln=1)

    pdf.output(f"PDFs/{path}.pdf")
