
.. _configuring_ventilation_section_label:

=======================
Configuring Ventilation
=======================

.. note:: This version of the software cannot run a ventilation problem and then run another ventilaion problem again.  There is a memory issue with one of the required libraries which is currently being investigated (and hopefully solved).  This means unfortunately that to run another problem, possibly with changed parameters, you will need to restart the application.

----------------
Basic Parameters
----------------

The most simple parameters we have to configure among all the ventilation parameters is whether to simulate a small tree model of the lung or a large tree model of the lung.  This is done through the :guilabel:`General` tab on the :guilabel:`Problem` screen.

The small model should only take a matter of seconds to run, whereas the large tree model may take up to a minute (or more).

---------------
Main Parameters
---------------

The main parameters available on the :guilabel:`Parameters`	tab control the solver settings.

---------------
Flow Parameters
---------------

The flow parameters available on the :guilabel:`Parameters` tab control the behaviour of the model.

-----------------
Advanced Settings
-----------------

There are some advanced settings availble when the advanced check box is checked on the :guilabel:`General` tab.  As the title indicates this is for advanced usage only (so you don't need to be told what to do if you are using this option!).
