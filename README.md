pickle-gzip
=======================
Small library to save and load objects with pickle from disc, with gzip compression. 
    
## Examples:

```python
from gzp import save, load

x = [1,2,3,4]

save(x, "test.dat")

y = load("test.dat") 

print y # prints [1,2,3,4]
```
