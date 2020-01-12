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
    list_column = []

    list_column.append(1)
    list_column.append(metadata[5]["value"]) #file's name
    list_column.append(metadata[2]["value"]) #file's image
    list_column.append(data["sequences"][0]["canvases"][0]["height"]) #height
    list_column.append(data["sequences"][0]["canvases"][0]["width"]) #width

    #4. CSV
    with open (nom_csv, "w") as csv_file :
        writing = csv.writer(csv_file, delimiter=",")
        writing.writerow(colonnes)
        writing.writerow(list_column)

iiif_csv("ark:/12148/btv1b84259980", "/data/csv/pages.csv")