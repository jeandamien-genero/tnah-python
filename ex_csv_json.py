#Exercice 1 : Le fichier data/json/twitter.humanitesnumeriques.json contient quelques tweets comprenant la mention "humanites numeriques". Afficher grâce à une boucle les tweets en suivant l'exemple suivant :
#http://twitter.com/statuses/939909652824969216    lapointejm    RT @agefen: L'ouverture de la nouvelle API de Gallica est un événement scientifique majeur pour le paysage des Humanités Numériques en Fran…

#Exercice 2 : À partir du code précédent, transformez l'exercice en chargeant le même fichier JSON et en écrivant un fichier CSV reprenant la structure en colonne : Lien | Auteur | Date | Tweet.


import json
import csv


def tweeter(index):
    """ Makes a list of a tweet's link, user_id, time and text out of a json file which contain metadata from Twitter.
        :param index: the tweet's index in the statuses list
        :return: a list with the tweet's URL (link), username (user_id), date (time) and content (tweet)
        :rtype: str
    """
    link = "http://twitter.com/statuses/" + (twitter_file["statuses"][index]["id_str"])
    user_id = twitter_file["statuses"][index]["user"]["screen_name"]
    time = twitter_file["statuses"][index]["created_at"]
    tweet = twitter_file["statuses"][index]["text"]
    return([link, user_id, time, tweet])

#Solution 1
with open("data/csv/tabl_tweet.csv", "w") as tabl_tweet:
    titlewritter = csv.writer(tabl_tweet, delimiter=",", quotechar='"')
    titlewritter.writerow(["Lien", "Auteur", "Date", "Tweet"]) #
    
with open("data/json/twitter.humanitesnumeriques.json") as json_file :
    twitter_file = json.load(json_file)
    index = 0
    for line in twitter_file["statuses"]:
        row = tweeter(index)
        index += 1
        with open("data/csv/tabl_tweet.csv", "a") as tabl_tweet :
            tweetwritter = csv.writer(tabl_tweet, delimiter=",")
            tweetwritter.writerow(row)


#Solution 2
with open("data/csv/tabl_tweet.csv", "w") as tabl_tweet:
    spamwritter = csv.writer(tabl_tweet, delimiter=",", quotechar='"')
    spamwritter.writerow(["Lien", "Auteur", "Date", "Tweet"])

with open("data/json/twitter.humanitesnumeriques.json") as json_file :
    twitter_file = json.load(json_file)
    nombre = 0
    while (len(twitter_file["statuses"]) - 1) > nombre:
        nombre += 1
        row = tweeter(nombre)
        with open("data/csv/tabl_tweet.csv", "a") as tabl_tweet :
            spamwritter = csv.writer(tabl_tweet, delimiter=",", quotechar='"')
            spamwritter.writerow(row)