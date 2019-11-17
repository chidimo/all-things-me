# The `relational model`, `RM`

1. The `relational model` is the conceptual base of all `RDBMS`.
1. The basic object of the relational model is the `relation`.
1. `relation`: abstract concept; `table`: concrete implementation
1. `relation` in `RM` is equivalent to a `table` in DB terms
1. A `row` in a `DB` table is equivalent to a `tuple` in the `RM`. Other terms are `n-tuple`, `record`, `vector`.
1. In a `relation`, the order of rows is irrelevant. But that is not necessarily the case in a `DB` table.
1. A `column` in a `DB` table is equivalent to an `attribute` in the `RM`.
1. A `domain` describes a set of possible values for a given `attribute`.
1. A `column type` in a `DB` table is roughly equivalent to the `domain` in `RM`.
1. A `relation` cannot contain identical tuples.

## `key`s

1. For a given `relation`, a key is the `minimum` set of `attribute`s that uniquely identifies a tuple.
1. In each `relation`, there may be multiple possible `key`s. These `key`s are called `candidate key`s, `CK`.
1. The `primary key` is that which is chosen from among all the `CK`s to uniquely identify a tuple.
1. To select a `PK`, there are three criteria to consider: brevity, simplicity, context (the most logical and intelligible to human beings)
1. If no `CK` meet these three criteria, an `artificial key`, `AK` can be used.
1. `AK` are popular with `DB`s as it is the best suited for better scalability and less processing time.

### `foreign key`s

1. Their purpose is to create links between `relation`s (=tables).
1. A `FK` of `relation` A is said to reference the `PK` of `relation` B.
1. `data redundancy` means storing one information in more than one place.

### Redundant tables

1. In a `relation`, if an `attribute`, `A` depends uniquely on a group of `attribute`s, `G`, then we can create a new `relation` that will contain the `attribute`s of both A and G. In this new `relation`, G would be the candidate key.
1. Any `attribute`s that uniquely depends on G should be moved to a separate table.

### Association tables

1. `cardinality` is the degree of `relation` e.g `One-to-One`, `One-to-Many`, `Many-to-Many`.
1. Modelling `Many-to-Many` relationship can be solved using `association table`s. `AT` consists of at least two `FK`, each of which references one of the two tables in question. But it is sometimes necessary to add additional `column`s to the key

## `relational algebra`, `RA`

1. This refers to data manipulation in the `RM`
1. In the `RM`, anything that has to do with data manipulation is called `relational algebra`.
1. The primary operations are `projection` (`SELECT`) and `restriction` (`WHERE`).
1. `projection` means selecting only the `attribute`s of a relation that we want to see. We say that we **`project` the `relation` unto its `attribute`s** . In `DB` terms, it means to extract `column`s from a table.
1. `restriction`: returns only `tuple`s that meet a `filtering condition`. In DB terms it means extracting `row`s.
1. `projection` and `restriction` are `unary` operations. This means that they are defined on a single `relation`.

    ```sql
    a = Projection (relation, attribA, ...)
    b = Restriction(relation, filtering-condition)
    ```

1. The `union` of two `relation`s of the same schema, `R1` and `R2`, produces a third relation, `R3`, also of the same schema, containing all of the `tuple`s of `R1` and `R2`.
1. The `difference` between an `R3` and an `R2` `relation` results in an `R1` `relation` containing all of the `tuple`s of `R3` that are not found in `R2`.
1. The `intersection` between two `relation`s `R1` and `R2` results in a third `relation`, `R3`, containing only the `tuple`s that are found in both `R1` and `R2`.

    ```sql
    R1 union R2
    R1 difference R2
    R1 intersection R2
    R1 Product R2
    ```

1. The `union`, `intersection` and `difference` between two tables can only be computed if the two tables have the same set of `column`s.

1. In `RA`, the `Cartesian product` of two `relation`s, `R1` and `R2` represents all of the possible combinations of `R1` and `R2` `tuple`s.
1. The `Cartesian product` between a `relation` with 3 `tuple`s and a `relation` with 4 `tuple`s results in a `relation` of 12 `tuple`s!
1. To perform the `CP` of two tables in a `DB`, we use the `SELECT` statement while specifying the two tables.

## `join`

1. It is perhaps the most foundational concept in `RA`.
1. Implementing a `join` requires that a `join condition` be specified.
1. In a `join`, the `FK` of one `table` references a `CK` of another table. This `CK` is often a `PK`.
1. It's also possible to join multiple `column`s.
1. `inner join`: This produces a `table` that only contains `row`s for which the `FK` of the first `table` has a match in the `PK` of the second table.
1. `outer join`: retain all `row`s in one of both `relation`s, regardless of whether they have a match in the other `relation`.
1. `left outer join`: retain all `row`s in the `left` `relation`
1. `right outer join`: retain all `row`s in the `right` `relation`.
1. `full outer join`: retain all `row`s in `both` relations.
1. `natural join`: This can happen if the two relations being joined have `attribute`s that appear in both. The join will be *implicit* and based on this common `attribute`.

    ```sql
    Join (relation1, relation2, relation1.attribute_name = relation2.attribute_name)

    For right, left, and full outer joins:
    JoinLeft (relation1, relation2, relation1.attribute_name = relation2.attribute_name)
    JoinRight (relation1, relation2, relation1.attribute_name = relation2.attribute_name)
    JoinFull (relation1, relation2, relation1.attribute_name = relation2.attribute_name)

    # join on FK and PK
    inner_join = rows (relation1.FK = relation2.CK (CK is often a PK))

    # join multiple columns
    relation1.attribute1 = relation2.attribute3 AND relation1.attribute2 = relation2.attribute4
    ```

## Aggregation

1. Used to perform computation over multiple `row`s of a table.
1. A proper aggregation consists of two elements (resulting in a two steps)
    1. `partitioning attribute`: used to form groups in which all elements have the same value for the attribute specified by the `PA`.
    1. `aggregate function`: e.g. average. function to be applied to a group of multiple rows.

`MapReduce` as an `aggregation` function

|      `MapReduce`     |    `aggregation`   |
| -------------------- | ------------------ |
| Information chunk    | 1 row of table |
| Key                  | Partitioning attributes |
| Value                | Attributes sent to the aggregate function
| Reduce function      | Aggregate Function

## SQL

`SQL` (Structured Query Language) offers three command categories:

1. `DDL` (Data Definition Language), used to create or delete objects in a `DB` (tables, constraints, etc.).
1. `DCL` (Data Control Language), used to manage users and control their access rights (view, modify, etc.).
1. `DML` (Data Manipulation Language), used to manipulate the data contained in the table—that is, to manipulate the rows of the tables. The four available operations are:
    1. Insert rows
    1. Read rows
    1. Update rows
    1. Delete rows

```sql
# projection
SELECT * FROM table;

# projection with restriction
SELECT * FROM table WHERE condition;

# cartesian product
SELECT * FROM table1, table2

# cartesian product with projection
SELECT
    table1.attrA,
    ... # any other attributes
    table2.attrB
FROM table1, table2

# union with projection for common attributes
SELECT attr1, attr2 FROM table1
UNION
SELECT attr1, attr2 FROM table2

# difference with projection for common attributes
SELECT attr1, attr2 FROM table1
EXCEPT
SELECT attr1, attr2 FROM table2

# intersection with projection for common attributes
SELECT attr1, attr2 FROM table1
INTERSECT
SELECT attr1, attr2 FROM table2

# nesting
SELECT *
FROM
    (
        SELECT attr1, attr2 FROM table1
        INTERSECT
        SELECT attr1, attr2 FROM table2
    )
WHERE condition

# join, method 1
SELECT
    table1.attr1,
    table1.id_address,
    table2.attr1,
    table2.attr2,
FROM table1, table2
WHERE table1.attr1 = table2.attr1

# join method 2
SELECT
    table1.attr1,
    table1.id_address,
    table2.attr1,
    table2.attr2,
FROM table1 JOIN table2
ON table1.attr1 = table2.attr1
```

## Entity Relationship Diagram (ERD)

customers -> vendors -> shops
