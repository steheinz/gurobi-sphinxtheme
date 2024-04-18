import os
import pathlib

here = pathlib.Path(__file__).parent


def setup_context(app, pagename, templatename, context, doctree):
    if os.environ.get("READTHEDOCS") == "True":

        context["gurobi_rtd"] = "true"
        context["gurobi_rtd_version"] = os.environ.get("READTHEDOCS_VERSION")
        context["gurobi_rtd_version_type"] = os.environ.get("READTHEDOCS_VERSION_TYPE")
        context["gurobi_rtd_canonical_url"] = os.environ.get("READTHEDOCS_CANONICAL_URL")

        if context["gurobi_rtd_version_type"] == "branch":
            stem, mid, _ = context["gurobi_rtd_canonical_url"].rpartition(context["gurobi_rtd_version"])
            assert mid
            assert stem.endswith("/")
            context["gurobi_rtd_stable_url"] = stem + "stable/"


def setup(app):
    app.add_html_theme("gurobi_sphinxtheme", here / "theme")
    app.connect("html-page-context", setup_context)
