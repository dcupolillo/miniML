from setuptools import setup

setup(
    name='miniML',
    version='0.1.0',
    description='Mini machine learning package for electrophysiology',
    packages=['', 'core', 'core.FileImport'],
    package_dir={'': '.'},
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
