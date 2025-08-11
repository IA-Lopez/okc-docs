# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OIPS Docs'  # This is like "My Docs" in your other project
copyright = '2025, ks_karem7'  # Matches the copyright in your screenshot
author = ' ks_karem7 '
release = '1.0'  # Simple version for your PoC

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []  # Keep empty for basic setup—no complex features needed

templates_path = ['_templates']
exclude_patterns = []

language = 'en'  # This enables /en/latest/ path

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # Matches "theme provided by Read the Docs"
html_static_path = ['_static']  # Leave this; for any images/CSS if you add later
