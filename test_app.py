from werkzeug.datastructures import FileStorage
import os

def test_no_file(client):
    response = client.post('/upload')
    data = response.json
    assert data['message'] == 'no file included'
   

def test_working_file(client):
    file_path = 'demo_sc.png'

    with open(file_path, 'rb') as f:
        
        file_storage = FileStorage(stream=f, filename=os.path.basename(file_path), content_type='img/png')
        
        data = {
            'file': file_storage  
        }
        
        response = client.post('/upload', content_type='multipart/form-data', data=data)
        data = response.json
        message = data['message']
        assert message == 'File uploaded successfully'