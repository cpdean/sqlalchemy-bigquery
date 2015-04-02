BigQuery dialect for SQLAlchemy.

BigQuery implements a DSL that is similar to SQL with a few quirks:

1. It has a "group each by" hint for grouping over large amounts of data
2. You need to use the "join each ... on" form when joining on a table larger than a small number of megabytes.
3. You can't quote columns, but you can quote tables. But probably not table aliasess.
4. Because you can't quote columns, you are limited to colums with no spaces, only alpha-numeric characters with underscores, and you can only start a column with a letter or underscore


The first two issues (the non-standard "each" modifier for grouping and joining) has not been addressed yet.  BigQuery pushes the responsibility of when to recognize a table is too big for certain operations, and shifts burden onto you when you want to use those modifiers.  Sometimes you need them, sometimes you don't.  Leaving this as an exercise to the user to just string replace those out of what this dialect returns.


### Usage

There currently isn't support for using sqlalchemy to connect to
BigQuery.  Currently there's only support for generating SQL to send
in a regular service call.


To Install::

    pip install sqlalchemy-bigquery

Usage Example::

    >>> import sqlalchemy.sql as sql
    >>>
    >>> from sqlalchemy import func
    >>> import sqlalchemy_bigquery.base as bq
    >>>
    >>>
    >>> country = sql.column("country")
    >>> fruit_type = sql.column("fruit_type")
    >>> calories = sql.column("calories")
    >>> total_usa = func.sum(
    ...     sql.case(
    ...         [(country == "usa", 1)],
    ...         else_=0
    ...     )
    ... ).label("Total_in_USA")
    >>> total_japan = func.sum(
    ...     sql.case(
    ...         [(country == "japan", 1)],
    ...         else_=0
    ...     )
    ... ).label("Total_in_Japan")
    >>> s = sql.select([
    ...     fruit_type,
    ...     total_usa,
    ...     total_japan,
    ... ]).select_from(sql.table("fruit.table")
    ... ).group_by(
    ...     fruit_type
    ... ).compile(
    ...     compile_kwargs={"literal_binds": True},
    ...     dialect=bq.BQDialect()
    ... )
    >>> print str(s)
    SELECT fruit_type, sum(CASE WHEN (country = 'usa') THEN 1 ELSE 0 END) AS Total_in_USA, sum(CASE WHEN (country = 'japan') THEN 1 ELSE 0 END) AS Total_in_Japan
    FROM [fruit.table] GROUP BY fruit_type
