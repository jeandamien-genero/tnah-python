def conjugate(verb, number):
    """ Conjugation of french verbs from the first group.
        Training for École nationale des chartes' TNAH Master degree, by Jean-Damien Généro, 2019. Contributor : Anne Brunnet.
    :param verb: the verb to conjugate
    :param number: the grammatical person
                (1 = I, 2 = you (french "tu"), 3 = he/she/it, 4 = we, 5 = you (french "vous"), 6 = they)
    :return: the conjugated verb
    :rtype: str
    """
    person = {1: "e", 2: "es", 3: "e", 4: "ons", 5: "ez", 6: "ent"}
    if verb[-3:] == "ger" and number == 4:
        return(print(verb[0:-2] + "e" + person[number]))
    elif verb[-3:] == "cer" and number == 4:
        return(print(verb[0:-3] + "ç" + person[number]))
    else:
        return(print(verb[0:-2]+person[number]))

verb = str(input("Enter a verb : "))
gram_person = int(input("Enter the grammatical person : "))
list(verb)
conjugate(verb, gram_person)
