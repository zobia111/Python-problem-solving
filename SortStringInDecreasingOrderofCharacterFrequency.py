# Program Problem: sort string in decreasing order of character frequency
#Asked by twitter in an interview

def KeyExists(str):
    if str in thisdict:
        global updatedFrequency
        updatedFrequency=thisdict.get(str)+1
        return 1

#--------------------------------------------------------------------------
string=input('Enter a string: ')
frequency=1
thisdict={}
row=""

for x in string:
    if(KeyExists(x)):
        
        thisdict[x] = updatedFrequency
        
    else:
        thisdict[x] = frequency

#lambda is un-named one line function, reverse for descending order
thisdict = sorted(thisdict.items(), key=lambda x: x[1], reverse=True)

#print string in order of decreasing frequency
#row=x*y, if ch=t and freuency=2 then print "tt"
for x, y in thisdict:
        row+=x*y
print('output: ',row)

















