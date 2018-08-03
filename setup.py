from setuptools import setup
setup(
    name='troper_thinker',
    packages=['troper_thinker'], # this must be the same as the name above
    install_requires=['numpy', 'sklearn', 'requests', 'bs4'],
    py_modules=['scorer', 'store'],
    version='0.0.1',
    # description='Missing data visualization module for Python.',
    # author='Aleksey Bilogur',
    # author_email='aleksey.bilogur@gmail.com',
    url='https://github.com/ResidentMario/troper-thinker',
    # download_url='',
    # keywords=['data', 'data visualization', 'data analysis', 'missing data', 'data science', 'pandas', 'python'],
    classifiers=[]
)