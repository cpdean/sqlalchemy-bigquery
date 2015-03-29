"""
Support for Google BigQuery.

Does not support actually connecting to BQ.
Directly derived from the mssql dialect with minor modifications

"""
import sqlalchemy.dialects.mssql.base as mssql_base


from sqlalchemy.dialects.mssql.base import MSDialect
from sqlalchemy.sql import compiler


class BQSQLCompiler(mssql_base.MSSQLCompiler):
    pass


class BQIdentifierPreparer(compiler.IdentifierPreparer):
    def __init__(self, dialect):
        super(BQIdentifierPreparer, self).__init__(
            dialect, initial_quote='[', final_quote=']'
        )

    def format_label(self, label, name=None):
        """ bq can't handle quoting labels """
        return name or label.name


class BQDialect(MSDialect):
    statement_compiler = BQSQLCompiler
    preparer = BQIdentifierPreparer
