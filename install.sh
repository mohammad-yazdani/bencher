#!/usr/bin/env bash

rm -r -f build dist *.egg-info
python setup.py bdist_wheel
pip uninstall csbencher
pip install dist/csbencher-0.0.7-py2-none-any.whl
rm -r -f build dist *.egg-info
