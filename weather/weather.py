import xmltodict, json, sys

def main():

    file = open(sys.argv[1], 'r')
    todict = dict(xmltodict.parse(file.read(), process_namespaces=True, attr_prefix=''))
    filename = ''.join([sys.argv[1][i] for i in range(sys.argv[1].find('.'))])
    file.close()

    todict = todict['current'] #parse root DOM out
    json_preparation = json.dumps(todict, indent=4)
    try:
        file = open(filename + '.json', 'x')
    except FileExistsError:
        file = open(filename + '.json', 'w')
    file.write(json_preparation)
    file.close()

main()
