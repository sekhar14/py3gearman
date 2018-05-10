from setuptools import setup, find_packages

setup(
    name="gearman",
    version="0.2.0",
    author="Sekhar Banarjee",
    author_email="sekharbanarjee14@gmail.com",
    description="Gearman API - Client, worker, and admin client interfaces for Python3",
    long_description="",
    url="https://github.com/sekhar14/py3gearman.git",
    packages=find_packages(exclude=["tests*"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
