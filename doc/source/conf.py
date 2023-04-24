import pathlib
import subprocess

# generate doxygen
pathlib.Path("docs/doxygen/lbr_fri_ros2").mkdir(parents=True) # this is the doxygen OUTPUT_DIRECTORY
subprocess.run("doxygen", shell=True)

# convert doxygen to sphinx, source and build directory need
# to follow https://boschglobal.github.io/doxysphinx/docs/getting_started.html#build
subprocess.run("doxysphinx build . $READTHEDOCS_OUTPUT/html Doxyfile", shell=True)

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'lbr_fri_ros2'
copyright = '2023, mhubii'
author = 'mhubii'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser"
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
