# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_rtd_theme

project = 'Camera Tutorials'
copyright = '2024, Apil Chaudhary'
author = 'Apil Chaudhary'
# release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  "sphinx_rtd_theme",
  "sphinx_copybutton"
]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_context = {
  "display_github": True,
  "github_user": "tyro-apil",
  "github_repo": "camera_tutorials",
  "github_version": "main",
  "conf_py_path": "/source/",
}

source_suffix = {
  '.rst': 'restructuredtext',
  '.txt': 'markdown',
  '.md': 'markdown',
}
