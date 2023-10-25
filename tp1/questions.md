# Questions

C'est quoi la longueur du text B.txt ?
Combien de mots doit contenir B.txt ?

Pourquoi parle-t-on des word sets T et B ? C'est quoi leur signification ?

----------------------------------------------------------

Comment faire un compte des occurences dans numpy ?

```python
import numpy as np

x = np.array([1,1,1,2,2,2,5,25,1,1])
unique, counts = np.unique(x, return_counts=True)

print(np.asarray((unique, counts)).T)
# [[ 1  5]
#  [ 2  3]
#  [ 5  1]
#  [25  1]]
```

----------------------------------------------------------
