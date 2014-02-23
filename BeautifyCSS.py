import re

#prefix = '<tr><td>open</td><td>'
#suffix = '</td><td></td></tr><tr><td>waitForPageToLoad</td><td></td><td>3000</td></tr>'

#with open('reportExtAllCSS.txt','r') as f:
with open('reportInlineCSS.txt','r') as f:
    newlines = []
    for line in f.readlines():
        line=re.sub(r'\/\*\*[^*]*\*+([^/][^*]*\*+)*\/', '\n', line)#erase comments
        line=re.sub(r'/\*[\s\S]*?\*/', '\n', line)#erase comments
        
        if not line.startswith('='):
            if not line.startswith('/*'):
                if not line.startswith('//'):
                    if not line.startswith('-'):
                        line=re.sub(r'\<.+?\>', '', line)#erase <style> tags
                        line=re.sub(r'</style>', '', line)#erase <style> tags
                        line=re.sub(r'\/=.+?=\/', '', line)
                        line=re.sub(r'<!--', '', line)
                        line=re.sub(r'-->', '', line)
                        line=re.sub(r'-- */ ', '\n', line)
                        newlines.append(line)
                            
#with open('CSSDBExt.txt', 'w') as f:            
with open('CSSDBIn.txt', 'w') as f:
    for line in newlines:
        f.write('%s\n' % (line.rstrip('\n')))

#f = open('CSSDBExt.txt')
f = open('CSSDBIn.txt')
text=f.read()
f.close()
text = text.replace('\n','')
clean = re.sub('{.+?}', '\n', text)#remove {css commnads}
clean=re.sub('}', '', clean)
clean=re.sub('\t+', '', clean)#remove start spaces
clean=re.sub('^\s+\s', '\n', clean)#remove start spaces

#f = open('CSSDBExt.txt','w')
f = open('CSSDBIn.txt', 'w')
f.write(clean)
f.close()
