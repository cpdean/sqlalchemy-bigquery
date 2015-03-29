# from sqlalchemy.testing.suite import *

import sqlalchemy.sql as sql
from sqlalchemy import func

import sqlalchemy_bigquery.base as bq


def test_mixed_case_column_not_quoted():
    s = sql.select([
        func.sum().label("Pork")
    ]).compile(
        dialect=bq.BQDialect()
    )
    assert "[Pork]" not in str(s)
    assert "Pork" in str(s)


def test_table_is_quoted_with_square_brackets():
    s = sql.select([
        func.sum().label("Pork")
    ]).select_from(
        sql.table("with.dot")
    ).compile(
        dialect=bq.BQDialect()
    )
    assert "[with.dot]" in str(s)
