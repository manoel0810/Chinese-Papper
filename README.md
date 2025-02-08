### Criar páginas para o estudo/prática da escrita dos ideogramas do mandarim.

### How to use:
1. Download the reportlab:
   ```bash
    pip install reportlab
   ```
2. Choose your ideogram
3. Set your ideogram on program main intrance
   ```python
   generate_pdf('不') # More than one is possible. Adjust as you feel better
   ```
4. Define other properties, such as rectangle size, font size, font style using the settings properties:
   ```python
   # Registrar fontes que serão usadas (mandarim): --------
   font_name = 'mandarim'
   font_path = 'Fonts/NotoSerifCJKsc-Regular.ttf'
   font_size = 24
   pdfmetrics.registerFont(TTFont(font_name, font_path)) # you should not modify this line ;)
   # ------------------------------------------------------

   # Configurações de leyout ------------------------------
   file_name   = 'model.pdf'
   rect_size   = 60                        #dots
   left_margin = 10                        #dots
   top_margin  = rect_size + left_margin   #dots
   # ------------------------------------------------------
   ```
5. Execute the python file

#### Warning 🐞: Maybe (I've sure) there some bugs that I might ain't fix. In especial with the page margin calcules :)
