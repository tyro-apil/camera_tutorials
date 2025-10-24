Setup
=====

OpenCV installation
-------------------

We will be installing OpenCV package in Python.
For using OpenCV with C++, see `OpenCV Linux Install`_ and `OpenCV with gcc and CMake`_.
There are 4 different opencv packages.

For desktop environments (GUI support):

1. opencv-python
    main modules package
2. opencv-contrib-python
    main + extra modules (`OpenCV Docs`_)

For server setups (no GUI):

1. opencv-python-headless
2. opencv-contrib-python-headless

The most preferred version is **opencv-python** but if you need extra modules install the **opencv-contrib-python** package.

.. code-block:: bash

  # Create a virtual environment
  python3 -m venv .venv

  # Activate environment (In Linux)
  source .venv/bin/activate

  # Install OpenCV package (It has numpy as dependency so numpy will be installed automatically.)
  pip3 install opencv-python


MATLAB
------

Recommended toolbox:

1. `MATLAB Image Processing Toolbox`_
2. `MATLAB Computer Vision Toolbox`_


.. _OpenCV Linux Install: https://docs.opencv.org/master/d7/d9f/tutorial_linux_install.html
.. _OpenCV with gcc and CMake: https://docs.opencv.org/master/db/df5/tutorial_linux_gcc_cmake.html
.. _OpenCV Docs: https://docs.opencv.org/master/

.. _MATLAB Image Processing Toolbox: https://www.mathworks.com/products/image-processing.html 
.. _MATLAB Computer Vision Toolbox: https://www.mathworks.com/products/computer-vision.html