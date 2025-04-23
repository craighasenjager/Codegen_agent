
from fpdf import FPDF
import os

def create_pdf(filename, title, content):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, title, ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 10, content)
        pdf.output(filename)
        print(f"PDF '{filename}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the PDF: {e}")

def get_essay_content():
    try:
        content = (
            "Birds are a group of warm-blooded vertebrates constituting the class Aves, "
            "characterized by feathers, toothless beaked jaws, the laying of hard-shelled eggs, "
            "a high metabolic rate, a four-chambered heart, and a strong yet lightweight skeleton.\n\n"
            "Birds live worldwide and range in size from the 5 cm (2 in) bee hummingbird to the 2.75 m (9 ft) ostrich. "
            "There are about ten thousand living species, more than half of which are passerine, or 'perching' birds.\n\n"
            "Birds have adapted to various habitats, from the Arctic to the Antarctic. They are found in forests, grasslands, "
            "deserts, and urban areas. Birds play significant roles in the ecosystem, such as pollination, seed dispersal, "
            "and pest control. They are also indicators of environmental health and contribute to biodiversity.\n\n"
            "The importance of birds to the ecosystem cannot be overstated. They help in maintaining the balance of nature, "
            "and their presence is crucial for the survival of many other species. Conservation efforts are essential to protect "
            "bird habitats and ensure their survival for future generations."
        )
        return content
    except Exception as e:
        print(f"An error occurred while generating the essay content: {e}")
        return ""

def main():
    try:
        filename = "Birds_Essay.pdf"
        title = "The Fascinating World of Birds"
        content = get_essay_content()
        if content:
            create_pdf(filename, title, content)
        else:
            print("Failed to generate essay content.")
    except Exception as e:
        print(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
