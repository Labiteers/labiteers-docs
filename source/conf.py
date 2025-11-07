# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Labiteers'
copyright = '2025 Labiteers'
author = 'Nicholas Doropoulos'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = 'Labiteers User Guide'
html_theme = 'insipid'
html_use_index = False
html_static_path = ['_static']
html_theme_options = {
    'sidebarwidth': 220,  # pixels
}

html_css_files = [
    'custom.css',
]

# Custom sidebar logo 
html_sidebars = {
    "**": [
        "sidebarlogo.html",     # your clickable logo
        "globaltoc.html",       # main docs navigation tree (the full TOC)
        "localtoc.html",        # in-page headings
        "searchbox.html"        # search field
    ]
}

# Dynamic release version based on Git commit count
import subprocess
try:
    commit_count = subprocess.check_output(
        ["git", "rev-list", "--count", "HEAD"], universal_newlines=True
    ).strip()
    release = f"1.0.{commit_count}"
except Exception:
    release = "1.0.0"