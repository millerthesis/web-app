from helpers.entity import get_states



def get_indexes():
    r = {}
    r['gentrification'] = gentrification_index()

    return r







def gentrification_index(n=10):
    index = {}

    index['states'] = sorted(get_states(), key=lambda x: x['Percent foreign born'], reverse=True)[0:n]
    for s in index['states']:
        s['gentrification_index'] = s['Percent foreign born']

    return index
