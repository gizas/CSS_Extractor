import re

#prefix = '<tr><td>open</td><td>'
#suffix = '</td><td></td></tr><tr><td>waitForPageToLoad</td><td></td><td>3000</td></tr>'
with open('reportExternalCSS.txt','r') as f:
    newlines = []
    for line in f.readlines():
        if  not line.startswith('='):
                newlines.append(line)
            
with open('reportExtCSSmodified.txt', 'w') as f:
    for line in newlines:
        f.write('%s\n' % (line.rstrip('\n')))