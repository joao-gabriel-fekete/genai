from time import sleep

from flask import Flask, request, jsonify
from genaiintegration import generateSummary
from werkzeug.utils import secure_filename
import os
from transcriber import convertAudioToText

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():
    # Check if the file part is in the POST request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    # If the user does not select a file, the browser submits an empty part without a filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = secure_filename(file.filename)
        save_path = os.path.join('./', filename)
        file.save(save_path)
        # return jsonify({'message': 'File uploaded successfully', 'path': save_path}), 200
        sleep(3)
        textToSummarize = convertAudioToText(save_path)
        return generateSummary(textToSummarize)

if __name__ == '__main__':
    app.run(port=8080)