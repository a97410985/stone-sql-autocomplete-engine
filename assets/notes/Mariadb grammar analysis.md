[important source](https://gist.github.com/a97410985/8c0a04b1e95335c2c3114721ccc6edce)

## Some ways to inference the last token suggestion
(notes: litecli part of core autocomplete feature is based on last token suggestion)
use `terminal symbol` as an inference point is a good choice. For example, the `VIEW` keyword is represented by Mariadb as `VIEW_SYM`, the Grammar rules that appear `VIEW_SYM` are 151, 153, 1085, 1087, 1258, 1297 2106, 2292, 3074, 3510, 3511. List them below.
```text*
Line 208:    151  create: create_or_replace definer_opt opt_view_suid VIEW_SYM opt_if_not_exists table_ident $@20 view_list_opt AS view_select
Line 212:    153  create: create_or_replace view_algorithm definer_opt opt_view_suid VIEW_SYM opt_if_not_exists table_ident $@21 view_list_opt AS view_select
Line 1596:   1085 alter: ALTER view_algorithm definer_opt opt_view_suid VIEW_SYM table_ident $@93 view_list_opt AS view_select stmt_end
Line 1600:   1087 alter: ALTER definer_opt opt_view_suid VIEW_SYM table_ident $@94 view_list_opt AS view_select stmt_end
Line 1841:   1258 repair_table_or_view: VIEW_SYM $@111 table_list opt_view_repair_type
Line 1905:   1297 check_view_or_table: VIEW_SYM $@116 table_list opt_view_check_type
Line 3035:   2106 drop: DROP VIEW_SYM opt_if_exists $@172 table_list opt_restrict
Line 3318:   2292 show_param: CREATE VIEW_SYM table_ident
Line 4243:   3074 keyword_sp_var_and_label:  VIEW_SYM
Line 4775:   3510 object_privilege: CREATE VIEW_SYM
Line 4776:   3511 object_privilege: SHOW VIEW_SYM
```
We can observe that similar pattern list below($@111 like symbol is empty)
1. VIEW_SYM opt_if_not_exists table_ident
2. VIEW_SYM table_ident
3. VIEW_SYM table_list

So when the cursor after `VIEW TOKEN` in one token, the autocompleter can suggest `table names`

This way can do by the programmer to observe rules. And maybe can write a program analysis of these rule and generate some rules for the suggestion type