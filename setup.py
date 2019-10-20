import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='firefly-iam-context',
    version='0.1',
    author="JD Williams",
    author_email="me@jdwilliams.xyz",
    description="Bounded context for users of your application.",
    long_description=long_description,
    url="https://github.com/firefly19/python-dependency-injection",
    packages=setuptools.PEP420PackageFinder.find('src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
)
