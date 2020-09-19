Japanese Aesthetic Terminal
==============================

.. toctree::
    :hidden:
    :maxdepth: 1

    license
    reference

A command-line interface prints random facts to your console in Japanese text,
using the `Wikipedia API <https://ja.wikipedia.org/api/rest_v1/#/>`_.

Perfect to have in the background while studying and Lo-Fi beats are playing!!!


Installation
------------

To install the Hypermodern Python project,
run this command in your terminal:

.. code-block:: console

   $ pip install jp-aesthetic-terminal


Usage
-----

Hypermodern Python's usage looks like:

.. code-block:: console

   $ jp-aesthetic-terminal [OPTIONS]

.. option:: -i <iterations>, --iterations <iterations>

   How many random pages to be printed before closing.
   Because this is meant to continuously run in the background for a while,
   the default value is 50.

.. option:: -s <time_to_sleep>, --time_to_sleep <time_to_sleep>

  How long to wait before making each API call (in seconds), default is 2 seconds

.. option:: --version

   Display the version and exit.

.. option:: --help

   Display a short usage message and exit.
