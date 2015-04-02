# from sqlalchemy.testing.suite import *

import sqlalchemy.sql as sql
from sqlalchemy import func

import sqlalchemy_bigquery.base as bq


def test_mixed_case_function_label_not_quoted():
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


def test_mixed_case_column_not_quoted():
    s = sql.select([
        sql.column("Pork")
    ]).compile(
        dialect=bq.BQDialect()
    )
    assert "[Pork]" not in str(s)
    assert "Pork" in str(s)


def test_string_literals_correctly_quoted():
    s = sql.select([
        func.look_at(sql.column("something"), "here's a single-quote")
    ]).select_from(
        sql.table("something_else")
    ).compile(
        compile_kwargs={"literal_binds": True},
        dialect=bq.BQDialect()
    )
    assert "here''s" not in str(s)
    assert "here\'s" in str(s)
