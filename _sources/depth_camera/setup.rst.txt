Basic Setup
==================

For integrating in ROS2 ecosystem, we have dedicated `DepthAI ROS Package`_ for it.
For quick prototyping and testing, we can use `DepthAI Pip Package`_.


Install Commands
-----------------------------

.. code-block:: shell

  # Create virtual environment
  python -m venv .env

  # Activate virtual environment
  source .env/bin/activate

  pip install depthai


``Using packages from virtual environment doesnot integrate with ROS2 ecosystem. We had install
packages in the home directory.``


Useful Packages
-------------------
For viewing frames live from a python script, you need opencv.

.. code-block:: bash

  pip install opencv-python
  

Read/Write Access through USB
-----------------------------
*Error*:
``[depthai] [warning] Insufficient permissions to communicate with X_LINK_UNBOOTED 
device with name "1.2". Make sure udev rules are set``

.. code-block:: bash

  # Setup proper udev rules
  echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="03e7", MODE="0666"' | sudo tee /etc/udev/rules.d/80-movidius.rules
  sudo udevadm control --reload-rules && sudo udevadm trigger

Debugging
----------------
For getting debug messages in console from python script, we need to set debug message level:

1. critical
2. error
3. warn
4. info
5. debug
6. trace

| Official `Debug Guide`_ Documentation: For details

You need to set **DEPTHAI_LEVEL** environment variable to one of above values.

**Temporary setting**

.. code-block:: bash

  DEPTHAI_LEVEL=debug python3 script.py


**Permanent setting**

.. code-block:: bash

  # Put Environment Variable in .bashrc
  echo "export DEPTHAI_LEVEL=debug" >> ~/.bashrc
  python3 script.py



.. _DepthAI ROS Package: https://docs.luxonis.com/software/ros/depthai-ros/
.. _DepthAI Pip Package: https://pypi.org/project/depthai/

.. _Debug Guide: https://docs.luxonis.com/software/depthai/debugging/