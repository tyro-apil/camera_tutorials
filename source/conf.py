# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_rtd_theme

project = "Robot Perception Tutorials"
copyright = "2024-2025, Robotics Club, Pulchowk Campus"
author = "Apil Chaudhary"
release = "2.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  "sphinx_rtd_theme",
  "sphinx_copybutton",
  "myst_parser",
  "sphinx_tabs.tabs",
  "sphinx.ext.autodoc",
  "sphinx.ext.napoleon",
  # "sphinx.ext.linkcode",
  "sphinx.ext.mathjax",
  "sphinx.ext.extlinks",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "en"

source_suffix = {
  ".rst": "restructuredtext",
  ".md": "markdown",
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
# html_static_path = ["_static"]

html_context = {
  "display_github": True,
  "github_user": "tyro-apil",
  "github_repo": "camera_tutorials",
  "github_version": "main",
  "conf_py_path": "/source/",
}

# Theme options for better appearance
html_theme_options = {
  "navigation_depth": 4,
  "collapse_navigation": False,
  "sticky_navigation": True,
  "includehidden": True,
  "titles_only": False,
}

# -- Options for MyST Parser -------------------------------------------------

myst_enable_extensions = [
  "colon_fence",
  "deflist",
  "linkify",
]
myst_heading_anchors = 3
