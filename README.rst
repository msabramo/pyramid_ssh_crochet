pyramid_ssh_crochet
=================================

.. image:: https://img.shields.io/pypi/v/pyramid_ssh_crochet.svg
    :target: https://pypi.python.org/pypi/pyramid_ssh_crochet

Intro
=================================

This lets your Pyramid_ app run an SSH server so that you can SSH in and inspect application state.

It does this by using Crochet_ and `Twisted Conch Manhole`_.

To use this, add some info to your config file:

.. code-block:: ini

    pyramid.includes =
      pyramid_ssh_crochet

    pyramid_ssh_crochet.port = 5022
    pyramid_ssh_crochet.username = admin
    pyramid_ssh_crochet.password = secret


.. _Pyramid: http://www.trypyramid.com/
.. _Crochet: https://crochet.readthedocs.org/
.. _Twisted Conch Manhole: http://twistedmatrix.com/documents/current/api/twisted.conch.manhole.html
