from pathlib import Path
from setuptools import setup

long_description = (Path(__file__).parent / "README.md").read_text('utf-8').split('# Installation')[0]

setup(
    name="tl",
    version='0.1.8',
    description="pagination and bubble typewriter in translating manga",
    url="https://github.com/kha-white/manga-ocr",
    author="abangtan",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=['tl'],
    include_package_data=True,
    install_requires=[
        "fire",
        "keyboard",
        "loguru",
    ],
    entry_points={
        "console_scripts": [
        'tl = tl:main'
        ]
    },
)
