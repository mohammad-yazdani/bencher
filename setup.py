import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csbencher",
    version="0.0.7",
    author="Mohammad Yazdani",
    author_email="yazdani.mohammad106@live.co.uk",
    description="Pain killer for CS courses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohammad-yazdani/bencher",
    packages=['bencher'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ['bencher = bencher.main:run']
    }
)
