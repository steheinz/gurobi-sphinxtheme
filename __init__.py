from os import path

def setup(app):
    app.add_html_theme("gurobi_sphinxtheme", path.abspath(path.dirname(__file__)))