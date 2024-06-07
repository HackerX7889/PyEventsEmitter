import os
import codecs

from setuptools import setup, find_packages

package_name = "PyEventsEmitter"

path = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(path, "PyEventsEmitter/README.md"), encoding="utf-8") as this:
    long_description = "\n" + this.read()

VERSION = "0.0.1"
DESCRIPTION = "Powerful and flexible EventEmitter implementation with advanced features."

exclude = ["PyEventsEmitter/tests", "PyEventsEmitter/*.tests", "PyEventsEmitter/*.txt", "PyEventsEmitter/others", "PyEventsEmitter/backups", "PyEventsEmitter/.vscode", "PyEventsEmitter/__pycache__","PyEventsEmitter/.gitignore", "PyEventsEmitter/docs"]
include = ["PyEventsEmitter/."]

setup(
    name=package_name,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HackerX7889/PyEventsEmitter",
    author="HackerX",
    packages=find_packages(exclude=exclude, include=include),
    keywords= ["EventEmitter", "PyEventsEmitter", "Emitter", "Events"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
