#Correction
import csv
import requests

def iiif_csv(ark, csv_name):
    """ Displays the metada of a BnF's manuscript out of its json file, and write in a .csv a table with pages' informations (number, name, link, width and height).
    :param ark: BnF's ark id
    :type ark: str
    :param csv_name: csv file where the table will be written
    :type nom_csv: str
    :return : none
    """
    columns = ["Number", "Page name", "Image link", "Width", "Height"]
    r = requests.get("http://gallica.bnf.fr/iiif/" + ark + "/manifest.json")
    data = r.json()

    for x in data["metadata"]:
        print(x["label"] + " " + x["value"])

    with open(csv_name, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(columns)
        number = 0
        for canvases in data["sequences"][0]["canvases"]:
            number += 1
            page_name = canvases["label"]
            image_link = canvases["images"][0]["resource"]["@id"]
            width = canvases["width"]
            height = canvases["height"]
            csv_writer.writerow([number, page_name, image_link, width, height])

    return None

iiif_csv("ark:/12148/btv1b84259980", "/Users/jdgenero/Desktop/M2_Cours/cours-python-master/data/csv/pages.csv")

#Proposition
def iiif_csv(ark, nom_csv):
    """ Displays the metada of a BnF's manuscript out of its json file, and write in a .csv a table with pages' informations (number, name, picture'link, hight and width)
    :param ark: BnF's ark id
    :type ark: str
    :parm nom_csv: csv file where the table will be written
    :type nom_csv: str
    :return : none
    """

    import requests
    import csv

    colonnes = ["Numéro", "Nom de Page", "Lien image", "Largeur", "Longueur"]

    #1. Url, request, json
    url = "http://gallica.bnf.fr/iiif/" + ark + "/manifest.json"
    r = requests.get(url)
    data = r.json()

    #2. Metadata
    metadata = data["metadata"]
    print(metadata)

    #3. Making of the table

    #4. CSV
    with open (nom_csv, "w") as csv_file :
        writing = csv.writer(csv_file, delimiter=",")
        writing.writerow(colonnes)
        numero = 0
        for canvas in data["sequences"][0]["canvases"] :
            numero += 1
            page_name = canvas["label"]
            image_link = canvas["images"][0]["ressource"]["@id"]
            hauteur = canvas["height"]
            largeur = canvas["width"]
            csv_writer.writerow([numero, page_name, image_link, hauteur, largeur])

iiif_csv("ark:/12148/btv1b84259980", "/data/csv/pages.csv")