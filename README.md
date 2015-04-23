Goodjob-Pyjobs
==============

A helper provider for integrating Python modules/packages into `Goodjob` more easily.


Why Goodjob-Pyjobs?
-------------------

In [Goodjob][1], job commands (so-called `provider`) can only be provided as standalone executables (e.g. Bash scripts or Python Scripts) with full path.

### Before using Goodjob-Pyjobs

For Python scripts, if we want to use our own scripts as providers in `Goodjob`, we must follow the steps below:

1. Create an **executable** Python script:

        $ vi /tmp/demo/jobs/hello.py

        #!/usr/bin/env python

        def main():
            print('hello')

        if __name__ == '__main__':
            main()

2. Use it as the provider **with full path** to create a job:

        $ curl -X POST ... -d '{
            "name": "greet",
            "provider": "python /tmp/demo/jobs/hello.py"
        }' ...

The provider will be executed directly on the server where `Goodjob` services are running.

### After using Goodjob-Pyjobs

With `Goodjob-Pyjobs`, we can use Python modules or packages as providers:

1. Set the `JOBS_PATH` configuration in a YAML file:

        $ vi /tmp/demo/goodjob_pyjobs.yml

        JOBS_PATH: /tmp/demo/jobs

2. Create a Python module:

        # Note here:
        # the module "hello.py" is located in `JOBS_PATH`
        # (i.e. "/tmp/demo/jobs").

        $ vi /tmp/demo/jobs/hello.py

        # A function named "main" is defined here,
        # since the default `ENTRY_POINT` is "main".
        # You can customize it by setting your preferred
        # entry point name as `ENTRY_POINT` in the YAML file.

        def main():
            print('hello')

3. Use it as the provider (with module name) to create a job:

        $ curl -X POST ... -d '{
            "name": "greet",
            "provider": "goodjob-pyjobs-provider hello"
        }' ...

Note that new Python modules or packages can be added at any time, and dynamically (without restarting any `Goodjob` services).


Installation
------------

Install development version from `GitHub`:

    $ git clone https://github.com/RussellLuo/goodjob-pyjobs.git
    $ cd goodjob-pyjobs
    $ python setup.py install


Example
-------

See [here][2] for example.


License
-------

[MIT][3]


[1]: https://github.com/RussellLuo/goodjob
[2]: https://github.com/RussellLuo/goodjob-pyjobs/tree/master/example
[3]: http://opensource.org/licenses/MIT
