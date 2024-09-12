from setuptools import setup 
import app

setup(
    version = app.__version__,
    packages = ['app'],
    entry_points = {
        'console_scripts': [
            'addcom = app.main:app' 
        ]
    },
    install_requires = app.__dependencies__
)