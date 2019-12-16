def conjugue(verb, number):
    """ Conjugation of french verbs from first and second groups and the verb to be.
        Training for École nationale des chartes' TNAH Master degree, by Jean-Damien Généro, 2019.
    :param verb: the verb to conjugate
    :param number: the grammatical person
                (1 = I, 2 = you (french "tu"), 3 = he/she/it, 4 = we, 5 = you (french "vous"), 6 = they)
    :return: the conjugated verb or an error message
    :rtype: str
    """
    if verb[-2:] == "er": #pour les verbes du premiers groupe
        radical_er = verb.replace("er", "")
        if number == 1 :
            conjugation = radical_er + "e"
        elif number == 2 :
            conjugation = radical_er + "es"
        if number == 3 :
            conjugation = radical_er + "e"
        elif number == 4 :
            conjugation = radical_er + "ons"
        elif number == 5 :
            conjugation = radical_er + "ez"
        elif number == 6 :
            conjugation = radical_er + "ent"
        return (conjugation)
    elif verb[-2:] == "ir": #pour les verbes du deuxième groupe
        radical_ir = verb.replace("ir", "")
        if number == 1 :
            conjugation = radical_ir + "is"
        if number == 2 :
            conjugation = radical_ir + "is"
        elif number == 3 :
            conjugation = radical_ir + "it"
        elif number == 4 :
            conjugation = radical_ir + "issons"
        elif number == 5 :
            conjugation = radical_ir + "issez"
        elif number == 6 :
            conjugation = radical_ir + "issent"
        return (conjugation)
    elif verb == "être": #pour le verbe être
        if number == 1 :
            conjugation = "Je suis"
        if number == 2 :
            conjugation = "Tu es"
        elif number == 3 :
            conjugation = "Il/Elle est"
        elif number == 4 :
            conjugation = "Nous sommes"
        elif number == 5 :
            conjugation = "Vous êtes"
        elif number == 6 :
            conjugation = "Ils sont"
        return (conjugation)
    else:
        error = "Vous n'avez pas entré un verbe."
        return(error)

#print(conjugue("commander", 1))
assert conjugue("manger", 2) == "manges"
assert conjugue("balayer", 5) == "balayez"
assert conjugue("travailler", 4) == "travaillons"