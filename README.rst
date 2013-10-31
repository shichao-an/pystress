pystress - Simple CPU stresser in Python
========================================

pystress is a tool to stress your CPU in a simple manner.

.. image:: https://travis-ci.org/shichao-an/pystress.png?branch=master
   :target: https://travis-ci.org/shichao-an/pystress


Installation
------------
You can install with pip::

  $ pip install pystress

Or, you can download a source distribution and install with these commands::

  $ python setup.py install


Example usage
-------------
Stress CPU(s) with the same number of processes for 60 (default) seconds::

  $ pystress


Stress CPU(s) with 2 processes for 10 seconds::

  $ pystress 10 2
