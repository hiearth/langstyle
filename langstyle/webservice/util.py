
import os

def get_file_suffix(file_path):
    if file_path:
        file_extension = os.path.splitext(file_path)[-1]
        return file_extension[1:].lower()

def get_file_name(file_path):
    if file_path:
        file_name = os.path.split(file_path)[-1]
        return os.path.splitext(file_name)[0]

def get_file_size(file_path):
    return os.stat(file_path).st_size

def get_path_tail(path):
    return os.path.split(path)[1]


class HttpUtil:

    _content_types = {"txt": "text/plain",
                      "html":"text/html;charset=utf-8",
                      "htm":"text/html;charset=utf-8",
                      "xml":"text/xml; charset=utf-8",
                      "png": "image/png",
                      "jpg": "image/jpeg",
                      "gif": "image/gif",
                      "js":"application/x-javascript",
                      "css":"text/css",
                      "mp3":"audio/mpeg",
                      "mp4":"audio/mp4",
                      "webm":"audio/webm",
                      "wav":"audio/vnd.wave",
                      "json":"application/json; charset=utf-8"
                      }

    @classmethod
    def get_content_type(cls, file_extension):
        return cls._content_types.get(file_extension)
