plik = open('liczby.txt')
data = plik.read().splitlines()
#data = ['45','19','8542','11264','471046105']
counter = 0
for number in data:
    r = []
    for char in number:
        r.insert(0,char)
    s= str(int(number)+int(''.join(r)))
    #print(str(s))

    i=0
    j=len(s)-1
    palindrom = True
    while i<j:
        if(s[i] != s[j]):
            palindrom = False
            break
        else:
            i += 1
            j -= 1
    if(palindrom):
        counter += 1

print(counter)