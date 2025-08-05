from flask import Flask, render_template, request, send_file
import os
from utils.ocr_processor import extract_text
from utils.pdf_generator import save_as_pdf
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'output'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No file uploaded.", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file.", 400

    filename = datetime.now().strftime("%Y%m%d%H%M%S") + "_" + file.filename
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(image_path)

    # Extract text and save PDF
    extracted_text = extract_text(image_path)
    output_pdf_path = os.path.join(OUTPUT_FOLDER, filename.rsplit('.', 1)[0] + '.pdf')
    save_as_pdf(extracted_text, output_pdf_path)

    return send_file(output_pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

