##############################################################################
#
# Copyright (C) Zenoss, Inc. 2015, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

from . import zenpacklib
import os

CFG = zenpacklib.load_yaml(os.path.join(os.path.dirname(__file__), 'zenpack.yaml'))