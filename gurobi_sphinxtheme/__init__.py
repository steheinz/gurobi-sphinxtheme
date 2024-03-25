import pathlib

here = pathlib.Path(__file__).parent


def setup(app):
    app.add_html_theme("gurobi_sphinxtheme", here / "theme")
