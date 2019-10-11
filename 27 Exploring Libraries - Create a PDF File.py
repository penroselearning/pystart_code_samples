try:

    from fpdf import FPDF
    from datetime import datetime

    pdf = FPDF()
    pdf.add_page()  # Page 1
    pdf.set_font('Arial', 'B', 12)  # Sets the Font Name and Size
    pdf.set_fill_color(10, 120, 120)  # Defines a Color to fill Objects with RGB Color Code
    pdf.rect(0, 0, 300, 20, 'F')  # Creates a Rectangular Shape on the Page

    pdf.set_text_color(255,255,255)
    pdf.cell(0, 5, 'List of Continents')
    pdf.ln()
    pdf.ln()
    pdf.ln()

    pdf.set_text_color(0, 0, 0)

    continents = ['Asia', 'Africa', 'Antartica', 'Australia', 'Europe', 'North America', 'South America']

    for continent in continents:  # Prints Numbers from 1 to 10 in the PDF File
        pdf.cell(0, 5, continent)
        pdf.ln()  # New Line

    pdf.add_page()  # Page 2
    pdf.cell(0, 5, "Page 2")
    filename = 'TestFile'+str(datetime.now())+ '.pdf'
    pdf.output(filename, 'F')  # Converts the Content to PDF

except ModuleNotFoundError:
    print('Kindly import the fpdf Library')