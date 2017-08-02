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
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)
