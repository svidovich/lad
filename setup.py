from setuptools import setup

# yapf: disable
setup(
    name='linux-allocated',
    version='0.1',
    url='https://github.com/svidovich/lad',
    author='svidovich',
    author_email='samuel.vidovich@gmail.com',
    license='MIT',
    packages=['lad'],
    package_data={'lad': ['data/*.txt']}
)
# yapf: enable
