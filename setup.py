#!/usr/bin/env python3
# coding=utf-8

from distutils.core import setup

version = "0.3"

setup(
    name="jefferson",
    version=version,
    description="",
    author="Stefan Viehböck",
    url="https://github.com/sviehb/jefferson",
    license="MIT",
    requires=['cstruct', 'pylzma'],
    packages=["jefferson"],
    package_dir={"jefferson": "src/jefferson"},
    scripts=["src/scripts/jefferson"],
)