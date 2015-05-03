"""Say goodbye to you."""


def main(name=''):
    greeting = 'goodbye'
    if name:
        greeting += ', %s' % name
    print(greeting)
