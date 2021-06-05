#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pathlib import Path
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import StyleSheet1, getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus.tables import TableStyle
from reportlab.rl_config import defaultPageSize
from .numbersentence import AdditionSentence
from .nsgenerator import NSGenerator


def onPage(canvas: canvas.Canvas, doc):
    page_width, page_height = A4
    canvas.saveState()
    canvas.setStrokeColor(colors.black)
    canvas.setDash(6, 3)
    canvas.line(0.5*inch, page_height/2, page_width-0.5*inch, page_height/2)
    canvas.restoreState()


def savePDF(filename, nses):
    title = '每日一练'
    subtitle = '''
    姓名：<u>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</u>
    日期：<u>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</u>
    '''
    PAGE_WIDTH = A4[0]

    pdfmetrics.registerFont(TTFont('FZKT', 'fonts/FangZhengKaiTi.ttf'))
    pdfmetrics.registerFont(TTFont('CMU', 'fonts/cm-unicode-0.7.0/cmunbx.ttf'))

    styles = StyleSheet1()
    styles.add(ParagraphStyle(
        name='title',
        fontName='FZKT',
        fontSize=35,
        leading=0,
        alignment=1,
        spaceAfter=6)
    )
    styles.add(ParagraphStyle(
        name='subtitle',
        fontName='FZKT',
        fontSize=25,
        leading=30,
        alignment=2,
        spaceAfter=6)
    )

    doc = SimpleDocTemplate(filename,
                            pagesize=A4,
                            topMargin=20,
                            bottomMargin=20)
    Story = []

    for i in range(len(nses)):
        Story.append(Paragraph(title, style=styles['title']))
        Story.append(Spacer(1, 0.8*inch))
        Story.append(Paragraph(subtitle, style=styles['subtitle']))
        Story.append(Spacer(1, 0.8*inch))

        tableStyle = TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONT', (0, 0), (-1, -1), 'CMU', 18),
            ('ALIGNMENT', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ])
        table = Table(nses[i],
                      colWidths=(PAGE_WIDTH-inch) / len(nses[i][0]),
                      rowHeights=32,
                      style=tableStyle)
        Story.append(table)
        if i < len(nses)-1:
            Story.append(Spacer(1, 1.5*inch))

    doc.build(Story, onFirstPage=onPage, onLaterPages=onPage)


def main():
    nses = []
    for _ in range(2):
        nsgen = NSGenerator(AdditionSentence, cols=2, max=5)
        ns = nsgen.gen()
        nses.append(ns)

    filename = '每日一练-{:%Y-%m-%dT%H%M%S}.pdf'.format(datetime.now())
    outFile = Path.cwd() / 'out' / filename
    savePDF(str(outFile), nses)


if __name__ == '__main__':
    main()
