from setuptools import setup, find_packages

setup(
    name='reconveritas',
    version='1.0.0',
    author='Aditya Goswami',
    author_email='your-email@example.com',
    description='A complete recon automation suite for offensive security assessments.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Aditya-Sec/ReconVeritas-Automated-Recon-Tool',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['recon-suite'],
    install_requires=[
        'requests',
        'dnspython'
    ],
    entry_points={
        'console_scripts': [
            'reconveritas = recon-suite:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Linux',
        'Topic :: Security',
    ],
    python_requires='>=3.6',
)
