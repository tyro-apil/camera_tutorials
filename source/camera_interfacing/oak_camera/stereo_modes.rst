Stereo-Depth Modes
==================

1. Active Stereo
    If there's no texture in the images, the usual block-matching process for left-right correspondence does not work.
    To solve this issue, OAK Pro cameras have **IR Laser Dot Projector** which projects little dots on the scene and 
    helps with stereo-matching algorithm.

    .. code-block:: python

      with dai.Device(pipeline) as device:

        #############################
        device.setIrLaserDotProjectorIntensity(0.5) # in %, from 0 to 1 
        #############################

        # Continue... 
    
    .. image:: /_static/images/depthai/active_stereo.png


2. Extended Disparity - A solution for short-range stereo-depth
    While matching left-right correspondance, the algorithm does not search through the whole line but just a section of the line 
    since its computationally expensive. But, by increasing this disparity search width helps get depths of nearer objects too
    by adding some latency to our pipeline.

    .. math::
      Z = \frac{f.B}{d}
    
    where,
      * `Z`: depth
      * `f`: focal length
      * `B`: baseline
      * `d`: disparity
    
    It can be seen that depth is inversely proportional to disparity. So, if disparity increases, then depth decreases.

    .. code-block:: python

      pipeline = dai.Pipeline()
      stereo = pipeline.create(dai.node.StereoDepth)

      # Closer-in minimum depth, disparity range is doubled:
      stereo.setExtendedDisparity(True)
  
3. Subpixel Disparity
    Disparity not just discrete but can be in fraction of a pixel too, which improves precision for long-range measurements.

    .. code-block:: python

      pipeline = dai.Pipeline()
      stereo = pipeline.create(dai.node.StereoDepth)

      # Better accuracy for longer distance, fractional disparity 32-levels:
      stereo.setSubpixel(True)

4. Left-Right Check
    Removes incorrectly calculated disparity pixels due to occlusions at object borders (Forward Mapping + Backward Check).

    .. code-block:: python

      pipeline = dai.Pipeline()
      stereo = pipeline.create(dai.node.StereoDepth)

      # Better handling for occlusions:
      stereo.setLeftRightCheck(True)




References
----------
1. `Stereo Depth Node Docs`_  
2. `Configuring Stereo Depth Docs`_


.. _Stereo Depth Node Docs: https://docs.luxonis.com/software-v3/depthai/depthai-components/nodes/stereo_depth/
.. _Configuring Stereo Depth Docs: https://docs.luxonis.com/hardware/platform/depth/configuring-stereo-depth/