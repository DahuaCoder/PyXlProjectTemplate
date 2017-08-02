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
    name='PyXlProjectTemplate',
    version='0.1dev',
    packages=['project_template', ],
    license='Dario Steiner license',
    long_description=open('README.md').read(),
    options=options,
    description='<any description>',
    executables=executables
)
