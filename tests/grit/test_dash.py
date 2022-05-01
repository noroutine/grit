import importlib

from grit import *


def test_simple_import():
    importlib.import_module("samples.simple")
    importlib.import_module("samples.simple.folder1")
    pass


def test_dashboard_registration():
    GritDash(title="Dummy")


def test_folder_config():
    Folder(title="Dummy")
