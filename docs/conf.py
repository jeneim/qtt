#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# qtt documentation build configuration file, created by
# sphinx-quickstart on Sat Feb  3 15:16:09 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
#    'nbsphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.autosummary',
    'nbsphinx']

extensions += ['sphinx_automodapi.automodapi']

if 0:
    extensions += ['autoapi.extension']
    
    # Document Python Code
    autoapi_type = 'python'
    autoapi_dirs = '../qtt'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


nbsphinx_execute = 'never'

import os
rtd = os.environ.get('READTHEDOCS', False)
print('READTHEDOCS env %s' % (rtd, ))

if rtd:
    # since tkinter seems to be unavailable on rtd
    autodoc_mock_imports = ['_tkinter']
    autodoc_mock_imports += ['Polygon3', 'Polygon']

    import sys
    from unittest.mock import MagicMock

    class Mock(MagicMock):

        @classmethod
        def __getattr__(cls, name):
            if name == '__version__':
                return '3.0.8'
            return MagicMock()

    MOCK_MODULES = ['Polygon']
    sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#

source_suffix = ['.rst', '.md'] # need package recommonmark
#source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'qtt'
copyright = '2018, Pieter Eendebak'
author = 'Pieter Eendebak'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

import re
def get_version(verbose=1, filename='qtt/version.py'):
    """ Extract version information from source code """

    with open(filename, 'r') as f:
        ln = f.readline()
        m = re.search('.* ''(.*)''', ln)
        version = (m.group(1)).strip('\'')
    if verbose:
        print('get_version: %s' % version)
    return version


# The short X.Y version.
if 0:    
    import qtt
    version = '{}'.format(qtt.__version__)
else:
    version = get_version(verbose=1, filename='../qtt/version.py')
    
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', 'legacy.py', '.DS_Store', 'untitled.*py',
                'notebooks/.ipynb_checkpoints', '../qtt/loggingGUI.py', '../qtt/debug.py', '../qtt/legacy.py',  'qtt/scans.py', '../qtt/deprecated/*']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
html_theme = 'classic'
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

"""
# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars

html_sidebars = {
    '**': [
        #'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}
"""

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'qttdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'qtt.tex', 'qtt Documentation',
     'Pieter Eendebak', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'qtt', 'qtt Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'qtt', 'qtt Documentation',
     author, 'qtt', 'Toolbox for quantum dot measurements and analysis.',
     'Miscellaneous'),
]



intersphinx_mapping = {
    'matplotlib': ('http://matplotlib.org/', None),
    'python': ('https://docs.python.org/3.6', None),
    'numpy': ('https://docs.scipy.org/doc/numpy', None)
}

if rtd:
    import matplotlib
    matplotlib.use('agg')

    # check packages
    import importlib
    
    modules=['skimage', 'matplotlib', 'cv2', 'PyQt5', 'pyqtgraph', 'qtpy', 'qcodes', 'qtt']
    for module_name in modules:
        print('loading module %s' % module_name)
        m=importlib.import_module(module_name)
        try:
            print('  __version__: %s' % m.__version__)                
        except:
            pass

if 1:
    def run_apidoc(_):
        import os
        print('run_apidoc: current dir is %s' % os.getcwd())
        import numpy; print('numpy.__version__ %s' % (numpy.__version__) )
    
        ignore_paths = [
            'qtt/legacy.py', 'qtt/debug.py', 'qtt/reports.py', 'qtt.loggingGUI.py',
            '../qtt/legacy.py', '../qtt/debug.py', '../qtt/reports.py', '../qtt/loggingGUI.py', '../qtt/scans.py',
            '../qtt/deprecated/.*.py', '../qtt/deprecated/tunnelbarrier.py','../qtt/algorithms/untitled*.py',
            'untitled*.py', 'setup.py',
        ]
    
        argv = [
            "-f",
            "-M",
            "-o", ".",
            "../qtt"
        ] + ignore_paths
    
        # Sphinx 1.7+
        from sphinx.ext import apidoc
        apidoc.main(argv)
        print('run_apidoc: done')
    


    def setup(app):
        app.connect('builder-inited', run_apidoc)        