def anna_vihje(esine, yritykset):
    if yritykset == 0:
        return esine["vihje1"]
    elif yritykset == 1:
        return esine["vihje2"]
    else:
        return esine["vihje3"]
