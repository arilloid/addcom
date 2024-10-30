from setuptools import setup, find_packages
import app

setup(
    version=app.__version__,
    packages=find_packages(),
    entry_points={"console_scripts": ["addcom = app.main:app"]},
    install_requires=app.__dependencies__,
)
