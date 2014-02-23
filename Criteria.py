import shlex
from compiler.ast import Print

allselectors={}

with open('CSSDBCriteria.txt','r') as f:
#with open('reportInlineCSS.txt','r') as f:
    newlines = []
    for line in f.readlines():
        line=line.rstrip('\n')
        if line in allselectors:
            times=allselectors.get(line)
            allselectors[line]=times+1
            continue
        else:
            allselectors[line] = 1
            continue

print (allselectors)
print (allselectors['#id'])
print (allselectors['.class'])
print (allselectors['tag'])
            


