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

Est-ce que les namedtuples peuvent avoir des membres variable ?

Réponse: Non, tout les attributs d'un named tuple sont immutable.

```python
from collections import namedtuple
Student = namedtuple("Student", "name grades")
s1 = Student("Fabrice", [1, 2, 3, 4, 5, 6])
# Va retourner une erreur: immutable
s1.grades = [5, 5, 5, 5, 5, 5]
```

----------------------------------------------------------

Comment faire un PCA avec scikit-learn ?

```python
from sklearn.decomposition import KernelPCA
kpca = KernelPCA(n_components = 2, kernel = 'rbf')
X_train = kpca.fit_transform(X_train)
X_test = kpca.transform(X_test)
```

----------------------------------------------------------

Comment sélectionner toutes les colonnes sauf la première dans pandas ?

```python
df_sauf_premiere = df.iloc[:, 1:]
```

