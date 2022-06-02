st = input()
cons = 0 
vow = 0
dig = 0 
wht_spa = 0 
for i in st:
    if i=='a' or  i=='e' or i =='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O'or i=='U':
        vow += 1
    elif i>='a' and i<='z'  or i>='A' and i<='Z':
        cons+=1
    elif i>='0' and i<='9':  
        dig += 1
    else:
        wht_spa += 1
print(cons)
print(vow)
print(dig)
print(wht_spa)
