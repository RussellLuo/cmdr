Cmdr
====

A command manager (i.e. Commander) for Python modules and packages.


Installation
------------

Install `Cmdr` with `pip`:

    $ pip install Python-Cmdr

Install development version from `GitHub`:

    $ git clone https://github.com/RussellLuo/cmdr.git
    $ cd cmdr
    $ python setup.py install


Why Cmdr?
---------

How to execute commands written in Python? There are some typical (or popular) ways:

1. Raw scripts

        $ vi /tmp/demo/hello.py

        def main():
            print('hello')

        if __name__ == '__main__':
            main()

        $ python /tmp/demo/hello.py

2. Use [click][1]

        $ vi /tmp/demo/hello.py

        import click

        @click.command()
        def main():
            print('hello')

        if __name__ == '__main__':
            main()

        $ python /tmp/demo/hello.py


3. Use [fabric][2]

        $ vi /tmp/demo/hello.py

        from fabric.api import task

        @task
        def main():
            print('hello')

        $ fab -f /tmp/demo/hello.py main

Although `click` and `fabric` are awesome (and flexible), they are also invasive (your code must depend on them). And all of the methods above may be tedious if you want to **manage a lot of commands which are almost independent, through an uniform interface**.

When you begin to care these problems, `Cmdr` is born for you.


Quickstart
----------

With `Cmdr`, we can just write normal Python modules or packages, and then use them as commands.

To make it happen, you must follow the steps below:

1. Set the `COMMANDS_PATH` configuration in a YAML file

        $ vi /tmp/demo/cmdr.yml

        COMMANDS_PATH: /tmp/demo/commands

2. Set the environment variable `CMDR_CONFIG_YAML`

        $ export CMDR_CONFIG_YAML=/tmp/demo/cmdr.yml

3. Create a Python module in `COMMANDS_PATH`

        # Note here:
        # the module "hello.py" is located in `COMMANDS_PATH`
        # (i.e. "/tmp/demo/commands").

        $ vi /tmp/demo/commands/hello.py

        # A function named "main" is defined here,
        # since the default `ENTRY_POINT` is "main".
        # You can customize it by setting your preferred
        # entry point name as `ENTRY_POINT` in the YAML file.

        def main():
            print('hello')

4. Show available commands (identified by module/package names)

        $ cmdr -l

5. Execute the command `hello`

        $ cmdr hello

6. Add more Python modules or packages


Example
-------

See [here][3] for an example.


License
-------

[MIT][4]


[1]: https://github.com/mitsuhiko/click
[2]: https://github.com/fabric/fabric
[3]: https://github.com/RussellLuo/cmdr/tree/master/example
[4]: http://opensource.org/licenses/MIT
