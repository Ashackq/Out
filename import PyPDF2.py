import PyPDF2


def merge_pdfs(pdf_list, output):
    # Create a PDF merger object
    pdf_merger = PyPDF2.PdfMerger()

    # Loop through all PDFs and append them to the merger object
    for pdf in pdf_list:
        with open(pdf, "rb") as f:
            pdf_merger.append(f)

    # Write out the merged PDF to a new file
    with open(output, "wb") as f_out:
        pdf_merger.write(f_out)


# List of PDFs you want to merge
pdfs = ["Assignment 1 _Pc-46.pdf", "a1.pdf"]

# Output file
output_pdf = "Assignment 1 _Pc-46m.pdf"

# Merge the PDFs
merge_pdfs(pdfs, output_pdf)
