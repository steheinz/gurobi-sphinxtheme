# Sphinx theme for all Gurobi documentation

## Usage

The docs repos that use this theme install from the main branch, so only the
following is needed:

`requirements.txt`:

```
gurobi-sphinxtheme @ git+https://github.com/Gurobi/gurobi-sphinxtheme.git@main
```

`conf.py`:

```
project = "<project title>"
copyright = "2024, Gurobi Optimization"
author = "Gurobi Optimization"
html_title = "<title to appear in browser tabs>"

html_theme = "gurobi_sphinxtheme"
html_favicon = "https://www.gurobi.com/favicon.ico"
```

## Styling

Based on [furo](https://github.com/pradyunsg/furo), with minor tweaks.
The stylesheet `gurobi.css` resets some header text sizes.

## Banners

The following banners are added in `page.html`:

- An 'under construction' warning banner on all sites (to be removed in future)
- A version warning banner directing users to the latest release if necessary
- An epilogue banner directing users to search features and support

Banners are configured based on [environment variables set by
readthedocs](https://docs.readthedocs.io/en/stable/reference/environment-variables.html)
and theme options specified in `theme.conf`. Check `setup_context` in
`__init__.py` for details.

## Development

A handy trick when working on the theme is to install in editable mode and use
`livehtml` on one of the docs repos to auto reload. This requires full rebuilds
on every theme change so choose one of the smaller repos if possible.

```
pip install -e </path/to/gurobi-sphinxtheme>
export READTHEDOCS="True"
export READTHEDOCS_VERSION_TYPE="branch"
export READTHEDOCS_GIT_CLONE_URL="git@github.com:Gurobi/repo.git"
export READTHEDOCS_VERSION="10.0"
export READTHEDOCS_CANONICAL_URL="./10.0/"
make SPHINXOPTS="-a --watch </path/to/gurobi-sphinxtheme>" livehtml
```
