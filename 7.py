print("введите кол-во копеек")
a=int(input())
b=a//100
a=a-b*100
c=a//10
a=a-c*10
d=a//3
a=a-d*3
e=a*4
print(b, "рублей",c," гривен",d," алтын",e," полушек")
input()