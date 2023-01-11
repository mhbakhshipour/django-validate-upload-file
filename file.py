import magic
from rest_framework import status

from app import settings


def validate_upload_file(this_file):
    if int(this_file.size) > settings.FILE_UPLOAD_MAX_MEMORY_SIZE:
        return {
            "message": f"File size should be under {settings.FILE_UPLOAD_MAX_MEMORY_SIZE}Bytes",
            "code": status.HTTP_400_BAD_REQUEST,
        }

    initial_pos = this_file.tell()
    this_file.seek(0)
    file_mime_type = str(magic.from_buffer(this_file.read(1024), mime=True)).strip()
    this_file.seek(initial_pos)
    file_extention = str(this_file.name).strip().split(".")[-1]
    file_content_type = str(this_file.content_type).strip()
    if (
        file_extention not in settings.FILE_SUPPORTED_EXTENTION
        or file_content_type not in settings.FILE_SUPPORTED_TYPES
        or file_mime_type not in settings.FILE_SUPPORTED_TYPES
    ):
        print(
            f"File type is not supported: {file_extention} - {file_content_type} - {file_mime_type}"
        )
        return {
            "message": "File type is not supported",
            "code": status.HTTP_400_BAD_REQUEST,
        }
    return {
        "message": "Success",
        "code": status.HTTP_200_OK,
    }
