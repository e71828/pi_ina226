try:
    # Try using ez_setup to install setuptools if not already installed.
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    # Ignore import error and assume Python 3 which already has setuptools.
    pass

from setuptools import setup

DESC = ('This Python library for Raspberry Pi makes it easy to leverage the '
        'complex functionality of the Texas Instruments INA226 '
        'sensor to measure voltage, current and power.')

classifiers = ['Development Status :: 5 - Production/Stable',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: 3.6',
               'Programming Language :: Python :: 3.7',
               'Topic :: System :: Hardware :: Hardware Drivers']

# Define required packages.
requires = ['smbus2']


def read_long_description():
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        return ""


setup(name='pi-ina226',
      version='0.1.0',
      author='e71828',
      author_email='740943170@qq.com',
      description=DESC,
      long_description=read_long_description(),
      license='MIT',
      url='https://github.com/e71828/pi_ina226/',
      classifiers=classifiers,
      keywords='ina226 raspberrypi',
      install_requires=requires,
      test_suite='tests',
      py_modules=['ina226'])
