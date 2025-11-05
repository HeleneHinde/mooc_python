def read_set(filename):
    with open(filename, 'r', encoding='utf8') as f:
        return set(line.strip() for line in f)

def search_in_set(filename_reference, filename):
    reference_set = read_set(filename_reference)
    retour_list = []
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            word = line.strip()
            if word in reference_set:
                retour_list.append((word, True))
            else:
                retour_list.append((word, False))
    return retour_list

def list_to_set(lst):
    return set(lst)

def diff(extended, abbreviated):
    """
    Compare deux listes de données de bateaux et retourne les différences
    
    Args:
        extended: Liste de listes complètes [ID, lat, lon, timestamp, nom, pays, ?, port]
        abbreviated: Liste de listes courtes [ID, lat, lon, timestamp]
    
    Returns:
        tuple: (noms uniquement dans extended, 
                noms communs, 
                IDs uniquement dans abbreviated)
    """
    # Extraction des IDs et noms depuis extended
    extended_ids = set()
    extended_names = set()
    for item in extended:
        boat_id = item[0]  # Premier élément = ID
        boat_name = item[4]  # Cinquième élément = nom du bateau
        extended_ids.add(boat_id)
        extended_names.add(boat_name)
    
    # Extraction des IDs depuis abbreviated  
    abbreviated_ids = {item[0] for item in abbreviated}
    
    # Calculs des différences
    common_ids = extended_ids & abbreviated_ids  # IDs présents dans les deux
    only_abbreviated_ids = abbreviated_ids - extended_ids  # IDs seulement dans abbreviated
    
    # Noms des bateaux communs (présents dans extended ET abbreviated)
    common_names = set()
    only_extended_names = set()
    
    for item in extended:
        boat_id = item[0]
        boat_name = item[4]
        if boat_id in common_ids:
            common_names.add(boat_name)
        else:
            only_extended_names.add(boat_name)
    
    return (only_extended_names, common_names, only_abbreviated_ids)

compteur = 0
for temoin in [ [], True, {}, "", None, False ] + list(range(3)):
    if temoin:
        compteur += 1
print(compteur)

a = 'disparaitre'
while a:
    a = a[:-1]
    print(a)