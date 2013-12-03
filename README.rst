===============================
Jetstream CLI
===============================

.. image:: https://badge.fury.io/py/jetstream.cli.png
    :target: http://badge.fury.io/py/jetstream.cli
    
.. image:: https://pypip.in/d/jetstream.cli/badge.png
        :target: https://crate.io/packages/jetstream.cli?version=latest

A command-line interface for the Jetstream framework. Supported commands
are `list´for showing available pipes that can be run, and `run` for
running such a pipe::

  Usage:
    jet list [--config FILE] [--log LEVEL]
    jet run <pipename> [--config FILE] [--log LEVEL]
    jet (-h | --help)
    jet --version

  Options:
    -h --help        Show this screen.
    --version        Show version.
    --config FILE    Use a given config file.
    --log LEVEL      Set log level (DEBUG|INFO|WARN|ERROR)
