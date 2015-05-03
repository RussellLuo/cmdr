#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import click

from .config import config


# Treat commands as plugins with the help of `pluginbase` library
from pluginbase import PluginBase
plugin_base = PluginBase(package='cmdr.commands')
plugin_source = plugin_base.make_plugin_source(searchpath=[config.COMMANDS_PATH])


class Commander(object):

    def get_command(self, command_name):
        for plugin_name in plugin_source.list_plugins():
            if plugin_name == command_name:
                command = plugin_source.load_plugin(plugin_name)
                return command
        else:
            raise RuntimeError(
                'Command `{0}` not found. Please ensure that a Python '
                'module (or package) named "{0}.py" (or "{0}/__init__.py") '
                'exists in "{1}"'.format(command_name, config.COMMANDS_PATH)
            )

    def get_command_list(self):
        command_list = []
        for plugin_name in plugin_source.list_plugins():
            command = plugin_source.load_plugin(plugin_name)
            command_list.append((plugin_name, command.__doc__))
        return command_list

    def execute_command(self, command_name, *args):
        command = self.get_command(command_name)
        try:
            entry_point = getattr(command, config.ENTRY_POINT)
        except AttributeError:
            raise RuntimeError(
                'Entry point `{0}` not found. Please ensure that a '
                'function named "{0}" exists in the Python module '
                '(or package) "{1}.py" (or "{1}/__init__.py") '.format(
                    config.ENTRY_POINT, command_name
                )
            )
        entry_point(*args)


@click.command()
@click.option('--list', '-l', is_flag=True, help='Show available commands.')
@click.argument('command_name', required=False)
@click.argument('args', nargs=-1)
def main(list, command_name, args):
    commander = Commander()
    if list:
        command_list = commander.get_command_list()
        if not command_list:
            click.echo('No commands available.')
        else:
            click.echo('Available commands:')
            for command_name, command_doc in command_list:
                click.echo('    {0: <26}{1}'.format(
                    command_name, command_doc or ''
                ))
    else:
        if command_name is None:
            raise click.UsageError('`COMMAND_NAME` argument is required.')
        commander.execute_command(command_name, *args)


if __name__ == '__main__':
    main()
