from collections import Counter
import os
import math
def print_bot():
    print("\033[1;36m")  # Utiliser le code de couleur ANSI pour définir la couleur en cyan brillant (1;36)
    print(r"""
   _____ _           _            
  / ____| |         | |      
 | |    | |__   __ _| |_  
 | |    | '_ \ / _` | __|
 | |____| | | | (_| | |_ 
  \_____|_| |_|\__,_|\__|                                                                                                      
    """)




def extraire_nom_president(nom_fichier):
    # Obtention du chemin absolu du dossier contenant les fichiers
    dossier_speeches = "speeches"

    # Chemin complet du fichier
    chemin_fichier = os.path.join(dossier_speeches, nom_fichier)

    # Obtention du nom du fichier sans extension
    nom_fichier_sans_extension = os.path.splitext(nom_fichier)[0]

    # Suppression du préfixe "Nomination_"
    nom_president = nom_fichier_sans_extension[11:]

    # Initialisation du compteur
    k = 0

    # Parcourir chaque caractère dans la chaîne
    for caractere in nom_president:
        # Vérifier si le caractère est un chiffre
        if caractere in '0123456789':
            # Augmenter le compteur si le caractère est un chiffre
            k += 1

    # Si des chiffres sont trouvés, enlever les derniers k caractères de la chaîne
    if k > 0:
        nom_president_sans_numero = nom_president[:-k]
    else:
        nom_president_sans_numero = nom_president

    return nom_president_sans_numero

def prenom_president(nom_pres):
    prenom_pres=""
    if nom_pres=="Chirac":
        prenom_pres="Jacques"
    elif nom_pres=="Giscard dEstaing":
        prenom_pres="Valérie"
    elif nom_pres=="Hollande":
        prenom_pres="François"
    elif nom_pres=="Mitterrand":
        prenom_pres="François"
    elif nom_pres=="Sarkozy":
        prenom_pres="Nicolas"
    return prenom_pres

def liste_nom_president(fichier__texte):
    noms_presidents_uniques = []
    for fichier in fichier__texte:
        # Extraire le nom du président
        nom_du_president = extraire_nom_president(fichier)
        # Vérifier si le nom est déjà présent dans la liste
        if nom_du_president not in noms_presidents_uniques:
            # Ajouter le nom du président à la liste
            noms_presidents_uniques.append(nom_du_president)
    # Afficher la liste des noms des présidents sans doublons
    return noms_presidents_uniques


def convertir_majuscules_en_minuscules(chemin_fichier_majuscules, chemin_fichier_minuscules):
    # Lire le contenu du fichier en majuscules
    with open(chemin_fichier_majuscules, 'r', encoding='utf-8') as file:
        contenu_en_majuscules = file.read()

    # Convertir le texte en minuscules
    contenu_en_minuscules = contenu_en_majuscules.lower()

    # Écrire le contenu en minuscules dans le nouveau fichier
    with open(chemin_fichier_minuscules, 'w', encoding='utf-8') as file_minuscules:
        file_minuscules.write(contenu_en_minuscules)

    print(f"Conversion de {chemin_fichier_majuscules} à {chemin_fichier_minuscules} terminée.")


def convertir_fichiers_en_minuscules(directory, extension, repertoire_cleaned):
    # Obtenez la liste des fichiers dans le répertoire avec l'extension spécifiée
    fichiers_a_traiter = list_of_files(directory, extension)

    # Création du répertoire cleaned s'il n'existe pas déjà
    chemin_repertoire_cleaned = os.path.join(os.path.dirname(__file__), repertoire_cleaned)
    if not os.path.exists(chemin_repertoire_cleaned):
        os.makedirs(chemin_repertoire_cleaned)

    # Parcourez chaque fichier et effectuez la conversion en minuscules
    for fichier in fichiers_a_traiter:
        chemin_fichier_source = os.path.join(directory, fichier)

        # Créer le chemin pour le nouveau fichier dans le répertoire cleaned
        chemin_fichier_minuscules = os.path.join(chemin_repertoire_cleaned, fichier)

        # Appel de la fonction pour convertir le fichier en minuscules
        convertir_majuscules_en_minuscules(chemin_fichier_source, chemin_fichier_minuscules)


# Fonction pour obtenir la liste des fichiers dans un répertoire avec une certaine extension
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def supprimer_caracteres_speciaux(directory_cleaned):
    # Obtenez la liste des fichiers dans le répertoire "cleaned"
    fichiers_cleaned = [f for f in os.listdir(directory_cleaned) if f.endswith(".txt")]

    # Caractères spéciaux à supprimer sauf apostrophe et tiret
    caracteres_speciaux = "!\"#$%&()*+,./:;<=>?@[\\]^_`{|}~"

    # Parcourez chaque fichier et supprimez les caractères spéciaux
    for fichier in fichiers_cleaned:
        chemin_fichier = os.path.join(directory_cleaned, fichier)

        # Lire le contenu du fichier
        with open(chemin_fichier, 'r', encoding='utf-8') as file:
            contenu = file.read()


        # Supprimer les caractères spéciaux (sauf apostrophe et tiret) à l'aide d'une boucle
        contenu_sans_speciaux = ''.join(caractere if caractere not in caracteres_speciaux or caractere in ["'", "-"] else '' for caractere in contenu)

        # Ajoutez le traitement spécial pour l'apostrophe et le tiret

        # Remplacement des apostrophes et des tirets par des espaces
        contenu_sans_speciaux = contenu_sans_speciaux.replace("'", " ").replace("-", " ")


        # Écrire le contenu sans caractères spéciaux dans le même fichier
        with open(chemin_fichier, 'w', encoding='utf-8') as file:
            file.write(contenu_sans_speciaux)


def compute_tf(corpus_dir):
    word_doc_count = {}
    total_docs = 0

    # Parcourir les fichiers du corpus
    for filename in os.listdir(corpus_dir):
        total_docs += 1
        file_words = set()

        # Lire chaque fichier et compter les mots uniques
        with open(os.path.join(corpus_dir, filename), 'r', encoding='utf-8') as file:
            words = file.read().split()
            file_words.update(set(words))

        # Mettre à jour le dictionnaire avec les mots du document actuel
        for word in file_words:
            if word in word_doc_count:
                word_doc_count[word] += 1
            else:
                word_doc_count[word] = 1

    return word_doc_count, total_docs

def calculate_idf(corpus_dir):
    word_doc_count, total_docs = compute_tf(corpus_dir)
    word_idf = {}

    # Calculer l'IDF pour chaque mot
    for word, doc_count in word_doc_count.items():
        word_idf[word] = math.log(total_docs / doc_count)

    return word_idf

def compute_tf_idf(corpus_dir):
    word_idf = calculate_idf(corpus_dir)
    word_tf_idf_matrix = []

    # Parcourir à nouveau les fichiers du corpus pour calculer TF-IDF
    for filename in os.listdir(corpus_dir):
        file_words = {}

        # Lire chaque fichier et compter les mots
        with open(os.path.join(corpus_dir, filename), 'r', encoding='utf-8') as file:
            words = file.read().split()

            # Compter les occurrences de chaque mot dans le fichier
            word_counts = Counter(words)

            # Calculer TF-IDF pour chaque mot dans le fichier
            file_tf_idf = []
            for word, tf in word_counts.items():
                word = word.lower()
                tf_idf = tf * word_idf.get(word, 0)  # Si le mot n'existe pas dans IDF, TF-IDF = TF * 0
                file_tf_idf.append(tf_idf)

            word_tf_idf_matrix.append(file_tf_idf)

    return word_tf_idf_matrix
def get_non_important_words(tf_idf_matrix, word_doc_count):
    non_important_words = set()

    # Récupérer les mots ayant un score TF-IDF nul dans tous les fichiers
    for file_tf_idf in tf_idf_matrix:
        for word, tf_idf_score in zip(word_doc_count.keys(), file_tf_idf):
            if tf_idf_score == 0:
                # Ajouter le mot à la liste des mots non importants
                non_important_words.add(word)

    return list(non_important_words)

#fonction qui nous permettra d'afficher le mot associé au plus haut TF-Idf
def get_unique_words(corpus_directory):
    unique_words = set()

    # Parcourir les fichiers du corpus pour extraire les mots uniques
    for filename in os.listdir(corpus_directory):
        with open(os.path.join(corpus_directory, filename), 'r', encoding='utf-8') as file:
            words = file.read().split()
            unique_words.update(words)

    return list(unique_words)
def get_word_with_highest_tfidf(corpus_directory):
    # Calculer la matrice TF-IDF
    tf_idf_matrix = compute_tf_idf(corpus_directory)

    highest_tfidf_score = float('-inf')
    word_associated = None

    # Parcourir la matrice TF-IDF pour trouver le score TF-IDF le plus élevé et son mot associé
    for document in tf_idf_matrix:
        for word, tf_idf_score in enumerate(document):
            if tf_idf_score > highest_tfidf_score:
                highest_tfidf_score = tf_idf_score
                word_associated = word

    # Récupérer le mot associé au score TF-IDF le plus élevé
    unique_words = get_unique_words(corpus_directory)
    word = unique_words[word_associated]

    return word, highest_tfidf_score

def compute_tf2(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
        word_counts = Counter(words)
        return word_counts


def detect_first_president_to_mention(directory):
    # Initialisation des variables
    first_president = None
    first_occurrence = float('inf')  # Initialisation de la première occurrence à une valeur élevée

    # Parcourir les fichiers du répertoire
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

            # Vérifier si les mots clés "climat" ou "écologie" sont présents dans le discours
            if 'climat' in content.lower() or 'écologie' in content.lower():
                # Récupérer le nom du président
                president_name = extraire_nom_president(filename)

                # Vérifier si c'est la première occurrence
                if president_name and president_name not in ['cleaned', 'speeches'] and 'Nomination' not in filename:
                    # Récupérer l'ordre de ce discours dans la liste des discours
                    order_of_occurrence = list_of_files(directory, ".txt").index(filename)

                    # Mettre à jour si c'est la première occurrence trouvée
                    if order_of_occurrence < first_occurrence:
                        first_occurrence = order_of_occurrence
                        first_president = president_name

    return first_president