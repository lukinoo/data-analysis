def handle_key_values(d, el, _class):
    return d.find(el, {"class": _class}).text.strip()
