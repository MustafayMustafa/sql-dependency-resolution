# sql-dependency-resolution
A dependency resolution library that performs conflict resolution to create a topological ordering for creating and destroying SQL objects such as views, functions and indexes.


## Usage
* import DependencyResolver.
* use `create_order` and `drop_order` to retrieve dependency ordering.(currently only views are supported).

## caveats
* assumes view name of file is the name of view.
* views must be pre-fixed with `vw` or `mvw`.
* dependecies are collected from join conditions.
## TODO
* implement functions, procedures and indexes.
* auto detect name from header using regex.
* collect dependencies from sql FROM statement.
