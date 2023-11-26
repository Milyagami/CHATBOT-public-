from Fonctions import *

if __name__ == '__main__':

    # partie principal
    fichiers_texte = [
        "Nomination_Chirac1.txt",
        "Nomination_Chirac2.txt",
        "Nomination_Giscard dEstaing.txt",
        "Nomination_Hollande.txt",
        "Nomination_Macron.txt",
        "Nomination_Mitterrand1.txt",
        "Nomination_Mitterrand2.txt",
        "Nomination_Sarkozy.txt"
    ]
    nom_du_fichier = "Nomination_Chirac1.txt"
    nom_du_president = extraire_nom_president(nom_du_fichier)
    ########################################################
    prenom_president=prenom_president(nom_du_president)
    ########################################################
    print("\nLe président est :",prenom_president, nom_du_president)
    ########################################################
    print_bot()
    print("Bienvenue dans la demonstration des quelques fonctions creer qui nous serviront de base pour ce projet.\nToutes le instructions vous seront donné dans ce programme ")

    while True:
        try:
            a = (input("Pour afficher la liste des noms de président des fichiers ainsi que leur conversion en minuscules taper Presidents :\n"))
            if a == 'Presidents':
                break  # Exit the loop if the input is valid
            else:
                print("Oups vous vous êtes trompé, veuillez réessayer")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

    print("\nListe des noms des présidents :", liste_nom_president(fichiers_texte))
    print("")

    while True:
        try:
            b = (input("Bravo, maintenant que vous avez la liste, taper cleaned pour creer un fichier netoyer de toutes les majuscules et caractère speciaux :\n"))
            if b == 'cleaned':
                break  # Exit the loop if the input is valid
            else:
                print("Oups vous vous êtes trompé, veuillez réessayer")
        except ValueError:
            print("Veuillez entrer une commande valide.")

    convertir_fichiers_en_minuscules("./speeches", "txt", "cleaned")
    directory_cleaned = "cleaned"
    supprimer_caracteres_speciaux("cleaned")
    print("")
    print("")

    # Afficher la matrice TF
    print("Commençons maintenant à explorer un peu ces fichiers.\nCommençons par la matrice TF "
          "associant à chaque mot le nombre de fois qu’il apparait dans la chaine de caractères:")
    print("")
    print(compute_tf(directory_cleaned))

    # Calculer et afficher l'IDF
    print("\nVoici maintenant IDF, qui va retourner un dictionnaire associant à chaque mot son score:")
    idf = calculate_idf(directory_cleaned)
    print("")
    print(idf)

    # Calculer la matrice TF-IDF
    while True:
        try:
            c = (input("Maintenant que nous avons TF et IDF, calculons la Matrice TF-IDF, pour cela taper TF-IDF:\n"))
            if c == 'TF-IDF':
                break  # Exit the loop if the input is valid
            else:
                print("Oups vous vous êtes trompé, veuillez réessayer")
        except ValueError:
            print("Veuillez entrer une commande valide.")
    print("\nMatrice TF-IDF:")
    tf_idf_matrix = compute_tf_idf(directory_cleaned)
    print("")
    print(tf_idf_matrix)


    print("Maintenant que nous avons TF-IDF nous pouvons enfin avoir la liste des information importantes dans nos textes.\n"
    "Vous trouverez donc la liste de ce que nous pouvons tirer de cette matrice.")
    print("")
    print("")
    # Récupérer les mots non importants et les afficher
    print("\nListe des mots non importants :")
    word_doc_count, _ = compute_tf(directory_cleaned)
    non_important_words = get_non_important_words(tf_idf_matrix, word_doc_count)
    print(non_important_words)
    #######

    word, highest_tfidf = get_word_with_highest_tfidf(directory_cleaned)
    print("\nMot associé au plus grand score TF-IDF :", word)
    print("\nScore TF-IDF le plus élevé :", highest_tfidf)

    ####

    # Recherche du fichier associé au président Chirac
    fichier_chirac = None
    for filename in os.listdir(directory_cleaned):
        nom_du_president = extraire_nom_president(filename)
        if nom_du_president == "Chirac":
            fichier_chirac = os.path.join(directory_cleaned, filename)
            break

    # Calcul de la fréquence des mots dans le discours de Chirac
    if fichier_chirac:
        mots_chirac = compute_tf2(fichier_chirac)

        # Trouver le mot le plus fréquent utilisé par Chirac
        mot_plus_frequent = max(mots_chirac, key=mots_chirac.get)

        # Affichage du mot le plus fréquent utilisé par Chirac
        print("")
        print(f"Le mot le plus fréquent utilisé par le président Chirac est : {mot_plus_frequent}")
    else:
        print("Aucun discours trouvé pour le président Chirac dans le dossier.")

    ########################

    # Initialisation des variables pour le mot "Nation"
    mot_a_rechercher = "nation"
    nombre_max_repetitions = 0
    presidents_avec_nation = []

    # Parcours de tous les fichiers pour trouver le nombre de répétitions du mot "Nation" par président
    for filename in os.listdir(directory_cleaned):
        nom_du_president = extraire_nom_president(filename)
        fichier = os.path.join(directory_cleaned, filename)
        mots_president = compute_tf2(fichier)

        if mot_a_rechercher in mots_president:
            nombre_repetitions = mots_president[mot_a_rechercher]
            if nombre_repetitions > nombre_max_repetitions:
                nombre_max_repetitions = nombre_repetitions
                presidents_avec_nation = [nom_du_president]
            elif nombre_repetitions == nombre_max_repetitions:
                presidents_avec_nation.append(nom_du_president)

    # Affichage des présidents ayant parlé de la "Nation" et celui qui l'a répété le plus de fois
    if presidents_avec_nation:
        print("")
        print(f"Présidents ayant parlé de la 'Nation': {', '.join(presidents_avec_nation)}")
        print("")
        print(f"Président qui a répété le plus de fois le mot 'Nation': {', '.join(presidents_avec_nation)} avec {nombre_max_repetitions} répétitions.")

    ########################

    first_president_climate_ecology = detect_first_president_to_mention("cleaned")
    print("")
    print(f"Le premier président à mentionner le climat ou l'écologie est : {first_president_climate_ecology}")
