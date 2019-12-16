def conjugate2(verb, number, tense):
    """ Conjugation of french verbs of the first group at present and inperfect tenses.
        Training for École nationale des chartes' TNAH Master degree, by Jean-Damien Généro, 2019.
    :param verb: the verb to conjugate
    :param number: the grammatical person
                (1 = I, 2 = you (french "tu"), 3 = he/she/it, 4 = we, 5 = you (french "vous"), 6 = they)
    :param tense: present or inperfect tense
    :return: the conjugated verb or error message
    :rtype: str
    """
    present = {1: "e", 2: "es", 3: "e", 4: "ons", 5: "ez", 6: "ent"}
    inperfect = {1: "ais", 2: "ais", 3: "ait", 4: "ions", 5: "iez", 6: "aient"}
    if tense == "present":
        return(print(verb[0:-2] + present[number]))
    elif tense == "imparfait":
        return(print(verb[0:-2] + inperfect[number]))
    else:
        return(print("Vous n'avez pas entré un verbe du premier groupe."))

v = str(input("Enter a verb : "))
n = int(input("Enter the grammatical person : "))
t = str(input("Enter the tense : "))

conjugate2(v, n, t)