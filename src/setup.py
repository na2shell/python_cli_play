from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name="samplecli",
    version="0.0.1",
    description="A small package",
    author="hgoe_hoge_bar",
    packages=find_packages(),
    py_modules=["sample_hoge.lib"],
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "sample_hoge=sample_hoge.core:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ]
)
