from os import path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4 # Only A4 is supported in vertial mode
from reportlab.lib.colors import Color

# Registrar fontes que serão usadas (mandarim): --------
font_name = 'mandarim'
font_path = 'Fonts/NotoSerifCJKsc-Regular.ttf'
font_size = 24
pdfmetrics.registerFont(TTFont(font_name, font_path))
# ------------------------------------------------------



# Configurações de leyout ------------------------------
file_name   = 'model.pdf'
rect_size   = 60                        #pontos
left_margin = 10                        #pontos
top_margin  = rect_size + left_margin   #pontos
# ------------------------------------------------------


def text_height() -> float:
    face = pdfmetrics.getFont(font_name).face
    string_height = (face.ascent - face.descent) / 1000 * font_size
    return string_height
        
def mp(mm: float) -> float:
    return mm / 0.3522777

def mm(mp: float) -> float:
    return mp * 0.3522777

def calculate_table_size(left_offset: float, top_offset: float) -> tuple[int, int]:
    col = (mp(210) - left_offset) / rect_size
    row = (mp(297) - top_offset) / rect_size
    return int(col), int(row)

def get_margin_offset(colCount: int, rowCount: int) -> tuple[float, float]:
    xOffset = (mp(210) - (colCount * rect_size)) / 2
    yOffset = (mp(297) - (rowCount * rect_size)) / 2
    return xOffset, yOffset

def generate_pdf(character: str) -> None:
    if path.exists(font_path) == False:
        raise Exception(f"Fonte {font_name} não encontrada no local '{font_path}'")

    cnv = canvas.Canvas(filename=f"({character}) " + file_name, pagesize=A4)
    cnv.setFont(font_name, font_size)

    #criar tabela de A x B (A = B).
    table_size = calculate_table_size(0, top_margin)
    yCord = mp(297)
    abs_size = rect_size
    pos_offset = get_margin_offset(table_size[0], table_size[1]) # It dint work with this offset... Why?
    charecter_size_w = cnv.stringWidth(character, font_name, font_size)
    charecter_size_h = text_height()
    cnv.setFillColorRGB(0, 0, 0, .6)

    for i in range(table_size[1]):
        for j in range(table_size[0]):
            xPos = left_margin + j * abs_size
            yPos = yCord - (top_margin + i * abs_size)

            # Linhas de guia
            cnv.setStrokeColor(aColor=Color(0,0,1,1), alpha=.1)
            cnv.line(xPos, yPos + rect_size / 2, xPos + rect_size, yPos + rect_size / 2)
            cnv.line(xPos + (rect_size / 2), yPos, xPos + (rect_size / 2), yPos + rect_size)

            # Região do retângulo
            cnv.setStrokeColor(aColor=Color(0,0,1,1), alpha=1)
            cnv.rect(xPos, yPos, abs_size, abs_size, stroke=1, fill=0)

            # Desenhar o caractere         
            cnv.drawString(xPos + (rect_size / 2) - (charecter_size_w / 2), yPos + (rect_size / 2) - (charecter_size_h / 3), character)

    cnv.save()
    print('Arquivo gerado com sucesso')

generate_pdf('不')

