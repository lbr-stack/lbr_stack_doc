LBR-Stack
=========
The ``LBR-Stack`` hosts community contributed extensions to KUKA's Fast Robot Interface (FRI) for accelerated research and deployment. The FRI is KUKA's library for commanding the ``LBR`` over a UDP connection.

The ``LBR-Stack`` provides ``CMake`` support for the FRI. This is further used for ``ROS 2`` integration and ``Python`` bindings, as shown :ref:`below <lbr_stack fri dependency architecture figure>`:

.. _lbr_stack fri dependency architecture figure:
.. thumbnail:: ../img/fri_dependency_architecture.svg
    :alt: fri_dependency_architecture

Further documentation is available for:

* `FRI CMake Support <fri/README.html>`_: To see available FRI versions.
* `ROS 2 Integration <lbr_fri_ros2_stack/README.html>`_: ROS 2 packages around the FRI and the LBR (simulation, system integration, safe execution utilities, research, deployment).
* `Python Bindings <pyfri/README.html>`_: Write custom FRI applications without compilation (reserach, experienced users).
* :doc:`Hardware Setup <lbr_fri_ros2_stack/lbr_fri_ros2_stack/doc/hardware_setup>`: Java application installation instructions.

.. toctree::
   :hidden:
   :caption: FRI CMake Support

   fri

.. toctree::
   :hidden:
   :caption: ROS 2 Integration

   lbr_fri_ros2_stack/lbr_fri_ros2_stack/doc/lbr_fri_ros2_stack
   lbr_fri_ros2_stack/lbr_bringup/doc/lbr_bringup
   lbr_fri_ros2_stack/lbr_demos/doc/lbr_demos
   lbr_fri_ros2_stack/lbr_fri_ros2/doc/lbr_fri_ros2
   lbr_fri_ros2_stack/lbr_ros2_control/doc/lbr_ros2_control
   lbr_fri_ros2_stack/docker/doc/docker
   lbr_fri_ros2_stack/lbr_moveit_config/doc/lbr_moveit_config
   lbr_fri_idl
   
.. toctree::
   :hidden:
   :caption: Python Bindings

   pyfri/doc/pyfri

.. toctree::
   :hidden:
   :caption: Hardware Setup

   lbr_fri_ros2_stack/lbr_fri_ros2_stack/doc/hardware_setup

.. toctree::
   :hidden:
   :caption: Additional Resources

   fri/doc/fri
   docs/kuka_documentation
   Paper <https://arxiv.org/pdf/2311.12709>
   contributing
   source_code
   changelog
