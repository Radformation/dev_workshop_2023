import nox


@nox.session(python=False)
def serve_docs(session):
    """Build the docs and open a browser with hot reloading"""
    session.run(
        "sphinx-autobuild",
        "source",
        "build",
        "--port",
        "8787",
        "--open-browser",
    )
