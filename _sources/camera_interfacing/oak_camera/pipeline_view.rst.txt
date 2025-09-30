Pipeline Graph
==================
There's `DepthAI Pipeline Graph`_ tool which helps in dynamic visualization of pipeline from script along
with input/output FPS of nodes.

Installation
--------------

.. code-block:: bash

  pip install git+https://github.com/luxonis/depthai_pipeline_graph.git

  # pip install PySide2   # Error while launching Qt Window
  pip install PyQt5


It is developed using Qt framework. Upon using **PySide2** as mentioned in official documentation,
I had error so I **switched to PyQt5** module.


.. _pipeline_depth_preview:

Live Pipeline View
--------------------

.. code-block:: bash

  pipeline_graph run "python3 script.py"

.. image:: /_static/images/depthai/pipeline_depth_preview.png


Errors Faced
-------------

1. When trying to use variable names in graph, it did not work.

  .. code-block:: bash

    pipeline_graph run "python3 script.py" -var


2. When trying to view pipeline from a json schema, it did not open. See this forum to check if issue is resolved: `json_load_error_forum`_.

  Saving pipeline schema to json:

  .. code-block:: python

    # After declaring nodes, defining properties and linking nodes

    pipeline.serializeToJson()

  Viewing pipeline schema:

  .. code-block:: bash

    pipeline_graph load test.json


See the code of depth preview example :ref:`depth_preview_example`


.. _DepthAI Pipeline Graph: https://docs.luxonis.com/software/tools/pipeline-graph/

.. _XLinkOut: https://docs.luxonis.com/software/depthai-components/nodes/xlink_out/
.. _XLinkIn: https://docs.luxonis.com/software/depthai-components/nodes/xlink_in/

.. _CameraControl message: https://docs.luxonis.com/software/depthai-components/messages/camera_control/

.. _json_load_error_forum: https://discuss.luxonis.com/d/1447-how-to-view-pipeline-with-pipeline-editor