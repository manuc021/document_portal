from setuptools import setup, find_packages

setup(
    name='doucument_portal',
    version='0.1',
    author='Manu Chauhan',
    description='A document portal application',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'streamlit',
    ],
)