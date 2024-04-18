import os
import pathlib
import re

here = pathlib.Path(__file__).parent


def setup_context(app, pagename, templatename, context, doctree):
    if os.environ.get("READTHEDOCS") == "True":

        # Version and url information. Store these in distinct jinja variables
        # to prevent clashes with themes we inherit from.
        context["gurobi_rtd"] = "true"
        context["gurobi_rtd_version"] = os.environ.get("READTHEDOCS_VERSION")
        context["gurobi_rtd_version_type"] = os.environ.get("READTHEDOCS_VERSION_TYPE")
        context["gurobi_rtd_canonical_url"] = os.environ.get(
            "READTHEDOCS_CANONICAL_URL"
        )

        # For branch (i.e. not pull request) builds, get the canonical URL of
        # the stable version.
        if context["gurobi_rtd_version_type"] == "branch":
            stem, mid, _ = context["gurobi_rtd_canonical_url"].rpartition(
                context["gurobi_rtd_version"]
            )
            assert mid and stem.endswith("/")
            context["gurobi_rtd_stable_url"] = stem + "stable/"

        # URL for the issues page of the source repo.
        git_clone_url = os.environ.get("READTHEDOCS_GIT_CLONE_URL")
        match = re.match(r"git@github\.com:Gurobi/([\w-]+)\.git", git_clone_url)
        if not match:
            raise ValueError(f"Unexpected value: GIT_CLONE_URL={git_clone_url}")
        repo_name = match.group(1)
        context["gurobi_gh_issue_url"] = (
            f"https://github.com/Gurobi/{repo_name}/issues/new?labels=bug&template=bug_report.md"
        )


def update_config(app):
    # Set options for furo, without theme users having to do it themselves.
    # See https://chrisholdgraf.com/blog/2022/sphinx-update-config/
    app.builder.theme_options.update({
        "light_css_variables": {
            "color-brand-primary": "#DD2113",
            "color-brand-content": "#1675a9",
        },
        "dark_css_variables": {
            "color-brand-primary": "#DD2113",
            "color-brand-content": "#1675a9",
        },
        "sidebar_hide_name": True,
        "light_logo": "gurobi_light.svg",
        "dark_logo": "gurobi_dark.svg",
    })


def setup(app):
    app.add_html_theme("gurobi_sphinxtheme", here / "theme")
    app.connect("html-page-context", setup_context)
    app.connect("builder-inited", update_config)
