
OpenCV AI Kit (OAK) Camera
==========================

`OAK-D Pro W`_ has 2 black-and-white mono sensors on each side, 1 RGB sensor at the center, 1 `IR Dot Projector`_ (For **Active Stereo**), and 1 `IR Illumination LED`_ (For **Low light environment**).
For using it with low-power (can't supply more than 1 Amps through USB) Single Board Computer like Raspberry Pi, use the `OAK Y Adapter`_ for powering camera from dedicated power source.

.. Attention::
  All the examples are based on **DepthAI v2** API. But, the concepts are similar and migration can be done with minimal changes based upon following `Migration Guide`_ to **DepthAI v3** API.

.. toctree::
  :maxdepth: 1
  :caption: Contents:

  oak_camera/setup.rst
  oak_camera/workflow.rst
  oak_camera/pipeline_view.rst
  oak_camera/stereo_modes.rst

.. _OAK-D PRO W: https://docs.luxonis.com/hardware/products/OAK-D%20Pro%20W
.. _OAK Y Adapter: https://shop.luxonis.com/products/oak-y-adapter
.. _IR Dot Projector: https://docs.luxonis.com/hardware/products/OAK-D%20Pro%20W#Stereo%20depth%20perception-IR%20Dot%20Projector
.. _IR Illumination LED: https://docs.luxonis.com/hardware/products/OAK-D%20Pro%20W#Stereo%20depth%20perception-IR%20Illumination%20LED

.. _Migration Guide: https://docs.luxonis.com/software-v3/depthai/tutorials/v2-vs-v3/