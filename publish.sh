#!/usr/bin/env bash

python setup.py bdist_wheel
twine upload dist/*
rm -rf build dist jackofspades_lib_lab_lotr.egg-info
