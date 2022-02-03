from turtle import listen


liste=[1,2,3]
tuple=(1,"üç",5.5)

print(type(liste))
print(type(tuple))

print(liste[2])
print(tuple[2])

print(len(liste))
print(len(tuple))

# tuple atama yapıldıktan sonra değiştirme yapılamaz
#tuple[0]="israfil" 
#print(tuple)

liste[0]="hakan"

print(liste)