from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="qwhale_client",  # How you named your package folder
    packages=["qwhale_client"],  # Chose the same as "name"
    include_package_data=True,
    version="v0.1.4",  # Start with a small number and increase it with every change you make
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="Python client for Qwhale API",  # Give a short description about your library
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yehoyada.s",  # Type in your name
    author_email="hvuhsg6@gmail.com",  # Type in your E-Mail
    url="https://qwhale.ml",  # Provide either the link to your github or to your website
    download_url="https://github.com/hvuhsg/qwhale_client/archive/0.1.10.tar.gz",
    keywords=[
        "API",
        "Client",
        "Qwhale",
        "QWhale",
        "client",
        "storage",
        "MongoDB"
    ],  # Keywords that define your package best
    install_requires=["pymongo", "requests"],  # I get to this in a second
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
