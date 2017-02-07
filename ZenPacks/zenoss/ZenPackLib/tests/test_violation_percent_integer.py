#!/usr/bin/env python

##############################################################################
#
# Copyright (C) Zenoss, Inc. 2015, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

"""
    Duration threshold has a problem where you cant set the violationPercent as integer (ZEN-24079)
"""
from ZenPacks.zenoss.ZenPackLib.tests.ZPLTestBase import ZPLTestBase


YAML_DOC = """
name: ZenPacks.zenoss.DurationThreshold
device_classes:
  /Devices:
    templates:
      TESTTEMPLATE:
        description: Testing that Duration threshold accepts integer values
        datasources:
          currentReading:
            type: SNMP
            datapoints:
              currentReading: {}
            oid: .1.3.6.1.4.1.232.6.2.6.8.1.4
        thresholds:
          DurationThreshold:
            type: DurationThreshold
            dsnames: [currentReading_currentReading]
            violationPercentage: 10
            timePeriod: 2 days
"""


class TestDurationThresholdInteger(ZPLTestBase):
    """Test fix for ZEN-24079

       Duration threshold has a problem where you cant set the violationPercent as integer
    """

    yaml_doc = YAML_DOC
    disableLogging = False

    def test_integer_threshold(self):
        if self.z.zenpack_installed():
            self.assertTrue(self.z.check_templates_vs_yaml(), "Template objects do not match YAML")
            self.assertTrue(self.z.check_templates_vs_specs(), "Template objects do not match Spec")
            # check properties on dummy template
            dcs = self.z.cfg.device_classes.get('/Devices')
            tcs = dcs.templates.get('TESTTEMPLATE')
            t = tcs.create(self.dmd, False)
            for th in t.thresholds():
                self.assertTrue(isinstance(th.violationPercentage, int),
                    'DurationThreshold property (violationPercentage) should be int, got {}'.format(type(th.violationPercentage)))
        else:
            self.log.warn('Skipping test_integer_threshold since ZenPacks.zenoss.DurationThreshold not installed.')


def test_suite():
    """Return test suite for this module."""
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestDurationThresholdInteger))
    return suite

if __name__ == "__main__":
    from zope.testrunner.runner import Runner
    runner = Runner(found_suites=[test_suite()])
    runner.run()
