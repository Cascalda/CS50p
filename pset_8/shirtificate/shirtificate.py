"""Orientate shirtificate.png."""
from fpdf import FPDF

IMAGE_PATH = "./shirtificate.png"
PDF_PATH = "./shirtificate.pdf"
PDF_TEXT = "CS50 Shirtificate"

SHIRT_X = 10
SHIRT_Y = 80
SHIRT_W = 190
SHIRT_H = 180

SHIRT_TEXT = "Cascalda took CS50"
SHIRT_TEXT_W = 0
SHIRT_TEXT_H = 180


class MyPDF(FPDF):
    """A class that inherits from FPDF."""

    def header(self):
        """Sets the header of the pdf."""
        self.ln(25)
        self.set_font(family='Arial', size=55)
        self.cell(w=0, txt=PDF_TEXT, align='C')
        self.ln(15)

    def add_shirt(self):
        """Add the shirt image."""
        self.image(name=IMAGE_PATH, x=SHIRT_X, y=SHIRT_Y,
                   w=SHIRT_W, h=SHIRT_H, type='PNG')

    def add_shirtificate_slogan(self):
        """Adds the certificate of completion slogan on the shirt."""
        self.set_font(family='Arial', size=30)
        self.set_text_color(255, 255, 255)
        self.cell(w=SHIRT_TEXT_W, h=SHIRT_TEXT_H, txt=SHIRT_TEXT, align="C")


def main():
    """Interface that controls all other functions."""
    pdf = MyPDF(orientation='portrait', format='a4')
    pdf.add_page()
    pdf.add_shirt()
    pdf.add_shirtificate_slogan()
    pdf.output(PDF_PATH)


if __name__ == "__main__":
    main()
