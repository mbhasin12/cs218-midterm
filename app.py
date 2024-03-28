from flask import Flask, request, jsonify
import boto3
from werkzeug.utils import secure_filename
import os
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/upload": {"origins": "*"}})


AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
S3_BUCKET_NAME = 'take-home-exam-bucket'

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'no file included'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'})

    filename = str(random.randint(10000, 99999)) + "_" + secure_filename(file.filename) 
    try:
        s3.upload_fileobj(file, S3_BUCKET_NAME, filename)
        return jsonify({'message': f'File uploaded successfully'})
    except Exception as e:
        return jsonify({'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5005)