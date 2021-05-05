#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the main package_name CLI module"""

from subprocess import (PIPE, Popen)
from unittest import TestCase


class TestMainHelp(TestCase):
    def test_returns_usage_information(self):
        output = Popen(['python', '-m', 'package_name', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue('usage:' in output.decode('utf-8'))
