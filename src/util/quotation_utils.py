def map_quotation_key(data):
    return {k.split(" ")[1]: v for k, v in data.items()}
