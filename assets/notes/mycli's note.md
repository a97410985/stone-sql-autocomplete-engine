## some good autocomplete examples about mycli
### keep view's name so it can be suggested
```SQL
CREATE TABLE t (qty INT, price INT);
CREATE VIEW v AS SELECT qty, price, qty*price AS value from t;
SELECT * FROM [cursor]
```
In [cursor] would suggest 「plays, t, v」. Includes created view's names.