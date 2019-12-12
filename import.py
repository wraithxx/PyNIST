import sqlite3
import xmltodict
import os


conn = sqlite3.connect('C:/Users/smayberry/Documents/Source/python_projects/NIST/nist.db')
fn = 'C:/Users/smayberry/Documents/Source/python_projects/NIST/800-53-controls.xml'
c = conn.cursor()
print(conn)
print(fn)


def get_nested(data, *args):
    if args and data:
        element = args[0]
        if element:
            v = data.get(element)
            return v if len(args) == 1 else get_nested(v, *args[1:])


with open(fn) as fd:
    obj = xmltodict.parse(fd.read())

for control in obj['controls:controls']['controls:control']:
    print(control['family'])
    print(control['number'])
    print(control['title'])
    if 'statement' in control['statement']:
        for statement in control['statement']['statement']:
            print(statement['number'])
