#!/usr/bin/env python

from cx_Freeze import setup, Executable

base = None


executables = [Executable("project_template/project_template.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name='PythonProjectTemplate',
    options=options,
    version='0.1',
    description='<any description>',
    long_description=open('README.md').read(),
    executables=executables
)
