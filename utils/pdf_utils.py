from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def export_text_to_pdf(text, filename="output.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    lines = text.split('\n')
    y = height - 50
    for line in lines:
        c.drawString(50, y, line)
        y -= 15
        if y < 50:
            c.showPage()
            y = height - 50
    c.save()