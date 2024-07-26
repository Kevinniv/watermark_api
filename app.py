import os
from flask import Flask, request, jsonify, send_file
from watermark import add_watermark

app = Flask(__name__)

@app.route('/add_watermark', methods=['POST'])
def add_watermark_route():
    if 'image' not in request.files or 'text' not in request.form:
        return jsonify({'error': 'No image file or text provided'}), 400
    
    image = request.files['image']
    text = request.form['text']
    input_path = 'input.jpg'
    output_path = 'output.jpg'
    image.save(input_path)
    add_watermark(input_path, text, output_path)
    
    return send_file(output_path, mimetype='image/jpeg', as_attachment=True, attachment_filename='output.jpg')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
