import importlib
import pytest


def test_adapter_importable():
    mod = importlib.import_module('adapter')
    assert hasattr(mod, 'load_ptseries')
    assert hasattr(mod, 'convert_file')
