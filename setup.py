#!/usr/bin/env python
import io
from setuptools import setup, find_packages

version = "0.2.1"

setup(
    name="pyalko",
    version=version,
    description="Asynchronous python client for AL-KO Robolinho Mowers.",
    long_description=io.open("README.md", encoding="UTF-8").read(),
    keywords="al-ko robolinho mower",
    author="Jon Kristian Nilsen (jonkristian)",
    author_email="hello@jonkristian.no",
    license="MIT",
    url="https://github.com/jonkristian/pyalko",
    packages=find_packages(exclude=["tests", "generator"]),
    install_requires=["aiohttp>=3.7.4"],
)
