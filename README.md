# SentimentAnalysis
Utilisation d'un classifieur de bayes naif pour l'analyse de sentiment d'un article en utilisant la librairie nltk
================================================
Le but du programme est de déterminer si un article musical emet un opinion positive ou négative.

J'ai utilisé un classifier de type bayes naif, présent dans la librairie nltk v2.04. 
Ce programme est décomposé en deux partie : une partie apprentissage et une partie de test. J'ai utilisé 2000 reviews positives et 2000 reviews négative appartenant à un corpus d'annotation de film. (http://ai.stanford.edu/~amaas/data/sentiment/)
Une fois le corpus analysé, les données sont regroupées dans deux fichiers .pickle qui seront par la suite utilisés dans TryArticle.py
Dans le dossier test sont regroupés 4 articles pitchfork (2 négatifs 0.6/10 et 1.6/10 et 2 positifs 7.8 et 8.1)

1  : Dézipper le fichier train.zip
2  : Lancer TrainCorpus.py
3  : Insérer un article en format txt dans le dossier Test
4  : Faire correspondre le nom de l'article à analyser à la ligne 39 de TryArticle.py
5  : Lancer TryArticle.py



