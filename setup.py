"""
Project setup
"""
import os

from setuptools import find_namespace_packages, find_packages, setup


def get_long_description():
    root = os.path.dirname(__file__)
    with open(os.path.join(root, "README.md")) as f:
        description = f.read()
    return description


base_requirements = {

}

dev = {"isort", "pre-commit", "pylint", "black", "pycln", "pyright"}

setup(
    name="template",
    version="0.0.1",
    description="Project template",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    python_requires=">=3.9",
    zip_safe=True,
    include_package_data=True,
    packages=find_namespace_packages(),
    # entry_points={
    #     "console_scripts": ["cmd = template.main:app"],
    # },
    install_requires=list(base_requirements),
    extras_require={
        "dev": list(dev),
    },
)
