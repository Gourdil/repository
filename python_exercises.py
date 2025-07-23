# Exercice 1 : Entrées utilisateur et prise de décision
# Demande à l'utilisateur son âge et affiche un message selon qu'il est mineur, adulte ou senior
def check_age():
    age = int(input("Entrez votre âge : "))
    if age < 18:
        print("Vous êtes mineur.")
    elif age <= 65:
        print("Vous êtes adulte.")
    else:
        print("Vous êtes senior.")

# Exercice 2 : Boucles et opérations sur nombres
# Calcule la somme des nombres pairs de 1 à un nombre donné par l'utilisateur
def sum_even_numbers():
    limit = int(input("Entrez un nombre limite : "))
    total = 0
    for i in range(1, limit + 1):
        if i % 2 == 0:
            total += i
    print(f"La somme des nombres pairs jusqu'à {limit} est : {total}")

# Exercice 3 : Fonctions et chaînes de caractères
# Crée une fonction qui prend une chaîne et retourne le nombre de voyelles qu'elle contient
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Exercice 4 : Listes et boucles
# Crée une liste de nombres saisis par l'utilisateur (jusqu'à ce qu'il entre 0) et affiche le maximum
def find_maximum():
    numbers = []
    while True:
        num = int(input("Entrez un nombre (0 pour arrêter) : "))
        if num == 0:
            break
        numbers.append(num)
    if numbers:
        print(f"Le plus grand nombre est : {max(numbers)}")
    else:
        print("Aucun nombre saisi.")

# Exercice 5 : Dictionnaires et tuples
# Crée un dictionnaire pour stocker des informations sur des étudiants (nom, note)
# et affiche les noms des étudiants ayant une note supérieure à la moyenne
def student_grades():
    students = {}
    while True:
        name = input("Entrez le nom de l'étudiant (ou 'fin' pour arrêter) : ")
        if name == 'fin':
            break
        grade = float(input(f"Entrez la note de {name} : "))
        students[name] = grade
    
    if students:
        average = sum(students.values()) / len(students)
        above_average = [(name, grade) for name, grade in students.items() if grade > average]
        print(f"Moyenne des notes : {average:.2f}")
        print("Étudiants au-dessus de la moyenne :")
        for name, grade in above_average:
            print(f"{name} : {grade}")
    else:
        print("Aucun étudiant saisi.")

# Pour exécuter les exercices, décommentez l'exercice que vous voulez tester
# check_age()
# sum_even_numbers()
# print(count_vowels(input("Entrez une phrase : ")))
# find_maximum()
# student_grades()
</x artifact_id="a4b8e6f2-9c1d-4b7a-8f9e-2c3d5e7b9a1c">
Plan de suivi :
1. **Semaine 1** : Exécute un exercice par jour. Commence par l'exercice 1 et progresse jusqu'au 5. Note les erreurs ou concepts flous.
2. **Semaine 2** : Refais les exercices où tu as eu des difficultés. Modifie légèrement les exercices (par exemple, change les conditions dans l'exercice 1 ou ajoute une contrainte dans l'exercice 4).
3. **Feedback** : Après chaque exercice, vérifie tes réponses. Si tu veux, partage-moi tes résultats ou erreurs, et je te donnerai des explications ou des exercices supplémentaires.
4. **Progression** : Si tu te sens à l’aise, je peux te fournir des exercices plus complexes (par exemple, combinant listes et dictionnaires ou intégrant des fichiers).

Pour commencer, exécute le premier exercice et dis-moi comment ça se passe ou si tu as des questions !