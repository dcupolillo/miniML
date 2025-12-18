from setuptools import setup, find_packages

setup(
    name='miniML',
    version='0.1.0',
    author='delvendahl',
    homepage='https://delvendahl.github.io/miniML/intro.html',
    description='Mini machine learning package for electrophysiology',
    packages=find_packages(),
    install_requires=[
        'scikit-learn==1.6.1',
        'matplotlib==3.8.2',
        'h5py==3.10.0',
        'pandas==1.5.3',
        'numpy==1.23.5',
        'scipy==1.10.1',
        'tensorflow==2.8.0',
        'pyabf==2.3.8',
    ],
    python_requires='>=3.9',
)
