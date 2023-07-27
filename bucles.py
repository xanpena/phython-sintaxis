nombre = "Xan"
# if
if nombre == "Juan":
    print("Hola Juan")
else:
    print("Hola Xan")
 
# while
contador = 0
while contador < 5:
    print("numero %i" % contador)
    contador = contador + 1

# for
print(range(4))
for i in range(4):
    print("Numero %i" % i)


for i in "Hola Mundo":
    print("%s" % i)

# zip
print(list(zip(range(1,4),["ana","juan","pedro"])))

for x,y in zip(range(1,4),["ana","juan","pedro"]):
    print(x,y)    

