Example
=======

A simple example that shows how to use `Goodjob-Pyjobs`.


Usage
-----

1. Install Goodjob-Pyjobs

        $ cd /tmp
        $ git clone https://github.com/RussellLuo/goodjob-pyjobs.git
        $ cd goodjob-pyjobs
        $ pip setup.py install

2. Configure YAML file

        $ vi example/goodjob_pyjobs.yml

3. Set environment variable

        $ export GOODJOB_PYJOBS_CONFIG_YAML=/tmp/goodjob-pyjobs/example/goodjob_pyjobs.yml

4. Run jobs

        $ goodjob-pyjobs-provider hello
        $ goodjob-pyjobs-provider goodbye
