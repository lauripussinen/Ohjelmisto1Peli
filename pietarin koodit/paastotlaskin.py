def vaikeustaso(H, K, V, km, vaikeustaso):
    if vaikeustaso == 'H':
        return km * 0.2
    elif vaikeustaso == 'K':
        return km * 0.4
    elif vaikeustaso == 'V':
        return km * 0.6