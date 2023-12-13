def open_file(file_name):
    with open(file_name, 'r') as fichier:
        contenu = [el.replace("\n", "").split("\t")[1:3]
                   for el in fichier.readlines()
                   if el[0] != "#" and el != "\n"]
    res = [x[0] for x in contenu], [x[1] for x in contenu]
    return res
