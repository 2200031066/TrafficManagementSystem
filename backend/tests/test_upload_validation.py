import pytest
import io
import json
import os
import sys

# Add backend to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    # Disable actual file saving for tests to keep it clean
    app.config['UPLOAD_FOLDER'] = '/tmp/test_uploads'
    with app.test_client() as client:
        yield client

def test_upload_wrong_count(client):
    """Test uploading fewer than 4 files."""
    data = {
        'videos': [
            (io.BytesIO(b"fake video content"), 'vid1.mp4'),
            (io.BytesIO(b"fake video content"), 'vid2.mp4')
        ]
    }
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 400
    json_data = json.loads(response.data)
    assert "Wrong number of files" in json_data['detail']

def test_upload_invalid_extension(client):
    """Test uploading files with invalid extensions (e.g., .txt)."""
    data = {
        'videos': [
            (io.BytesIO(b"text content"), 'test.txt'),
            (io.BytesIO(b"text content"), 'test.txt'),
            (io.BytesIO(b"text content"), 'test.txt'),
            (io.BytesIO(b"text content"), 'test.txt')
        ]
    }
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 400
    json_data = json.loads(response.data)
    assert "Invalid video format" in json_data['error']

def test_upload_no_files(client):
    """Test uploading with no files."""
    response = client.post('/upload', data={}, content_type='multipart/form-data')
    # Depending on how flask handles empty lists, it often returns 400 or the custom check fails
    assert response.status_code == 400
