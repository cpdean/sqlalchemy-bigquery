__version__ = '0.0.1a'

from sqlalchemy.dialects import registry

registry.register("bigquery", "sqlalchemy_bigquery.pyodbc", "BigQueryDialect_pyodbc")
registry.register("bigquery.pyodbc", "sqlalchemy_bigquery.pyodbc", "BigQueryDialect_pyodbc")
