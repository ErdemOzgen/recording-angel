"""Sphinx configuration."""
project = "Recording Angel"
author = "Erdem Ozgen"
copyright = "2023, Erdem Ozgen"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
