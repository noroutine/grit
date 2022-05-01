
import inspect
import sys
from pydantic import BaseModel

FOLDER_MAGIC_STR = '__folder__'


class Folder(BaseModel):
    title: str

    def __init__(self, **data):
        super().__init__(**data)
        caller = inspect.currentframe().f_back
        caller_module = sys.modules[caller.f_globals['__name__']]
        setattr(caller_module, FOLDER_MAGIC_STR, self)
