#Exercice 1 = Le fichier data/json/twitter.humanitesnumeriques.json contient quelques tweets comprenant la mention "humanites numeriques". Afficher grâce à une boucle les tweets en suivant l'exemple suivant :
#http://twitter.com/statuses/939909652824969216    lapointejm    RT @agefen: L'ouverture de la nouvelle API de Gallica est un événement scientifique majeur pour le paysage des Humanités Numériques en Fran…

#Exercice 2 = À partir du code précédent, transformez l'exercice en chargeant le même fichier JSON et en écrivant un fichier CSV reprenant la structure en colonne : Lien | Auteur | Date | Tweet.


#0. Packages
import json
import csv


#Exercice 1.
with open("data/json/twitter.humanitesnumeriques.json") as json_file :
    twitter_file = json.load(json_file)
    tweet = twitter_file["statuses"]
    first_tweet = tweet[0]
    username = first_tweet["user"]
    link = "http://twitter.com/statuses/" + first_tweet["id_str"]
    user_id = username["screen_name"]
    time = username["created_at"]
    txt = first_tweet["text"]
    row1 = [link, user_id, time, txt]


#Exercice 2.
#Nota : j'ai créé un fichier tabl_tweet.csv dans le dossier csv pour y mettre le tableau.
with open("data/csv/tabl_tweet.csv", "w") as tabl_tweet :
    spamwritter = csv.writer(tabl_tweet, delimiter=",", quotechar='"')
    spamwritter.writerow(["Lien", "Auteur", "Date", "Tweet"])
    spamwritter.writerow(row1)