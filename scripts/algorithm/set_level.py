def set_level(id_dict, depth):
    """
    Defines the cluster label.

    Parameters
    ----------
    id_dict
    depth : int
      Tree depth level.
    """
    id = 0
    while True:
        if id not in id_dict[depth]:
            id_dict[depth].append(id)
            return f'Lvl {depth} - {id}'
        if id in id_dict[depth]:
            id += 1