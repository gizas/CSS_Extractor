import re

prefix = 'http://'
#suffix = '</td><td></td></tr><tr><td>waitForPageToLoad</td><td></td><td>3000</td></tr>'
with open('top100_alexa.txt','r') as f:
    newlines = []
    for line in f.readlines():
        found=re.sub(r'\d+', '', line)
        line=found
        newlines.append(line.replace(',', ''))
with open('urls.txt', 'w') as f:
    for line in newlines:
        #f.write('%s%s%s\n' % (prefix, line.rstrip('\n'), suffix))
        f.write('%s%s\n' % (prefix, line.rstrip('\n')))