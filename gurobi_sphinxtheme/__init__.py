import os
import pathlib

here = pathlib.Path(__file__).parent


def setup_context(app, pagename, templatename, context, doctree):
    if os.environ.get("READTHEDOCS") == "True":
        context["gurobi_rtd"] = "true"
        for env_var in [
            "project",
            "version",
            "version_name",
            "version_type",
            "canonical_url",
        ]:
            context[f"gurobi_rtd_{env_var}"] = os.environ.get(
                f"READTHEDOCS_{env_var.upper()}", ""
            )


def setup(app):
    app.add_html_theme("gurobi_sphinxtheme", here / "theme")
    app.connect("html-page-context", setup_context)
