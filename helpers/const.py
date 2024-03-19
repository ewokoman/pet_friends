from pathlib import Path
import os


# Пути к директориям
PROJECT_DIR = Path(__file__).parent.parent
TEST_DATA = os.path.join(PROJECT_DIR, 'test_data')
UPLOAD_FILES = os.path.join(TEST_DATA, 'upload_files')