PythonPathTools
================

Some useful commands I always use to handle imports and paths on python projects

Install
=======

...

Usage
=====

There are 3 commands available:

- `copy_python_path`: (Default shortcut `Ctrl+Alt+k`) Will generate the python path and will copy it to the clipboard. e.g. `foo.bar.MyClass.my_method`
- `copy_pytest_path`: (Default shortcut `Ctrl+Alt+p`) Will generate the "nodeid" used for runing pytest test and will copy it to the clipboard. e.g. `foo/bar.py::MyClass::my_method`
- `copy_import_first_definition`: (Default shortcut `Ctrl+Alt+i`)Will read the definitions list and generate a "from .. import .." and will copy it into the clipboard. e.g. `from foo.bar import MyClass`