#Exercice 1 : Le fichier data/json/twitter.humanitesnumeriques.json contient quelques tweets comprenant la mention "humanites numeriques". Afficher grâce à une boucle les tweets en suivant l'exemple suivant :
#http://twitter.com/statuses/939909652824969216    lapointejm    RT @agefen: L'ouverture de la nouvelle API de Gallica est un événement scientifique majeur pour le paysage des Humanités Numériques en Fran…

#Exercice 2 : À partir du code précédent, transformez l'exercice en chargeant le même fichier JSON et en écrivant un fichier CSV reprenant la structure en colonne : Lien | Auteur | Date | Tweet.


import json
import csv


#Correction ex. 1
with open("data/json/twitter.humanitesnumeriques.json") as json_file :
    tweets = json.load(json_file)
for tweet in tweets["statuses"]:
    print("http://twitter.com/statuses/{0} {1} {2}".format(
    tweet["id_str"], tweet["user"]["screen_name"],
    tweet["text"]
    ))


#Ex 2
def tweeter(index):
    """ Makes a list of a tweet's link, user_id, time and text out of a json file which contain metadata from Twitter.
        :param index: the tweet's index in the statuses list
        :return: a list with the tweet's URL (link), username (user_id), date (time) and content (tweet)
        :rtype: list
    """
    link = "http://twitter.com/statuses/" + (twitter_file["statuses"][index]["id_str"])
    user_id = twitter_file["statuses"][index]["user"]["screen_name"]
    time = twitter_file["statuses"][index]["created_at"]
    tweet = twitter_file["statuses"][index]["text"]
    return [link, user_id, time, tweet]
"""
NB : this function can not be used with all the files but only with the current file of the exercice. 
Correction to make it universal (you need to add a file "data" param) :
def affichage_tweet(index, data):
    lien = "http://twitter.com/statuses/" + \
           data["statuses"][index]["id_str"]
    auteur = data["statuses"][index]["user"]["screen_name"]
    date = data["statuses"][index]["user"]["created_at"]
    tweet = data["statuses"][index]["text"]
    return [lien, auteur, date, tweet]
"""

with open("data/csv/tabl_tweet.csv", "w") as tabl_tweet:
    titlewritter = csv.writer(tabl_tweet)
    titlewritter.writerow(["Lien", "Auteur", "Date", "Tweet"])
with open("data/json/twitter.humanitesnumeriques.json") as json_file :
    twitter_file = json.load(json_file)
    index = 0
    for line in twitter_file["statuses"]:
        row = tweeter(index)
        index += 1
        with open("data/csv/tabl_tweet.csv", "a") as tabl_tweet :
            tweetwritter = csv.writer(tabl_tweet)
            tweetwritter.writerow(row)

#Correction ex. 2
def affichage_propre(statut):
    lien = "http://twitter.com/statuses/" + statut["id_str"]
    auteur = statut["user"]["screen_name"]
    date = statut["created_at"]
    tweet = statut["text"]
    return [lien, auteur, date, tweet] # pas besoin de mettre des paranthèses


with open("data/json/twitter.humanitesnumeriques.json") as json_file:
    tweeter_f = json.load(json_file)

with open("data/csv/tabl_tweet.csv", mode="w") as csv_file:
    head_writer = csv.writer(csv_file)
    head_writer.writerow(["Lien", "Auteur", "Date", "Tweet"])

    for line in tweeter_f["statuses"]:
        row = affichage_propre(line)
        head_writer.writerow(row)