# from sqlalchemy.testing.suite import *

import sqlalchemy.sql as sql
from sqlalchemy import func

import sqlalchemy_bigquery
import sqlalchemy_bigquery.base as bq


def test_assert_correct_version():
    """ yep. update it every time """
    assert "0.0.4" == sqlalchemy_bigquery.__version__


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


def test_string_literal_does_not_use_old_sql_quote_escaping():
    s = sql.select([
        func.look_at(sql.column("something") == "here's a single-quote")
    ]).select_from(
        sql.table("something_else")
    ).compile(
        compile_kwargs={"literal_binds": True},
        dialect=bq.BQDialect()
    )
    assert "here''s" not in str(s)


def test_string_literals_correctly_quoted():
    s = sql.select([
        func.look_at(sql.column("something") == "here's a single-quote")
    ]).select_from(
        sql.table("something_else")
    ).compile(
        compile_kwargs={"literal_binds": True},
        dialect=bq.BQDialect()
    )
    assert "here\\'s" in str(s)


def test_string_literals_not_oldstyle_quoted_in_func():
    s = str(
        sql.case(
            [(sql.column("WHOA") == "Jason's", 1)],
            else_=0
        ).compile(
            compile_kwargs={"literal_binds": True},
            dialect=bq.BQDialect()
        )
    )
    assert "Jason's" not in s
