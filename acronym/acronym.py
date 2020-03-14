import re
def abbreviate(words):
    word=re.findall("[\'A-Za-z]+", words)
    return "".join([w[0:1].capitalize() for w in word])
