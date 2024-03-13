# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Gurobi Optimizer Reference Manual'
copyright = '2023, Gurobi Optimization'
author = 'Gurobi Optimization'

html_title = "Optimizer Reference Manual - Gurobi Optimization"
html_favicon = "_static/favicon.ico"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os, sys

sys.path.append(os.path.abspath("./ext"))

extensions = [
    "dotnetdomain",
    "javadomain",
    "matlabdomain",
    "rdomain",
    "sphinx.ext.intersphinx",
    "sphinx_tabs.tabs",
    "sphinx_search.extension",
    "sphinx_design",
]

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
html_theme_options = {
    "light_logo": "gurobi_light.svg",
    "dark_logo": "gurobi_dark.svg",
    "light_css_variables": {
        "color-brand-primary": "#DD2113",
        "color-brand-content": "#DD2113",
        "font-size-normal": "50%",
    },
    "dark_css_variables": {
        "color-brand-primary": "#DD2113",
        "color-brand-content": "#DD2113",
    },
    "sidebar_hide_name": True,
}
html_css_files = [
    'custom.css',
]

# -- Options for LaTeX pdf output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_logo = "_static/gurobi_whitebg.png"

# -- Intersphinx mappings ----------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    # TODO sharing tokens are only needed while our RTD deployments are private
    # Note: this should point to the same grbrs *version* as the optimizer version
    # covered by this branch
    "grbrs": (
        "https://D5bzs14LEezCXIC9R8iUi0By9Mhf5yQm:@docs.gurobi.com/projects/remoteservices/en/stable",
        None,
    ),
    "examples": (
        "https://ZqtknhTe2Y5WdM8CXEeT8TZOc4vudlFP:@docs.gurobi.com/projects/examples/en/stable",
        None,
    ),
}

# -- Link checker ------------------------------------------------------------

linkcheck_ignore = [
    # Redirects to zendesk which returns 403 forbidden. Not ideal, but ultimately
    # not a problem since the page can be accessed without a zendesk login.
    "https://support.gurobi.com",
    "https://www.gurobi.com/getting-started",
]

# Anchor checks currently fail on correctly resolved intersphinx links to the
# remoteservices docs. It may be just due to privacy settings.
# TODO check and re-enable later?
linkcheck_anchors = False

# -- Translations ------------------------------------------------------------

locale_dirs = ["locales"]

# Exclude all files from the build which are included inline
exclude_patterns = [
    "common.rst",
    "common/*.rst",
    "reference/misc/params.rst",
    "reference/misc/attrs.rst",
]

# -- Prologue/epilogue

# Not-fit-to-fly-yet warning
rst_prolog = """
.. warning::

   This documentation site is still under construction. It may contain errors
   and omissions. Please visit
   `gurobi.com/documentation <https://www.gurobi.com/documentation>`_ for the
   official documentation of Gurobi.

"""

# Include file of subsitition directives in all pages
rst_epilog = """
.. include:: /common.rst
"""
