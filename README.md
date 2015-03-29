BigQuery dialect for SQLAlchemy.

BigQuery implements a DSL that is similar to SQL with a few quirks:

1. It has a "group each by" hint for grouping over large amounts of data
2. You need to use the "join each ... on" form when joining on a table larger than a small number of megabytes.
3. You can't quote columns, but you can quote tables. But probably not table aliasess.
4. Because you can't quote columns, you are limited to colums with no spaces, only alpha-numeric characters with underscores, and you can only start a column with a letter or underscore


The first two issues (the non-standard "each" modifier for grouping and joining) has not been addressed yet.  BigQuery pushes the responsibility of when to recognize a table is too big for certain operations, and shifts burden onto you when you want to use those modifiers.  Sometimes you need them, sometimes you don't.  Leaving this as an exercise to the user to just string replace those out of what this dialect returns.

Making this not quote columns will be fixed, however.


