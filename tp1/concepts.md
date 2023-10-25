# Concepts:

- word vector basis (Like B and T)
- context word
- Similarity
- Clustering
- co-occurrence matrix
- Point-wise mutual information (as weight)


### co-occurrence matrix
Prend deux mots et retourne le nombre de fois ou le deuxième mot apparaît dans la fenêtre de contexte (pour une fenêtre de context choisie) du premier mot: (m1: str, m2: str) -> int

### Point-wise mutual information (as weight)
Est une mesure de probabilité pour mesurer la force d'association entre deux mots dans un corpus de texte.

$$PMI(A, B) = log_2(\frac{P(A,B)}{P(A)*P(B)})$$


