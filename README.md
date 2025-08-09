# Conversor a PDF

Script de línea de comandos para convertir archivos de texto (`.txt`, `.md`) e imágenes (`.png`, `.jpg`, `.jpeg`) a formato PDF.

## Requisitos
- Python 3
- [fpdf2](https://pypi.org/project/fpdf2/)
- [Pillow](https://pypi.org/project/Pillow/)
- [img2pdf](https://pypi.org/project/img2pdf/)

Instalación de dependencias:
```bash
pip install fpdf2 Pillow img2pdf
```

## Uso
```bash
python convert_to_pdf.py archivo.txt salida.pdf
```
Si no se indica el archivo de salida, se utilizará el mismo nombre que la entrada con extensión `.pdf`.

## Limitaciones
El script soporta únicamente archivos de texto plano e imágenes. Para otros tipos de archivos será necesario ampliar la funcionalidad.
