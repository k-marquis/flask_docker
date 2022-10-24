from setuptools import setup

setup(
    name='PomoApp-CLI',
    version='0.1.0',
    packages=['cli','cli.commands'],
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'pomoapp=cli.cli:cli',
        ],
    },
)

