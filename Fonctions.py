from collections import Counter
import os
import math
import string
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
    word_tf_dict, _ = compute_tf(corpus_dir)
    word_tf_idf_dict = {}  # Utilisation d'un dictionnaire pour stocker les TF-IDF pour chaque mot

    # Parcourir les fichiers du corpus pour calculer TF-IDF
    for filename in os.listdir(corpus_dir):
        # Lire chaque fichier et compter les mots
        with open(os.path.join(corpus_dir, filename), 'r', encoding='utf-8') as file:
            words = file.read().split()

            # Compter les occurrences de chaque mot dans le fichier
            word_counts = Counter(words)
            total_words_in_doc = sum(word_counts.values())

            # Calculer TF-IDF pour chaque mot dans le fichier
            for word, tf in word_counts.items():
                word = word.lower()
                tf_idf = (tf / total_words_in_doc) * word_idf.get(word, 0)  # Calcul du TF * IDF

                # Ajouter le mot et son TF-IDF au dictionnaire
                if word in word_tf_idf_dict:
                    word_tf_idf_dict[word].append(tf_idf)
                else:
                    word_tf_idf_dict[word] = [tf_idf]

    # Calculer la moyenne des TF-IDF pour chaque mot
    for word, tf_idf_list in word_tf_idf_dict.items():
        word_tf_idf_dict[word] = sum(tf_idf_list) / len(tf_idf_list)

    return word_tf_idf_dict



def get_non_important_words(tf_idf_matrix):
    non_important_words = []
    for word, tf_idf_score in tf_idf_matrix.items():
        if tf_idf_score == 0.0:
            non_important_words.append(word)
    return non_important_words

def get_word_with_highest_tfidf(corpus_directory):
    tf_idf_matrix = compute_tf_idf(corpus_directory)
    highest_tfidf_score = float('-inf')
    word_associated = None
    for word, tf_idf_score in tf_idf_matrix.items():
        if tf_idf_score > highest_tfidf_score:
            highest_tfidf_score = tf_idf_score
            word_associated = word
    return word_associated, highest_tfidf_score

def compute_tf2(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
        word_counts = Counter(words)
        return word_counts

def detect_first_president_to_mention(directory):
    first_president = None
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            if 'climat' in content.lower() or 'écologie' in content.lower():
                president_name = extraire_nom_president(filename)
                if president_name and president_name not in ['cleaned', 'speeches'] and 'Nomination' not in filename:
                    first_president = president_name
                    break
    return first_president

def supprimer_caracteres_speciaux_txt(text):
    for caractere in string.punctuation:
        text = text.replace(caractere, ' ')
    return text

def convertir_majuscules_en_minuscules_txt(text):
    return text.lower()

def tokenizer_question(question):
    question = supprimer_caracteres_speciaux_txt(question)
    question = convertir_majuscules_en_minuscules_txt(question)
    mots = []
    for mot in question.split():
        mots.append(mot)
    return mots

def trouver_termes_dans_corpus(question, directory_cleaned):
    mots_question = tokenizer_question(question)
    termes_dans_corpus = set()
    for filename in os.listdir(directory_cleaned):
        filepath = os.path.join(directory_cleaned, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            mots_corpus = tokenizer_question(content)
            termes_question_dans_corpus = set(mots_question) & set(mots_corpus)
            termes_dans_corpus.update(termes_question_dans_corpus)
    return termes_dans_corpus

def calculate_tf_question(question):
    words_in_question = tokenizer_question(question)
    tf_question = {}
    for word in words_in_question:
        if word in tf_question:
            tf_question[word] += 1
        else:
            tf_question[word] = 1
    return tf_question

def compute_tfidf_question(question, corpus_dir):
    # Obtention des scores IDF et TF du corpus
    word_idf = calculate_idf(corpus_dir)
    word_tf_dict, _ = compute_tf(corpus_dir)

    # Calcul du score TF pour chaque mot de la question
    tf_question = calculate_tf_question(question)

    # Initialisation du vecteur TF-IDF de la question
    tfidf_question = {}

    # Calcul du score TF-IDF pour chaque mot de la question en utilisant les scores IDF du corpus
    for word, tf_question_value in tf_question.items():
        if word in word_idf:
            tfidf_question[word] = tf_question_value * word_idf[word]
        else:
            tfidf_question[word] = 0  # Mettre 0 pour les mots absents dans les scores IDF du corpus

    return tfidf_question

def tokenize_question(question):
    question = question.lower()
    question = question.translate(str.maketrans('', '', string.punctuation))
    tokens = question.split()
    return tokens

def find_terms_in_corpus(question_tokens, idf_scores):
    return [token for token in question_tokens if token in idf_scores]

def calculate_question_tf_idf(question_tokens, unique_words, idf_scores):
    word_freq = Counter(" ".join(question_tokens))
    question_tf_idf = [0] * len(unique_words)
    for i, word in enumerate(unique_words):
        if word in word_freq:
            question_tf_idf[i] = word_freq[word] * idf_scores.get(word, 0)
    return question_tf_idf

def dot_product(vector_a, vector_b):
    return sum(a * b for a, b in zip(vector_a.values(), vector_b.values()))

def vecteur_norm(vector):
    return math.sqrt(sum(a * a for a in vector.values()))

def cosinus_similarité(vector_a, vector_b):
    dot_prod = dot_product(vector_a, vector_b)
    norm_a = vecteur_norm(vector_a)
    norm_b = vecteur_norm(vector_b)
    if norm_a == 0 or norm_b == 0:
        return 0
    return dot_prod / (norm_a * norm_b)

def find_most_relevant_document(tfidf_matrix, question_vector):
    highest_similarity = 0
    most_relevant_doc_index = None  # Pour stocker le nom du document le plus similaire
    for doc_name, doc_vector in tfidf_matrix.items(): # l'erreur vient du départ car on fait des moyennes du tf idf de l'ensemble de chaque dossiers
        similarity = cosinus_similarité(question_vector, doc_vector)
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_relevant_doc_index = doc_name
    return most_relevant_doc_index


def highest_tf_idf_word(question_tf_idf, unique_words):
    highest_score_index = question_tf_idf.index(max(question_tf_idf))
    return unique_words[highest_score_index]

def find_sentence_with_word(text, word):
    sentences = [sentence.strip() + '.' for sentence in text.split('.') if word in sentence]
    return sentences[0] if sentences else ""

def refine_response(question, answer):
    question_starters = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr! ",
    }
    for starter, response_starter in question_starters.items():
        if question.startswith(starter):
            return response_starter + answer[0].upper() + answer[1:]
    return answer[0].upper() + answer[1:]
