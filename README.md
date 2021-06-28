# Description
This project is aiming for providing SQL autocomplete functionality. And part of the code is based on litecli, which many people use that make sure part of the core functionality is nearly bug-free. By standing on the shoulders of giants, make improvements and add more functionality. 

# Features
1. flexible keywords and SQL functions setting: providing the interface to adjust the keyword and SQL functions that the program can use and providing config options to adjust them.
2. more fitting MariaDB: 
    1. when using MariaDB would execute fetching KEYWORDS INFORMATION_SCHEMA commands for getting current MariaDB server keywords and SQL functions name.

# Competitive product analysis
Listing about this project do what imporvement that better than other SQL autocomplete tools(such as litecli ... etc)

# Development
```shell
pip install -r requirements.txt
```


# TODO LIST
- [ ] implement MariaDB/MySQL's version [sqlexecute class](https://github.com/dbcli/litecli/blob/master/litecli/sqlexecute.py)
    would use the same interface as litecli's sqlexecute class for compatibility. Do this because litecli is connecting to sqllite.
- [ ] reuse total or most of litecli's completion_refresher code
      check compatibility and fixing it. And on top include litecli's [BSD 3-Clause](https://github.com/dbcli/litecli/blob/22ff7eaf1775ecd272a111bbb344cecc8d1f7c5a/LICENSE)
- [ ] when using MariaDB and MariaDB's server support KEYWORDS, SQL_FUNCTIONS INFORMATION_SCHEMA then fetching them as autocompleter's keywords and sql_functions
- [ ] ...