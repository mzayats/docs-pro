# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sys
import yaml
import os

import sphinx_rtd_theme
# -- Project information -----------------------------------------------------

sys.path.append(os.path.abspath('ext'))

project = 'OpenNebula'
copyright = '2018, OpenNebula Systems <contact@opennebula.org>'
author = 'OpenNebula Systems'

site_conf = yaml.load(os.popen('git show origin/one-5.6:source/site_conf.yml'))
versions = site_conf['versions']
downloads = site_conf['downloads']

# Github path
github_repo   = "https://github.com/OpenNebula/docs-pro"
github_branch = "master"


# The short X.Y version
version = '5.6'
# The full version, including alpha/beta/rc tags
release = '5.6.1'

rst_epilog = '.. |version| replace:: %s' % version

#Specific options for generating changelog, please use only single quotes
milestone = 'Release 5.6.1'
link = 'true'
repo = 'one'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx-prompt','versions']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []
html_show_copyright = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_theme_options = {'logo_only': True}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_style = 'css/opennebula.css'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "opennebula-white_addons.png"

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_sidebars = {
    'index': [],
    '**': ['alltoc.html']
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'OpenNebulaExtensionsdoc'

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# -- Options for LaTeX output ------------------------------------------------

latex_logo = "_static/opennebula.png"

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',
'classoptions': ',openany,oneside',
'babel': '\\usepackage[english]{babel}',
'maketitle': '\\maketitle\nThis document is being provided by OpenNebula Systems under the Creative Commons Attribution-NonCommercial-Share Alike License.\\newline{}\\newline{}THE DOCUMENT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE DOCUMENT.'
# Additional stuff for the LaTeX preamble.
}


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'one-addons-' + release + '.tex', 'OpenNebula 5.6-master Enterprise Add-ons Documentation',
   'OpenNebula Systems', 'manual'),
]



# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'opennebula', 'OpenNebula Enterprise Add-ons Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'OpenNebulaExtensions', 'OpenNebula 5.6 Enterprise Add-ons Documentation',
     author, 'OpenNebulaExtensions', 'One line description of project.',
     'Miscellaneous'),
]
