from flask import Flask, request, jsonify
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
    
    return jsonify({'message': 'Watermark added', 'output_path': output_path})

if __name__ == '__main__':
    app.run(debug=True)
