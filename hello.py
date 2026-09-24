# Exercice 1
nom = "Danko"
prenom = "Jordan"
age = 11
ville = "Yaounde"
taille = 1.80
est_etudiant = True
print(f"votre non est: {nom}")
print(type(nom))
print(f"votre prenom est: {prenom}")
print(type(prenom))
print(f"votre  age est: {age}")
print(type(age))
print(f"votre ville est: {ville}")
print(type(ville))
print(f"votre taille est: {taille}")
print(type(taille))
print(f"votre status est etudiant: {est_etudiant}")
print(type(est_etudiant))

# Exercice 2
score = 18
print(type(score))
score = "dix-huit"
print(type(score))
score = 18.0
print(type(score))
# a) En python une variable peut changer de type au cour du programme
# b) la difference entre les trois est juste que les trois variables sont de type different
# c) on choisis les nom de variable explicite pour eviter les bugs

# Exercice 3
a = 17
b = 5
print(f"a+b = {a + b}, a-b = {a - b}, a*b = {a * b}, a/b = {a / b}")
print(f"a//b = {a // b}, a%b = {a % b}")
print(f"a**b = {a ** b}")
print(f"a>b = {a > b}, a==b = {a == b}, a!=b = {a != b}")
print(f"a>10 = {a > 10} and b<10 = {b < 10}, a>10 = {a > 10} or b<10 = {b < 10}")

# Exercice 4
nombre1 = float(input("entrer le premier nombre"))
nombre2 = float(input("entrer le deuxieme nombre"))
sum = nombre1 + nombre2
diff = nombre1 - nombre2
prod = nombre1 * nombre2
print(f"la somme de {nombre1} et {nombre2} est: {sum}")
print(f"la difference de {nombre1} et {nombre2} est: {diff}")
print(f"le produit de {nombre1} et {nombre2} est: {prod}")

# Exercice 5
prenom = "Alice"
age = input("Quel age avez vous ")
# il y'a l'erreur au niveau du type de age car input donne les type chaine de caractere
print("Bonjour " + prenom + ", vous avez " + age + " ans. ")
print("Dans 5 ans vous aurez " + (age + 5) + " ans. ")
# il y'a erreur au niveau de age + 5 car age et 5 sont de type different 
print("Votre prenom en majuscules : " + prenom.upper())

# Exercice 6
nom_du_produit = input("entrer le nom du produit")
prix_unitaire = float(input("entrer le prix unitaire du produit"))
qté = int(input("quantité acheté"))
reduktion = float(input("entrer un taux de reduction en % "))
reduction = (total * reduktion)/100
total = qté * prix_unitaire
total_reduction = total - reduction
print(f"le total est: {total}")
print(f"la reduction est: {reduction}")
print(f"total apres reduction est: {total_reduction}")
