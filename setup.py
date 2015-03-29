import os
import re

from setuptools import setup

v = open(os.path.join(os.path.dirname(__file__), 'sqlalchemy_bigquery', '__init__.py'))
VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(v.read()).group(1)
v.close()

readme = os.path.join(os.path.dirname(__file__), 'README.md')


setup(name='sqlalchemy_bigquery',
      version=VERSION,
      description="BigQuery for SQLAlchemy",
      long_description=open(readme).read(),
      classifiers=[
      'Development Status :: 3 - Alpha',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: Implementation :: CPython',
      'Topic :: Database :: Front-Ends',
      ],
      keywords='SQLAlchemy Google BigQuery',
      author='Conrad Dean',
      author_email='conrad.p.dean@gmail.com',
      license='MIT',
      packages=['sqlalchemy_bigquery'],
      include_package_data=True,
      tests_require=['py.test'],
      zip_safe=False,
      entry_points={
         'sqlalchemy.dialects': [
              'bigquery = sqlalchemy_bigquery.pyodbc:BigQueryDialect_pyodbc',
              'bigquery.pyodbc = sqlalchemy_bigquery.pyodbc:BigQueryDialect_pyodbc',
              ]
        }
)
