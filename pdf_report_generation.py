# %% Importing necessary packages

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, BaseDocTemplate, PageTemplate, Frame, Paragraph, NextPageTemplate, PageBreak
import markdown
from reportlab.pdfgen.canvas import Canvas


# %% PDF Test with doc

# def generate_pdf(data):
#     doc = SimpleDocTemplate("report.pdf", pagesize=letter)
#     styles = getSampleStyleSheet()
#     story = []
#     for item in data:
#         story.append(Paragraph(item, styles["Normal"]))
#     doc.build(story)
# data = ["Hello, world!", "This is a simple PDF report.", "Generated using ReportLab."]
# generate_pdf(data)


# %% Markdown to HTML test


markdown_text = """
# This is a Markdown example

This is a paragraph of text.

**Bold text**

*Italic text*

**Here's a list:**

* Item 1
* Item 2

**And here's a code block:**

```python
def greet(name):
    print("Hello, " + name + "!") """

html = markdown.markdown(markdown_text)
print(html)


# %% RAG retrieval

def extract_text_from_pdfs(pdf_folder):
    documents = []
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            # Assume filename format: CompanyName_Year.pdf
            pdf_name = os.path.splitext(filename)[0]  # Remove .pdf extension
            parts = pdf_name.split('_')
            if len(parts) >= 2:
                company = '_'.join(parts[:-1])
                year = parts[-1]
            else:
                company = pdf_name
                year = 'Unknown'
            pdf_path = os.path.join(pdf_folder, filename)
            with open(pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ''
                for page in reader.pages:
                    text += page.extract_text()
            # Store text with metadata
            doc = {
                'company': company,
                'year': year,
                'text': text
            }
            documents.append(doc)
    return documents


# %% Defining necessary functions

def generate_pdf_report(text_page1,
                        text_page2,
                        text_page3,
                        text_page4,
                        text_page5,
                        text_page6,
                        text_page7,
                        text_page8,
                        text_page9,
                        text_page10,
                        var_pdf_name='test_report.pdf', var_header_text='Sample Header', var_footer_text='Sample Footer',):
    class MyDocTemplate(BaseDocTemplate):
        """Template class for PDF document"""

        def __init__(self, filename, **kwargs):
            super().__init__(filename, **kwargs)
            
            # Define the page frames
            self.frame = Frame(
                inch, inch, self.pagesize[0] - inch * 2, self.pagesize[1] - inch * 2,
                id='normal'
            )

            # Define the styles for header and footer
            self.styles = getSampleStyleSheet()
            self.header_style = self.styles['Heading3']
            self.footer_style = self.styles['Heading5']

            # Define the header and footer frames
            self.header_frame = Frame(
                inch, self.pagesize[1] - 0.5 * inch, self.pagesize[0] - inch, 0.5 * inch,
                id='header'
            )
            self.footer_frame = Frame(
                inch, 0.25 * inch, self.pagesize[0] - inch, 0.5 * inch,
                id='footer'
            )

            # Define the PageTemplate
            self.addPageTemplates([
                PageTemplate(
                    id='FirstPage',
                    frames=[self.frame, self.header_frame, self.footer_frame],
                    onPage=self._header_footer,
                    onPageEnd=self._footer
                )
            ])

        def _header_footer(self, canvas, doc):
            # Draw the header
            self.header_style.alignment = 0  # center align the header text
            header_text = Paragraph(var_header_text, self.header_style)
            header_text.wrapOn(canvas, self.header_frame.width, self.header_frame.height)
            header_text.drawOn(canvas, self.header_frame.x1, self.header_frame.y1)

        def _footer(self, canvas, doc):
            # Draw the footer

            self.footer_style.alignment = 0  # center align the footer text
            footer_text = Paragraph(var_footer_text, self.footer_style)
            footer_text.wrapOn(canvas, self.footer_frame.width, self.footer_frame.height)
            footer_text.drawOn(canvas, self.footer_frame.x1, self.footer_frame.y1)

    # Create a new PDF document using the template
    pdf_doc = MyDocTemplate(var_pdf_name)

    # Add the content to the PDF document
    elements = [
                Paragraph(text_page1), 
                PageBreak(), 
                Paragraph(text_page2),
                PageBreak(),
                Paragraph(''),
                Paragraph(text_page3),
                PageBreak(),
                Paragraph(text_page4),
                PageBreak(),
                Paragraph(text_page5),
                PageBreak(),
                Paragraph(text_page6),
                PageBreak(),
                Paragraph(text_page7),
                PageBreak(),
                Paragraph(text_page8),
                PageBreak(),
                Paragraph(text_page9),
                PageBreak(),
                Paragraph(text_page10),
                PageBreak()]

    pdf_doc.build(elements)


# %%  ReportLab - Generate report
generate_pdf_report('A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B')

# %%
