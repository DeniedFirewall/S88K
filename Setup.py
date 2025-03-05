from setuptools import setup, find_packages

setup(
    name="S88K",
    version="0.1",
    packages=find_packages(),
    description="S88K: A Wi-Fi pentesting library built from scratch",
    author="deniedfirewall",
    author_email="everunner673@gmail.com",
    url="https://github.com/deniedfirewall/S88K",
    license="MIT",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "s88k-cli=S88K.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Security",
    ],
)
