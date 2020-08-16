#program to check wether the string is pangram or not
string=input("enter the string in lower case letters")
alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
k=list(string)
count=0
a=[]
for i in range(0,len(k)):
    if(k[i]==' '):
        continue
    else:
        a.append(k[i])
for i in range(0,len(alp)):
    if alp[i] in a:
        count=count+1
if(count==26):
    print('string is a pangram')
else:
    print('string is not pangram')
    
    

