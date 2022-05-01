from modulefinder import Module
from attrs import define

import importlib
import pkgutil

from grit.variation import Variation

@define
class Grit:

    @classmethod
    def inspect(cls, module: str) -> dict:
        grit_module = importlib.import_module(module)
        return {
            "name": grit_module.__name__,
            "folders": list(map(lambda m: m.name, pkgutil.iter_modules(grit_module.__path__))),
            "variations": Variation.find_variations_simple(grit_module)
        }