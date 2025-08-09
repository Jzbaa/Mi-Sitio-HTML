#!/usr/bin/env python3
"""Convierte archivos de texto o imagen a PDF."""
from __future__ import annotations

import argparse
from pathlib import Path


def convert_text_to_pdf(entrada: Path, salida: Path) -> None:
    """Convierte un archivo de texto a PDF."""
    try:
        from fpdf import FPDF  # type: ignore
    except ImportError as exc:  # pragma: no cover - librería externa
        raise SystemExit(
            "La librería 'fpdf2' es necesaria para convertir archivos de texto"
        ) from exc

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    with entrada.open("r", encoding="utf-8") as fh:
        for linea in fh:
            pdf.multi_cell(0, 10, linea)

    pdf.output(str(salida))


def convert_image_to_pdf(entrada: Path, salida: Path) -> None:
    """Convierte una imagen a PDF."""
    try:
        from PIL import Image  # type: ignore
        import img2pdf  # type: ignore
    except ImportError as exc:  # pragma: no cover - librerías externas
        raise SystemExit(
            "Las librerías 'Pillow' e 'img2pdf' son necesarias para convertir imágenes"
        ) from exc

    # Abrimos la imagen para asegurarnos de que es válida
    with Image.open(entrada) as img:
        pdf_bytes = img2pdf.convert(img.filename)

    salida.write_bytes(pdf_bytes)


def main() -> None:
    parser = argparse.ArgumentParser(description="Convierte archivos a PDF")
    parser.add_argument("entrada", help="Ruta del archivo a convertir")
    parser.add_argument(
        "salida",
        nargs="?",
        help="Ruta del PDF de salida (por defecto usa el mismo nombre que la entrada)"
    )
    args = parser.parse_args()

    entrada = Path(args.entrada)
    if not entrada.exists():
        parser.error("El archivo de entrada no existe")

    salida = Path(args.salida) if args.salida else entrada.with_suffix(".pdf")

    extension = entrada.suffix.lower()
    if extension in {".txt", ".md"}:
        convert_text_to_pdf(entrada, salida)
    elif extension in {".png", ".jpg", ".jpeg"}:
        convert_image_to_pdf(entrada, salida)
    else:
        parser.error(f"Tipo de archivo no soportado: {extension}")

    print(f"Convertido {entrada} -> {salida}")


if __name__ == "__main__":
    main()
