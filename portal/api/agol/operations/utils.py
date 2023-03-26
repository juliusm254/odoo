# def inline_serializer(*, fields, data=None, **kwargs):
#     serializer_class = create_serializer_class(name='', fields=fields)

#     if data is not None:
#         return serializer_class(data=data, **kwargs)

#     return serializer_class(**kwargs)

from io import BytesIO
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Table
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
# from barcode import EAN13
# from barcode.writer import ImageWriter


def create_pdf( order_no,
                truck_reg,
                truck_epra,
                truck_trans,
                trailer_reg,
                trailer_epra,
                trailer_trans,
                q1,
                q2,
                q3,
                q4,
                c1,
                c2,
                c3,
                c4,                
                warehouse,
                date,
                time,
                pallets_pos,
                pallets):
    buffer = BytesIO()
    canvas = Canvas(buffer, pagesize=A4)
    WIDTH, HEIGHT = A4
    MARIGIN = 1.5 * cm
    canvas.translate(MARIGIN, HEIGHT-MARIGIN)
    # pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
    # pdfmetrics.registerFont(TTFont('Verabd', 'Verabd.ttf'))
    # pdfmetrics.registerFont('Courier')
    
    font = canvas.getAvailableFonts()
    print(font)

    # header
    canvas.setFont("Helvetica", size=14)
    canvas.drawString(150, 0, "Appendix two: BULK LPG Pre-entry Checklist")
    canvas.setFont("Helvetica-Bold", size=10)
    canvas.drawString(400, -0.9*cm, "SAFETY INSPECTION")
    canvas.setStrokeGray(0)
    canvas.line(0, -1*cm, WIDTH - 2*MARIGIN, -1*cm)

    # footer
    canvas.drawString(0, -26.2*cm, "\u00A9 AGOL")
    canvas.drawString(400, -26.5*cm, "SAFETY INSPECTION")
    canvas.line(0, -26.6*cm, WIDTH - 2*MARIGIN, -26.6*cm)


    # # barcode
    # my_code = EAN13(str(order_no).zfill(12), writer=ImageWriter())
    # image = my_code.render()
    # im = ImageReader(image)
    # canvas.drawImage(im, x=0, y=-5*cm, width=150, height=100)

    # paragraphs
    txt_obj = canvas.beginText(14, -1.5* cm)
    txt_obj.setFont("Helvetica", 12)
    txt_obj.setWordSpace(3)
    txt_lst = ["Order Details", 
                "Order no.: " + str(order_no),
                "Truck Reg: " + truck_reg,
                "Truck EPRA no.: " + truck_epra,
                "Transporter:" + truck_trans,                
                # "Warehouse: " + warehouse,
                # f"Date and time of booking: {date} {time}",
                 " ", 
                ]
    for line in txt_lst:
        txt_obj.textOut(line)
        txt_obj.moveCursor(0, 16)
    canvas.drawText(txt_obj)
        
    
    txt_obj = canvas.beginText(350, -2.0* cm)
    # txt_obj.setFont("Helvetica", 12)
    txt_obj.setWordSpace(3)
    txt_lst = [               
                "Trailer Reg: " + trailer_reg,
                "Trailer EPRA no.: " + trailer_epra,
                "Transporter:" + trailer_trans,
                 " ", 
                ]
    for line in txt_lst:
        txt_obj.textOut(line)
        txt_obj.moveCursor(0, 16)
    canvas.drawText(txt_obj)

    # summary table
    # canvas.setFont("Verabd", size=14)
    
    table_data = [['Licenses/Mandatory inspections', 'Certificate Number', 'Expiry'],
                []]
    t = Table(table_data, colWidths=[160, 230, 70], rowHeights=15)
    style = [('BACKGROUND',(0,0),(-1,-2),colors.lightblue),
            ('ALIGN',(0,-1),(-1,-1),'CENTER'),
            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
            ('FONTSIZE', (0,0), (-1,-1), 10),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')]
    t.setStyle(tblstyle=style)
    t.wrapOn(canvas, 10, 10)
    t.drawOn(canvas=canvas, x=12, y=-5.5*cm)

    table_data = [['Immediate corrective action required if any?']]
    t = Table(table_data, colWidths=[460], rowHeights=30.2)
    style = [           
            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
            ('FONTSIZE', (0,0), (-0.25,-0.25), 7),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP')]
    t.setStyle(tblstyle=style)
    t.wrapOn(canvas, 10, 10)
    t.drawOn(canvas=canvas, x=12, y=-6.6*cm)

    table_data = [['DRIVER DETAILS','Y/N'],
                [q1, c1],
                [q2, c2],
                [q3, c3],
                [q4, c4],
                [q1, c1],
                [q2, c2],
                [q3, c3],
                [q4, c4],
                [q1, c1],
                [q2, c2],
                [q3, c3],
                [q4, c4],
                [q1, c1],
                [q2, c2],
                [q3, c3],
                [q4, c4],]
    t = Table(table_data, colWidths=[208, 20], rowHeights=15)
    style = [           
            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
            ('FONTSIZE', (0,0), (-0.25,-0.25), 7),
            ('ALIGN', (1, 0), (-1, 0), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP')]
    t.setStyle(tblstyle=style)
    t.wrapOn(canvas, 10, 10)
    t.drawOn(canvas=canvas, x=12, y=-17*cm)

    table_data = [['DRIVER DETAILS','Y', 'N'],
                ['Insurance PTA Cover'],]
    t = Table(table_data, colWidths=[208, 10,10], rowHeights=15)
    style = [           
            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
            ('FONTSIZE', (0,0), (-0.25,-0.25), 7),
            ('ALIGN', (1, 0), (-1, 0), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP')]
    t.setStyle(tblstyle=style)
    t.wrapOn(canvas, 10, 10)
    t.drawOn(canvas=canvas, x=242, y=-8.6*cm)

    # summary table
    # canvas.setFont("Verabd", size=14)
    # canvas.drawString(0, -10.5*cm, "SUMMARY:")
    # table_data = [['Order no.', 'Trailer', 'Trailer Epra.', 'Pallets pos.', 'Pallets'],
    #             [order_no, trailer_epra, trailer_epra, pallets_pos, pallets]]
    # t = Table(table_data, colWidths=[60, 230, 70, 60, 50], rowHeights=30)
    # style = [('BACKGROUND',(0,0),(-1,-2),colors.lightblue),
    #         ('ALIGN',(0,-1),(-1,-1),'CENTER'),
    #         ('BOX', (0,0), (-1,-1), 0.25, colors.black),
    #         ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
    #         ('FONTSIZE', (0,0), (-1,-1), 10),
    #         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #         ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')]
    # t.setStyle(tblstyle=style)
    # t.wrapOn(canvas, 10, 10)
    # t.drawOn(canvas=canvas, x=12, y=-15*cm)

    canvas.showPage()
    canvas.save()
    return buffer
