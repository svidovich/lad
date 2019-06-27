# lad

Linux allocated devices parsing library for python.

Use:

`from lad import lad`

`major_minor = lad.convert('sda5')` or

`name = lad.convert('8:6')`

That's all.

## Why this implementation is good

It only loads what it needs to when it needs to. It does so quickly.

## Why this implementation is bad

I need help. There are a lot of LADs.

## Find it on pypi!

https://pypi.org/project/linux-allocated/0.1/
