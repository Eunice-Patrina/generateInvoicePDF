import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoice/*.xlsx")

for filepath in filepaths:
    # read excel file into data frame
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # extract  invoice nr and date of invoice
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    # Generate PDF invoice
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice nr {invoice_nr}", ln=1)
    pdf.cell(w=50, h=8, txt=f"Date {date[::-1]}", ln=1)

    pdf.output(f"PDFs/{filename}.pdf")
