from setuptools import setup

setup(
    name='PomoApp-CLI',
    version='1.0',
    packages=['cli','cli.commands'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_point="""
        [console_scripts]
        pomoapp=cli.cli:cli
    """,    
)

