from setuptools import setup, find_packages

setup(
    name='pyhdl',
    version='0.1.0',
    description='Python to VHDL converter',
    long_description='PYHDL - A tool to convert Python-like syntax to VHDL',
    author='PYHDL Team',
    author_email='pyhdl@example.com',
    url='https://github.com/pyhdl/pyhdl',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'pyhdl=tokenizer:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Compilers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.7',
    install_requires=[],
)

