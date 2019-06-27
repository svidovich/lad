## TODO: Make this a true python package that one can install. Then, put in on PYPI. Let's get more LADs in before that last step, shall we?

# lad

Linux allocated devices parsing library for python.

Use:

`from lad import convert`

`major_minor = convert('sda5')` or

`name = convert('8:6')`

That's all.

## Why this implementation is good

It only loads what it needs to when it needs to. It does so quickly.

## Why this implementation is bad

I need help. There are a lot of LADs.
