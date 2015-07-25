"""installation setup file"""

from setuptools import setup

setup(name='pylang',
      description='Multiple language installer',
      version='0.1.0',
      author='Harsha Srinivas',
      author_email='95harsha95@gmail.com',
      packages=['pylang'],
      entry_points={
          'console_scripts': ['pylang=pylang:main'],
      },
      url='https://github.com/harshasrinivas/pylang/',
      keywords=['languages', 'installer', 'CLI', 'python'],
      classifiers=[
          'Operating System :: POSIX',
          'Environment :: Console',
          'Topic :: System :: Installation/Setup',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Topic :: Utilities',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],)
