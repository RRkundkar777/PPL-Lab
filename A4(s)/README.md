# About
In this assignmnet we obtained graphical representation of Cfg Dumps

Graphical Representation helps us to analyse the dumps easily and quickly

 
## Commands used
```
gcc filename.c -fdump-tree-cfg-graph or gcc filename.c -fdump-tree-all-graph
#Graphviz
sudo apt-get install graphviz
dot -Tpng filename.c.011t.cfg.dot -o filename.png
```
 
## References
```
GCC developer options
https://gcc.gnu.org/onlinedocs/gcc/Developer-Options.html
```