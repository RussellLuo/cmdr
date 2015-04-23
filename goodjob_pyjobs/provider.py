#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import click

from goodjob_pyjobs.config import config


# Treat jobs as plugins with the help of `pluginbase` library
from pluginbase import PluginBase
plugin_base = PluginBase(package='goodjob_pyjobs.jobs')
plugin_source = plugin_base.make_plugin_source(searchpath=[config.JOBS_PATH])


class Job(object):
    def __init__(self, name):
        self.name = name
        for job_name in plugin_source.list_plugins():
            if job_name == name:
                self.job = plugin_source.load_plugin(job_name)
                break
        else:
            raise RuntimeError(
                'Job `{0}` not found. Please ensure that a Python '
                'module (or package) named "{0}.py" (or "{0}/__init__.py") '
                'exists in "{1}"'.format(name, config.JOBS_PATH)
            )

    def execute(self, *args):
        try:
            entry_point = getattr(self.job, config.ENTRY_POINT)
        except AttributeError:
            raise RuntimeError(
                'Entry point `{0}` not found. Please ensure that a '
                'function named "{0}" exists in the Python module '
                '(or package) "{1}.py" (or "{1}/__init__.py") '.format(
                    config.ENTRY_POINT, self.name
                )
            )
        entry_point(*args)


@click.command()
@click.argument('job_name')
@click.argument('args', nargs=-1)
def main(job_name, args):
    job = Job(job_name)
    job.execute(*args)


if __name__ == '__main__':
    main()
