import re

#prefix = '<tr><td>open</td><td>'
#suffix = '</td><td></td></tr><tr><td>waitForPageToLoad</td><td></td><td>3000</td></tr>'

with open('CSSDB.txt','r') as f:
    newlines = []
    for line in f.readlines():
        line=re.sub(r'^\s*', '', line)
        line=line.replace(':link', '')
        line=line.replace(':visited', '')
        line=line.replace(':active', '')
        line=line.replace(':hover', '')
        line=line.replace(':focus', '')
        line=line.replace(':-o-prefocus', '')
        line=line.replace(':first-letter', '')
        line=line.replace(':first-line', '')
        line=line.replace(':before', '')
        line=line.replace(':after', '')
        
        if not line.startswith('@'):
            temp=re.findall (r':nth-[a-z\-]+\([^)]+\)', line)
            
            line=re.sub(r'(:nth-[a-z\-]+)\([^)]+\)',r'\1()', line)
            line=re.sub(r'^[0-9].*', '', line)
            line=re.sub(r'^to$', '', line)
            line=re.sub(r'::[^\n,]+', '', line)
            line=re.sub(r'#[^\.\s,>:+\*~#\)]+', '#id', line)#create ids
            line=re.sub(r'\.[^\.\s,>:+\*~#\)]+', '.class', line)#create classes
            line=re.sub(r'([\s,>+\(])[^\.\s,>:+\*~#\[\)]+', r'\1tag', line)#create tags
            line=re.sub(r'([*~])[^=\.\s,>:+\*~#\[\)]+', r'\1tag', line)
            line=re.sub(r'^[^\.\s,>:+\*~#\[]+', 'tag', line)#for the beginning tags
            line=re.sub(r':lang\(.*\)', '', line)
            line=re.sub(r'\[[^\^\$\*\|\!~=\]]+', '[name', line)#create attributes names
            line=re.sub(r'\[name([\^\$\*\|\!~]?=)\"?([^\"\]]+)"?\]', r'[name\1value]', line)#create attributes values
            line=re.sub(r'gt\(\s*tag\s*\)', 'gt(value)',line)
            line=re.sub(r'lt\(\s*tag\s*\)', 'lt(value)',line)
            line=re.sub(r'eg\(\s*tag\s*\)', 'eg(value)',line)
            line=re.sub(r'contains\(\s*tag\s*\)', 'contains(value)',line)
            if not line=='\n':
                newlines.append(line)
                if temp:
                    newlines.append(str(temp))
   
with open('CSSDBCriteria.txt', 'w') as f:
    for line in newlines:
        f.write('%s\n' % (line.rstrip('\n')))
        