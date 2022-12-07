from setuptools import setup, find_packages


setup(
    name='pippychippyprod',
    version='1.0.0',
    author="Matyas aka chip",
    author_email='mkrizek@dons.usfca.edu',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)