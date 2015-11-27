How to Contribute to the BigQuery SQLAlchemy Dialect
====================================================

It's the goal of this project to provide an easy interface to generate
SQL that's valid for use in BigQuery.

When You Find a Bug
===================

1. Come up with a small example that generates the invalid SQL. Then
   convert your example to a test and add it to the test suite.  Doing
   this already saves everyone a ton of time in understanding the
   nature of the bug.
2. Once you have a failing test that correctly demonstrates the bug,
   make changes to the dialect to make your test pass.
3. Rev the version number.
4. Run the entire test suite! Make sure nothing else broke.
5. Submit a Pull Request.
