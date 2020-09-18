#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Andrew Canter"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser()
    return parser


def main(args):
    """Implementation of echo"""
    # your code here
    parser = create_parser()
    parser.add_argument('echo', help='Provided string to be printed out')
    parser.add_argument('-t', '--title', action="store_true", help='Title string')
    parser.add_argument('-u', '--upper', action="store_true", help='Uppercase string')
    parser.add_argument('-l', '--lower', action="store_true", help='Lowercase string')
    ns = parser.parse_args(args)

    result = ns.echo

    if ns.title:
        result = result.title()
    if ns.upper:
        result = result.upper()
    if ns.lower:
        result = result.lower()

    print(result)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
