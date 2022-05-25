from cgi import FieldStorage
from typing import Any

import boto3
from decouple import config
from werkzeug.datastructures import FileStorage


class FileService:
    client: Any

    @staticmethod
    def upload_file(file):
        s3_bucket = config('S3_BUCKET')
        if s3_bucket is None or len(s3_bucket) == '':
            raise ValueError('S3_BUCKET not defined!')

        # We have to create the client before overloading file methods
        client = FileService.get_client()

        import os
        original_getsize = os.path.getsize
        import builtins as bt
        original_open = bt.open

        if isinstance(file, FileStorage):
            file_name = file.filename
            file_size = os.fstat(file.fileno()).st_size
            file = file._file

        else:
            file_name = file.name
            file_size = file.size

        key = f'photos/{file_name}'

        try:
            def getsize_override(*_args, **_kwargs):
                return file_size

            def open_override(*_args, **_kwargs):
                return file

            os.path.getsize = getsize_override
            bt.open = open_override

            client.upload_file(Filename=file_name, Bucket=s3_bucket, Key=key)
        finally:
            os.path.getsize = original_getsize
            bt.open = original_open

        return f'https://{s3_bucket}.s3.sa-east-1.amazonaws.com/{key}'

    @staticmethod
    def get_client():
        if getattr(FileService, 'client', None) is None:
            setattr(FileService, 'client', boto3.client('s3'))

        return FileService.client
