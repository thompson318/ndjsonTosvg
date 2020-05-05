ndjsonTosvg
===============================

.. image:: https://github.com/thompson318/ndjsonTosvg/raw/master/project-icon.png
   :height: 128px
   :width: 128px
   :target: https://github.com/thompson318/ndjsonTosvg
   :alt: Logo

.. image:: https://github.com/thompson318/ndjsonTosvg/badges/master/build.svg
   :target: https://github.com/thompson318/ndjsonTosvg/pipelines
   :alt: GitLab-CI test status

.. image:: https://github.com/thompson318/ndjsonTosvg/badges/master/coverage.svg
    :target: https://github.com/thompson318/ndjsonTosvg/commits/master
    :alt: Test coverage

.. image:: https://readthedocs.org/projects/ndjsonTosvg/badge/?version=latest
    :target: http://ndjsonTosvg.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status



Author: Stephen Thompson

ndjsonTosvg is part of the `SNAPPY`_ software project, developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, part of `University College London (UCL)`_.

ndjsonTosvg supports Python 2.7 and Python 3.6.

ndjsonTosvg is currently a demo project, which will add/multiply two numbers. Example usage:

::

    python ndjsontosvg.py 5 8
    python ndjsontosvg.py 3 6 --multiply

Please explore the project structure, and implement your own functionality.

Developing
----------

Cloning
^^^^^^^

You can clone the repository using the following command:

::

    git clone https://github.com/thompson318/ndjsonTosvg


Running tests
^^^^^^^^^^^^^
Pytest is used for running unit tests:
::

    pip install pytest
    python -m pytest


Linting
^^^^^^^

This code conforms to the PEP8 standard. Pylint can be used to analyse the code:

::

    pip install pylint
    pylint --rcfile=tests/pylintrc ndjsontosvg


Installing
----------

You can pip install directly from the repository as follows:

::

    pip install git+https://github.com/thompson318/ndjsonTosvg



Contributing
^^^^^^^^^^^^

Please see the `contributing guidelines`_.


Useful links
^^^^^^^^^^^^

* `Source code repository`_
* `Documentation`_


Licensing and copyright
-----------------------

Copyright 2020 University College London.
ndjsonTosvg is released under the BSD-3 license. Please see the `license file`_ for details.


Acknowledgements
----------------

Supported by `Wellcome`_ and `EPSRC`_.


.. _`Wellcome EPSRC Centre for Interventional and Surgical Sciences`: http://www.ucl.ac.uk/weiss
.. _`source code repository`: https://github.com/thompson318/ndjsonTosvg
.. _`Documentation`: https://ndjsonTosvg.readthedocs.io
.. _`SNAPPY`: https://weisslab.cs.ucl.ac.uk/WEISS/PlatformManagement/SNAPPY/wikis/home
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://github.com/thompson318/ndjsonTosvg/blob/master/CONTRIBUTING.rst
.. _`license file`: https://github.com/thompson318/ndjsonTosvg/blob/master/LICENSE

