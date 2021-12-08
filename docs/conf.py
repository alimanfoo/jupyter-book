###############################################################################
# Auto-generated by `jupyter-book config`
# If you wish to continue using _config.yml, make edits to that file and
# re-generate this one.
###############################################################################
author = 'The Jupyter Book Community'
bibtex_bibfiles = ['references.bib']
bibtex_reference_style = 'author_year'
comments_config = {'hypothesis': False, 'utterances': False}
copyright = '2021'
exclude_patterns = ['**.ipynb_checkpoints', '.DS_Store', 'Thumbs.db', '_build', 'file-types/include-rst.rst']
execution_allow_errors = False
execution_excludepatterns = []
execution_in_temp = False
execution_timeout = 30
extensions = ['sphinx_togglebutton', 'sphinx_copybutton', 'myst_nb', 'jupyter_book', 'sphinx_thebe', 'sphinx_comments', 'sphinx_external_toc', 'sphinx.ext.intersphinx', 'sphinx_panels', 'sphinx_book_theme', 'sphinx_click.ext', 'sphinx_inline_tabs', 'sphinxext.rediraffe', 'sphinx_proof', 'sphinxcontrib.bibtex', 'sphinx_jupyterbook_latex']
external_toc_exclude_missing = False
external_toc_path = '_toc.yml'
html_baseurl = 'https://jupyterbook.org/'
html_extra_path = ['images/badge.svg']
html_favicon = 'images/favicon.ico'
html_logo = 'images/logo-wide.svg'
html_sourcelink_suffix = ''
html_static_path = ['_static']
html_theme = 'sphinx_book_theme'
html_theme_options = {'search_bar_text': 'Search this book...', 'launch_buttons': {'notebook_interface': 'classic', 'binderhub_url': 'https://mybinder.org', 'jupyterhub_url': '', 'thebe': True, 'colab_url': 'https://colab.research.google.com'}, 'path_to_docs': 'docs', 'repository_url': 'https://github.com/executablebooks/jupyter-book', 'repository_branch': 'master', 'google_analytics_id': 'UA-52617120-7', 'extra_navbar': 'Powered by <a href="https://jupyterbook.org">Jupyter Book</a>', 'extra_footer': '', 'home_page_in_toc': False, 'use_repository_button': True, 'use_edit_page_button': True, 'use_issues_button': True}
html_title = ''
intersphinx_mapping = {'ebp': ['https://executablebooks.org/en/latest/', None], 'myst-parser': ['https://myst-parser.readthedocs.io/en/latest/', None], 'myst-nb': ['https://myst-nb.readthedocs.io/en/latest/', None], 'sphinx': ['https://www.sphinx-doc.org/en/master', None], 'nbformat': ['https://nbformat.readthedocs.io/en/latest', None], 'sphinx-panels': ['https://sphinx-panels.readthedocs.io/en/sphinx-book-theme/', None]}
jupyter_cache = ''
jupyter_execute_notebooks = 'cache'
language = 'en'
latex_elements = {'preamble': '\\newcommand\\N{\\mathbb{N}}\n\\newcommand\\floor[1]{\\lfloor#1\\rfloor}\n\\newcommand{\\bmat}{\\left[\\begin{array}}\n\\newcommand{\\emat}{\\end{array}\\right]}\n'}
latex_engine = 'xelatex'
mathjax3_config = {'TeX': {'Macros': {'N': '\\mathbb{N}', 'floor': ['\\lfloor#1\\rfloor', 1], 'bmat': ['\\left[\\begin{array}'], 'emat': ['\\end{array}\\right]']}}}
myst_enable_extensions = ['amsmath', 'colon_fence', 'deflist', 'dollarmath', 'html_admonition', 'html_image', 'linkify', 'replacements', 'smartquotes', 'substitution']
myst_substitutions = {'sub3': 'My _global_ value!'}
myst_url_schemes = ['mailto', 'http', 'https']
nb_custom_formats = {'.Rmd': ['jupytext.reads', {'fmt': 'Rmd'}]}
nb_output_stderr = 'show'
numfig = True
panels_add_bootstrap_css = False
pygments_style = 'sphinx'
rediraffe_branch = 'master'
rediraffe_redirects = {'content-types/index.md': 'file-types/index.md', 'content-types/markdown.md': 'file-types/markdown.md', 'content-types/notebooks.ipynb': 'file-types/notebooks.ipynb', 'content-types/myst-notebooks.md': 'file-types/myst-notebooks.md', 'content-types/jupytext.md': 'file-types/jupytext.Rmd', 'content-types/restructuredtext.md': 'file-types/restructuredtext.md'}
suppress_warnings = ['myst.domains']
use_jupyterbook_latex = True
use_multitoc_numbering = True
