import shlex
from compiler.ast import Print

allselectors={}
total=0
#with open('CSSDBCriteria.txt','r') as f:
with open('CSSDBCriteria.txt','r') as f:
    newlines = []
    for line in f.readlines():
        line=line.rstrip('\n')
        if line in allselectors:
            times=allselectors.get(line)
            allselectors[line]=times+1
            total+=1
            continue
        else:
            allselectors[line] = 1
            continue
keylist = allselectors.keys()
keylist.sort()
#print total
for key in keylist:
    times = allselectors[key]
    percentage = float(times)/total
    #print "%s" % key
    #print "%s" % allselectors[key]
    #print "%.2f" % percentage
    print "%s : %s is %.2f" % (key, allselectors[key],percentage)
    
print ('*********************************************')    
print (allselectors['#id'])    
print (allselectors['.class'])
print (allselectors['tag'])
            


