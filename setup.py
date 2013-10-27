from setuptools import setup


def get_version():
    with open('pystress.py') as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


setup(
    name='pystress',
    version=get_version(),
    description="Simple CPU stresser in Python",
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
)