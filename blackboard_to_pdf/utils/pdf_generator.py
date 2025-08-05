from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def save_as_pdf(text, output_path):
    doc = SimpleDocTemplate(output_path)
    styles = getSampleStyleSheet()
    flowables = [Paragraph(line, styles["Normal"]) for line in text.split('\n') if line.strip()]
    doc.build(flowables)

