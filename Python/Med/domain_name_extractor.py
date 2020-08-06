import re

def domain_name(url: str):
    # Either python regex hates me or I really suck at it (most likely)
    # m = re.findall(r"(https?:?\/?\/?)?(w{3}?\.?)?([a-z]+\-?[a-z]?+[0-9]?+)\.[\w]+", url) # originally r"https?:\/\/w{3}?}\.?([a-z]+)\.[\w]+'
    m = url.split("www.")[-1].split("//")[-1].split(".")[0]
    return m