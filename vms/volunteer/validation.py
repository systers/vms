from PyPDF2 import PdfFileReader
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from vms.settings import MEDIA_ROOT
import os.path

def validate_file(my_file):

    MAX_FILENAME_LENGTH = 40
    MAX_FILESIZE_BYTES = 5243000
    VALID_CONTENT_TYPES = [
        "text/plain",
        "application/msword",
        "application/pdf",
        "application/vnd.openxmlformats-"
        "officedocument.wordprocessingml.document",
        "application/vnd.oasis.opendocument.text",
    ]

    is_valid = True

    if len(my_file.name) > MAX_FILENAME_LENGTH:
        is_valid = False
    if my_file.size > MAX_FILESIZE_BYTES:
        is_valid = False
    else:
        if my_file.content_type == "application/pdf":
            path = default_storage.save(my_file.name, ContentFile(my_file.read()))
            path = os.path.join(MEDIA_ROOT, path)
            try:
                PdfFileReader(open(path, 'rb'))
            except Exception as e:
                print("Read failed or invalid: ", e)
                is_valid = False
            default_storage.delete(my_file.name)
    if my_file.content_type not in VALID_CONTENT_TYPES:
        is_valid = False

    return is_valid
