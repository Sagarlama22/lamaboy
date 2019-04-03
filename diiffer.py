a=["apple","orange","mango"]
b=("22","grapes","watermelon")
for z in a :
    print(z)
a.append("guava")
print(a)
a.remove("mango")
print(a)
if "orange" in a:
            print("yes it does")
a[0]="promogranate"
print(a)
print(len(a))
x=234
x=a.copy()
print(x)
y=(a.count("orange"))
print(y)
print(a[2])


b=("BMW","FORD","BBT")
print(b[1])
print(b*2)
print(len(b))


c={"IGN","RYZEN","RRQ"}
c.add("EVOS")
print(c)
c.remove("RYZEN")
print(c)
c.pop()
print(c)


d={"apple","mango","cherry"}
e={"cat","dog","bird"}
d.update(e)
print(d)
z=d.difference(e)
print(z)
d.intersection(e)
print(d)
d.difference_update(e)
print(d)
