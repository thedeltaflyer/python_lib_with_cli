#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the main package_name CLI module"""

from subprocess import (PIPE, Popen)
from unittest import TestCase

from package_name import __version__ as app_version


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = Popen(['package_cli', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue('usage:' in output.decode('utf-8'))

        output = Popen(['package_cli', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('usage:' in output.decode('utf-8'))


class TestVersion(TestCase):
    def test_return_version_information(self):
        output = Popen(['package_cli', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(output.strip().decode('utf-8'), "v{}".format(app_version))
