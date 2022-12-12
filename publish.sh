python setup.py bdist_wheel
twine upload dist/*
rm -rf build dist jackofspades_liblab_lotr.egg-info
