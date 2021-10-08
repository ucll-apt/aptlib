from setuptools import setup


setup(name='aptlib',
      version='0.1.0',
      description='APTLib',
      url='http://github.com/ucll-apt/aptlib',
      author='Frederic Vogels',
      author_email='frederic.vogels@ucll.be',
      license='MIT',
      packages=['aptlib'],
      install_requires = [
          'GitPython',
          'pydriller',
          'colorama',
          'termcolor',
      ],
      zip_safe=False)