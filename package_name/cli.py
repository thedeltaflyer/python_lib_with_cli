#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

from . import (log, __version__)
from .googs import can_get_to_google


def main():
    parser = ArgumentParser()
    parser.add_argument("echo_text",
                        default=None,
                        nargs='*',
                        help="Echo some text...")
    parser.add_argument("-d", "--debug", action='store_true',
                        default=False,
                        help="Enable debug mode")
    parser.add_argument("-v", "--version", action='version',
                        version="v{}".format(__version__),
                        help="Print version number.")
    args = parser.parse_args()

    if args.debug:
        log.logger.setLevel(log.DEBUG)

    log.debug("Debug Mode is Enabled!")

    if args.echo_text:
        print(args.echo_text)

    if can_get_to_google():
        print("Able to get to Google!")
    else:
        print("Can't get to Google :(")
