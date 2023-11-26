Lien GitHub: https://github.com/Milyagami/CHATBOT-public-.git

Partie 1 :
My first ChatBot

Mathieu Rat
Milhane aifi

Bonjour,
Comme demandé, voici une petite explication de ce que fais chaque fonction dans le dossier fonctions.py
Pour leur exécution, veuillez lancer le main.py et les instructions seront donné au fur et à mesures
Explication fonctions :

-	extraire_nom_president(nom_fichier):

Cette fonction extrait le nom du président à partir du nom d'un fichier en supprimant le préfixe "Nomination_" et les chiffres à la fin du nom. Elle renvoie le nom du président résultant.
-	prenom_president(nom_pres):
Cette fonction prend le nom du président en entrée et renvoie le prénom correspondant en utilisant des correspondances conditionnelles sur le nom du président.
-	liste_nom_president(fichier__texte):
Cette fonction crée une liste de noms de présidents uniques en parcourant une liste de noms de fichiers texte. Elle utilise la fonction extraire_nom_president pour extraire les noms des présidents et les ajoute à la liste uniquement s'ils ne sont pas déjà présents.
-	convertir_majuscules_en_minuscules(chemin_fichier_majuscules, chemin_fichier_minuscules):

Cette fonction lit le contenu d'un fichier en majuscules, convertit le texte en minuscules, puis écrit le résultat dans un nouveau fichier. Elle est utilisée pour normaliser la casse du texte.
-	convertir_fichiers_en_minuscules(directory, extension, repertoire_cleaned):
Cette fonction parcourt tous les fichiers d'un répertoire avec une certaine extension, convertit leur contenu en minuscules à l'aide de convertir_majuscules_en_minuscules, puis écrit les nouveaux fichiers dans un répertoire "cleaned".
-	list_of_files(directory, extension):
Cette fonction renvoie une liste de noms de fichiers dans un répertoire avec une certaine extension en filtrant les fichiers par extension.
-	supprimer_caracteres_speciaux(directory_cleaned):

Cette fonction supprime les caractères spéciaux (sauf apostrophe et tiret) de tous les fichiers dans un répertoire "cleaned". Elle est utilisée pour éliminer les caractères non pertinents des discours.
-	compute_tf(corpus_dir):

Cette fonction calcule la fréquence des termes (TF) pour chaque mot dans un corpus de documents. Elle compte le nombre d'occurrences de chaque mot dans chaque document.
-	calculate_idf(corpus_dir):

Cette fonction calcule l'inverse de la fréquence du document (IDF) pour chaque mot dans un corpus de documents. Elle utilise les résultats de compute_tf pour déterminer la fréquence de chaque mot dans l'ensemble du corpus.
-	compute_tf_idf(corpus_dir):

Cette fonction utilise les fonctions précédentes (compute_tf et calculate_idf) pour calculer la matrice TF-IDF pour chaque mot dans un corpus de documents.
-	get_non_important_words(tf_idf_matrix, word_doc_count):

Cette fonction identifie les mots qui ont un score TF-IDF nul dans tous les fichiers. Ces mots sont considérés comme non importants dans le contexte du corpus.
-	get_unique_words(corpus_directory):

Cette fonction renvoie la liste des mots uniques dans tous les fichiers d'un répertoire. Elle est utilisée pour créer une liste de mots uniques présents dans l'ensemble du corpus.
-	get_word_with_highest_tfidf(corpus_directory):

Cette fonction renvoie le mot associé au score TF-IDF le plus élevé dans l'ensemble du corpus. Elle utilise la matrice TF-IDF calculée par compute_tf_idf.


-	compute_tf2(file_path):

Cette fonction calcule la fréquence des termes (TF) pour chaque mot dans un fichier spécifique. Elle est une version simplifiée de la fonction compute_tf pour un seul fichier.
-	detect_first_president_to_mention(directory):

Cette fonction identifie le premier président à mentionner les mots clés "climat" ou "écologie" dans l'un de ses discours. Elle parcourt les fichiers d'un répertoire et utilise la fonction extraire_nom_president pour extraire les noms des présidents. Elle identifie le premier discours qui contient les mots clés spécifiés.


https://github.com/Milyagami/CHATBOT-public-.git

