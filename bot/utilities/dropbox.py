import os
import time
import datetime
import contextlib

import dropbox

os.environ["DROPBOX"] = input('Dropbox: ')
dbx = dropbox.Dropbox(os.getenv('DROPBOX'))

@contextlib.contextmanager
def stopwatch(message):
    """Context manager to print how long a block of code took."""
    t0 = time.time()
    try:
        yield
    finally:
        t1 = time.time()
        print('Total elapsed time for %s: %.3f' % (message, t1 - t0))

def download(path):
    """Download a file.
    Return the bytes of the file, or None if it doesn't exist.
    """
    path = path
    while '//' in path:
        path = path.replace('//', '/')
    with stopwatch('download'):
        try:
            md, res = dbx.files_download(path)
        except dropbox.exceptions.HttpError as err:
            print('*** HTTP error', err)
            return None
    data = res.content
    # print(len(data), 'bytes; md:', md)
    return data

def upload(file_upload, path, overwrite=True):
    """Upload a file.
    Return the request response, or None in case of error.
    """
    path = path
    while '//' in path:
        path = path.replace('//', '/')
    mode = (dropbox.files.WriteMode.overwrite
            if overwrite
            else dropbox.files.WriteMode.add)
    mtime = os.path.getmtime(file_upload)
    with open(file_upload, 'rb') as f:
        data = f.read()
    with stopwatch('upload %d bytes' % len(data)):
        try:
            res = dbx.files_upload(
                data, path, mode,
                client_modified=datetime.datetime(*time.gmtime(mtime)[:6]),
                mute=True)
        except dropbox.exceptions.ApiError as err:
            print('*** API error', err)
            return None
    # print('uploaded as', res.name.encode('utf8'))
    return res
