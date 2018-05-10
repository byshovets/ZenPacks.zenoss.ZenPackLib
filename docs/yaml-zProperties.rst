.. _zProperties:

###########
zProperties
###########

zProperties are one part of Zenoss' hierarchical configuration system. They are
configuration properties that can be specified on any device class including
the root /Devices class, and on any individual device.


.. _zProperty-inheritance:

*********************
zProperty Inheritance
*********************

The most-specific value for a zProperty within the hierarchy will be used for
any given device. For instance, given a device *linux1* in the /Server/Linux
device class. The value for zSnmpMonitorIgnore will be checked first on the
linux1 device. If it is not set locally on the device, the /Server/Linux device
class will then be checked. If not set there, /Server will be checked. Finally
the value at / (or /Devices) will be checked as a final resort. Since all
zProperties must have a default values that is set at the root device class,
there will always be a value for the zProperty. Even if it is an empty string.

.. _adding-zProperties:

******************
Adding zProperties
******************

To add a zProperty to your ZenPack you must include a *zProperties* section in
your YAML file. The following example shows an example of adding two
zProperties.

.. code-block:: yaml

   zProperties:
     zWidgeterEnable:
       category: ACME Widgeter
       type: boolean
       default: true

     zWidgeterInterval:
       category: ACME Widgeter
       type: string
       default: 300

Each of these zProperty entries specifies a *category*, *type* and *default*.
These are the only valid fields of the a zProperty entry. However, each of
these fields has a default value that will be used if the field isn't
explicitly specified. For example, the default value for *type* is string. So
the above example could be shortened slightly by omitting the explicit *type*
on zWidgeterInterval.

.. code-block:: yaml

   zProperties:
     zWidgeterEnable:
       category: ACME Widgeter
       type: boolean
       default: true

     zWidgeterInterval:	
       category: ACME Widgeter
       default: 300

There is a special zProperty entry named *DEFAULTS* that can be used to further
shorten definitions in cases where you're adding many zProperties. The
following example shows how *DEFAULTS* can be used to replace the duplicated
*category* property.

.. code-block:: yaml

   zProperties:
     DEFAULTS:
       category: ACME Widgeter

     zWidgeterEnable:
       type: boolean
       default: true

     zWidgeterInterval:
       default: 300

Since a zProperty is a YAML "mapping", the minmal specification of a zProperty (name only) would look like:

.. code-block:: yaml

   zProperties:
     zWidgeterMinimal: {}

Each zProperty listed in *zProperties* will be created when the ZenPack is
installed, and removed when the ZenPack is removed.

.. note::

  When changing the default or category for a zProperty in the yaml, it changes in the zenoss system.  Removing a zProperty from yaml will not remove it from the zenoss system.  To remove it completely, you must write a migrate script to remove it.

.. _zProperty-fields:

****************
zProperty Fields
****************

The following fields are valid for a zProperty entry.

name
  :Description: Name (e.g. zWidgeterEnable). Must be begin with a lowercase "z".
  :Required: Yes
  :Type: string
  :Default Value: *implied from key in zProperties map*

type
  :Description:
      Type of property. Valid types:

      * `boolean`
      * `float`
      * `int`
      * `lines`
      * `long`
      * `password`
      * `string`

  :Required: No
  :Type: string
  :Default Value: string

default
  :Description:

      Default value for property. Default value depends on the type:

      * boolean: `false`
      * lines: `[]`
      * password: `""` (empty string)
      * string: `""` (empty string)
      * all others: `null` (None)

  :Required: No
  :Type: *varies*
  :Default Value: *varies*

category
  :Description: Category name. (e.g. ACME Widgeter). Used to group related zProperties in the UI.
  :Required: No
  :Type: string
  :Default Value: "" (empty string)

description
  :Description: Notes regarding the purpose and function of this zProperty
  :Required: No
  :Type: string
  :Default Value: "" (empty string)

label
  :Description: Brief description of zProperty
  :Required: No
  :Type: string
  :Default Value: "" (empty string)


***************************
Zenoss specific zProperties
***************************

When changing modeler bindings using the zDeviceTemplates property, this will take effect on your ZenPack.  Any previously defined bindings will be replaced.  The same applies to the device level template bindings using the zCollectorPlugins property.

.. note::

   Beginning with ZenPackLib 2.0, this behavior has changed by default.  zProperties will no longer be overwritten if a target device class
   already exists (i.e. during an upgrade or if the YAML affects a preexisting class such as /Devices/Server.  Instead, a warning
   will be displayed to the user during installation, and the target zProperty will be left alone.
   
   Setting "reset: true" for a specific device class in the YAML will override this behavior, causing the zProperties to be overritten with the YAML defaults
   

   
   
   