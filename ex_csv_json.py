#Exercice 1 : Le fichier data/json/twitter.humanitesnumeriques.json contient quelques tweets comprenant la mention "humanites numeriques". Afficher grâce à une boucle les tweets en suivant l'exemple suivant :
#http://twitter.com/statuses/939909652824969216    lapointejm    RT @agefen: L'ouverture de la nouvelle API de Gallica est un événement scientifique majeur pour le paysage des Humanités Numériques en Fran…

#Exercice 2 : À partir du code précédent, transformez l'exercice en chargeant le même fichier JSON et en écrivant un fichier CSV reprenant la structure en colonne : Lien | Auteur | Date | Tweet.


#0. Packages
import json
import csv


#Exercice 1.
with open("data/json/twitter.humanitesnumeriques.json") as json_file :
    twitter_file = json.load(json_file)
    link = "http://twitter.com/statuses/" + (twitter_file["statuses"][0]["id_str"])
    user_id = twitter_file["statuses"][0]["user"]["screen_name"]
    time = twitter_file["statuses"][0]["user"]["created_at"]
    tweet = twitter_file["statuses"][0]["text"]
    print(link, user_id, time, tweet)


#Exercice 2.
#Nota : j'ai créé un fichier tabl_tweet.csv dans le dossier csv pour y mettre le tableau.
row1 = [link, user_id, time, tweet]
with open("data/csv/tabl_tweet.csv", "w") as tabl_tweet :
    spamwritter = csv.writer(tabl_tweet, delimiter=",", quotechar='"')
    spamwritter.writerow(["Lien", "Auteur", "Date", "Tweet"])
    spamwritter.writerow(row1)


#Exercice 3 : à partir du même fichier JSON, écrire un fichier CSV avec les colonnes Lien | Auteur | Date | Tweet et un tweet par ligne.

def tweeter(index):
    link = "http://twitter.com/statuses/" + (twitter_file["statuses"][index]["id_str"])
    user_id = twitter_file["statuses"][index]["user"]["screen_name"]
    time = twitter_file["statuses"][index]["user"]["created_at"]
    tweet = twitter_file["statuses"][index]["text"]
    return([link, user_id, time, tweet])

liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

with open("data/csv/tabl_tweet.csv", "w") as tabl_tweet:
    spamwritter = csv.writer(tabl_tweet, delimiter=",", quotechar='"')
    spamwritter.writerow(["Lien", "Auteur", "Date", "Tweet"])

with open("data/json/twitter.humanitesnumeriques.json") as json_file :
    twitter_file = json.load(json_file)
    for nombre in liste:
        if nombre < len(liste):
            row = tweeter(nombre)
            with open("data/csv/tabl_tweet.csv", "a") as tabl_tweet :
                spamwritter = csv.writer(tabl_tweet, delimiter=",", quotechar='"')
                spamwritter.writerow(row)