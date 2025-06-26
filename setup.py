from setuptools import setup

setup(
    name='ReconVeritas',
    version='1.0.0',
    py_modules=['recon-suite'],
    entry_points={
        'console_scripts': [
            'reconveritas = recon-suite:main',
        ],
    },
    install_requires=[
        'requests',
        'beautifulsoup4',
        'colorama'
    ],
)
