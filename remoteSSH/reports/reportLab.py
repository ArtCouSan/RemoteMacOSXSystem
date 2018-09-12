from reportlab.pdfgen import canvas
from datetime import datetime
import os
global canvas

def geraPdf(canvas, reports):

    # Cria nome de arquivo com data
    now = datetime.now()
    arquivoName = "Report {} - {} - {}.pdf".format(now.day, now.month, now.year)
    
    arquivoLocal = os.path.join(os.path.expanduser("~"), "Desktop/", arquivoName)

    canvas = canvas.Canvas(arquivoLocal)
    canvas.setLineWidth(.3)
    canvas.setFont('Helvetica', 12)

    i = 750

    for report in reports:

        canvas.drawString(30,i, report)
        i = i + 15
    
    canvas.save()