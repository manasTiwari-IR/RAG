import os
import tempfile
from llama_index.core import SimpleDirectoryReader

def load_data_from_user(data):
    # data is a Streamlit UploadedFile object; SimpleDirectoryReader needs a file path
    suffix = os.path.splitext(data.name)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        tmp_file.write(data.getvalue())
        tmp_path = tmp_file.name
    try:
        documents = SimpleDirectoryReader(input_files=[tmp_path]).load_data()
    finally:
        os.unlink(tmp_path)
    return documents