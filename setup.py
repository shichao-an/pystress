from setuptools import setup


def get_version():
    with open('pystress.py') as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def get_long_description():
    desc = None
    with open('README.rst') as f:
        desc = f.read()
    return desc


setup(
    name='pystress',
    version=get_version(),
    description="Simple CPU stresser in Python",
    long_description=get_long_description(),
    keywords='pystress',
    author='Shichao An',
    author_email='shichao.an@nyu.edu',
    url='https://github.com/shichao-an/pystress',
    license='BSD',
    py_modules=['pystress'],
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'pystress = pystress:_main',
        ],
    },
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
    ],
)