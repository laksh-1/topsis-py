
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Topsis-Laksh-101916002",
    version="0.0.1",
    author="Laksh Mittal",
    author_email="lmittal_be19@thapar.edu",
    description="Package to get topsis score and the respective rank",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/laksh-1/topsis-py",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires='pandas'
)
