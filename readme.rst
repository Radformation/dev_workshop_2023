How to contribute
=================

Get set up
----------

These are the steps to get set up with the repo locally with the intent to contribute:

* Clone the repo
* Install `Python 3.11 <https://www.python.org/downloads/>`__ (if not on your system already) and check the box to include in PATH (on Windows).
* Create a `virtual environment <https://docs.python.org/3/library/venv.html#creating-virtual-environments>`__ via a terminal:

  .. code-block:: bash

    # navigate to the repo location
    python -m venv venv  # creates a venv named 'venv' in the current directory

* With the activated venv, install the requirements:

  .. code-block:: bash

    pip install -r requirements.txt

* Set up `pre-commit <https://pre-commit.com/>`__. Pre-commit is an amazing tool to ensure checks are performed before committing changes.
  In our case, we want to make sure we've properly formatted the docs. Install the hooks like so:

  .. code-block:: bash

    pre-commit install

  This will install repo-specific hooks that check a number of items defined by ``.pre-commit-config.yaml``.

Now you're ready to go!

Rendering the docs
------------------

To render the docs with hot reloading so you can see your contributions
interactively, run a ``nox`` script like so:

.. code-block:: bash

  nox -s serve_docs

This will build the docs, open a browser, and hot-reload changes you make.

Sphinx
------

The markup used is `Sphinx <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`__ `reStructuredText <https://en.wikipedia.org/wiki/ReStructuredText>`__.
It is generic and flexible and for complicated layouts is often preferable to markdown.

The Sphinx `primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__ is an excellent place to start.

As well, simply looking at the other .rst files in this repo should give you a good understanding of how to do
most things.
